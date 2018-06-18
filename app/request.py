from app import app
import urllib.request,json
from .models import news

News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
	'''
	Function that gets the json response to our url request
	'''
	get_news_url = base_url.format(category,api_key)
	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = None

		if get_news_response['results']:
			news_results_list = get_news_response['results']
			news_results = process_results(news_results_list)

	return news_results

def process_results(news_list):
	'''
	Function that processes the results and transform them to a list of objects
	'''
	news_results = []
	for news_item in news_list:
		id = news_get('id')
		name = news_get('name')
		description = news_get('description')
		image = news_get('image_path')
		category = news_get('category')
		language = news_get('language')
		country = news_get('country')

		if image:
			news_object = News(id,name,description,image,category,language,country)
			news_results.append(news_object)
	return news_results
def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
        	id = news_details_response.get('id')
        	name = news_details_response.get('original_name')
        	description = news_details_response.get('description')
        	image = news_details_response.get('image_path')
        	category = news_details_response.get('category')
        	language = news_details_response.get('language')
        	country = news_details_response.get('country')

        	news_object = News(id,name,description,image,category,language,country)

        	return news_object
