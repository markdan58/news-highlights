from flask import render_template
from app import app
from .requests import get_articles, get_sources

@app.route('/')
def index():
    """ View root page function that returns the index page and it's data """

    # Getting popular movie
    headlines = get_articles('top-headlines', 'business')
    all_sources = get_sources('sources', '')
    print(headlines)
    title = "Up to date news headlines"
    return render_template('index.html', title = title, headlines = headlines, all_sources = all_sources)
