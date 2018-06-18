from flask import render_template
from app import app
from .request import get_news,get_news
# Views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    business_news = get_news('business')
    entertainment_news = get_news('entertainment')
    general_news = get_news('general')
    health_news = get_news('health')
    sports_news = get_news('sports')
    technology_news = get_news('technology')

    title = 'News'

    return render_template('index.html', title = title, business = business_news, entertainment = entertainment_news, general = general_news, health = health_news, sports = sports_news, technology = technology_news)

@app.route('/movie/<int:id>')
def news(news_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    news = get_news(id)
    name = f'{news.name}'

    return render_template('news.html', news = news, name = name)
