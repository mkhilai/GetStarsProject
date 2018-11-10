from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class GetReposList(generics.ListAPIView):

	def list(self, request, *args, **kwargs):

		return Response("ok", status=status.HTTP_200_OK)