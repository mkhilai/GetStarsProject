# GetStarsProject

The project scraps the https://github.com/trending page and returns an object containing title, number of stars and watchers. In order to use it, a GET request needs to be sent to the following API endpoint:

- localhost:8000/repos/

The are two search parameters available: "limit" and "search_word". They can be used as following:

- localhost:8000/repos/?limit=NUMBER_OF_REPOS_TO_LIMIT
- localhost:8000/repos/?search_word=THE_NAME_OF_THE_REPO

- NUMBER_OF_REPOS_TO_LIMIT - could limit the number of repos to display
- THE_NAME_OF_THE_REPO - can search by the repo name, as shown on the trending page

The project was implemented using Python 3, Django and Django Rest Framework
