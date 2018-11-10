from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import re


class GetReposList(generics.ListAPIView):

	def get_parsed_data(self, url):
		parse_data = None
		response = urlopen(url)

		if response.status == 200:
			get_data = response.read()
			parse_data = BeautifulSoup(get_data, features="html.parser")

		return parse_data

	def list(self, request, *args, **kwargs):

		main_page = self.get_parsed_data("https://github.com/trending")

		if main_page:

			final_result = None

			trending_links = []
			for li in main_page.findAll('div', attrs={'class': re.compile("d-inline-block col-9 mb-1")}):
				for div in li.findAll('h3'):
					for a in div.findAll('a'):
						trending_links.append(a.get('href'))

			result = []
			for index in range(len(trending_links)):
				temp_repo = self.get_parsed_data("https://github.com/" + trending_links[index])
				result.append(
					{
						"title": [item.string for item in temp_repo.find('title')],
						"stars": [a.get('aria-label') for a in temp_repo.findAll('a', attrs={'href': re.compile(trending_links[index] + "/stargazers")})],
						"watchers": [a.get('aria-label') for a in temp_repo.findAll('a', attrs={'href': re.compile(trending_links[index] + "/watchers")})]
					}
				)

			return Response(result, status=status.HTTP_200_OK)

		return Response(status=status.HTTP_400_BAD_RQUEST)




