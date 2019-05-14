from django.shortcuts import render, redirect
import requests
from django.conf import settings

# Create your views here.

def index(request):
	context = {}
	categories = ['now_playing', 'upcoming', 'popular', 'top_rated']
	
	try:
		for category in categories:
			endpoint = 'https://api.themoviedb.org/3/movie/{category}?api_key={api_key}&language=en-US&page=1'
			url = endpoint.format(category=category, api_key=settings.TMDB_API_KEY)
			response = requests.get(url)
			context[category] = response.json()

	except:
		context['success'] = False
		context['message'] = 'Connection To TMDB API not available at the moment, Check Your Internet Connection and Try again later'

	
	return render(request, 'movies/index.html', context)


def search(request):
	result = {}
	if 'q' in request.GET:
		query = request.GET['q']

		try:
			endpoint = 'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'
			url = endpoint.format(api_key = settings.TMDB_API_KEY, query = query)
			response = requests.get(url)
			result = response.json()
			result['searched_item'] = query
			result['success'] = True 
		except:
			result['searched_item'] = query
			result['message'] = 'Connection to TMDB API not Available at the moment try again later'
			result['success'] = False
	return render(request, 'movies/result.html', {'result': result})


			


def detail(request, id):
	movie_detail = {}

	try:
		endpoint = 'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US&append_to_response=videos'
		url = endpoint.format(movie_id=id, api_key=settings.TMDB_API_KEY)
		response = requests.get(url)
		movie_detail = response.json()
		movie_detail['success'] = True
	except:
		movie_detail['success'] = False
		movie_detail['message'] = 'Connection To TMDB API not available at the moment, Check Your Internet Connection and Try again later'

	return render(request, 'movies/detail.html', {'movie_detail': movie_detail})

	

