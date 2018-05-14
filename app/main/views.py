from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Sources

@main.route('/')
def index():
    '''
    categories:business, entertainment, general, health, science, sports, technology
    '''
    news_categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    sources_list=[get_sources(source) for source in news_categories]
    sources_dict=dict(zip(news_categories,sources_list))
    title = "News Highlighter"
    return render_template('index.html',title = title, business_sources =sources_dict['business'],
    sports_sources = sources_dict['sports'],technology_sources = sources_dict['technology'],entertainment_sources = sources_dict['entertainment'],
    health_sources=sources_dict['health'],general_sources=sources_dict['general'],science_sources=sources_dict['science'])

@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    import string
    articles = get_articles(id)
    title = string.capwords(id.replace("-"," "))
    return render_template('article.html',title= title,articles = articles)