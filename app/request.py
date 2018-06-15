from app import app
import urllib.request,json
from .models import News

News = news.News


api_key = app.config['MOVIE_API_KEY']

base_url = app.config["MOVIE_API_BASE_URL"]


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        movie_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results


def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in movie_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')

        if poster:
            mnews_object = Movie(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return movie_results
