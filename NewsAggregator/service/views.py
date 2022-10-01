import feedparser
from newspaper import Article
from datetime import timedelta

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from service import models


@require_http_methods(['GET'])
def home_view(request):
    news_cat = request.GET.get('news_cat')
    if news_cat is None or news_cat not in ('TPS', 'SPR', 'TCH', 'BSN', 'ENT'):
        news_cat = 'TPS'
    news, created = models.CategoryUrlsModel.objects.get_or_create(news_cat=news_cat)
    refresh_news = False
    REFRESH_TIME = 5
    if created:
        refresh_news = True
    elif (timedelta(minutes=REFRESH_TIME) + news.updated) < timezone.now():
        refresh_news = True

    if refresh_news:
        fetch_news(news_cat)
    return render(request, 'service/home.html', {'news': news, 'news_cat': news_cat})


def fetch_news(news_cat):
    categories = {
        'TPS': 'top_stories_url',
        'ENT': 'entertainment_url',
        'BSN': 'business_url',
        'SPR': 'sports_url',
        'TCH': 'tech_url',
    }

    sources = models.NewsSourceModel.objects.values()
    news_links = []
    for source in sources:

        # Extracts news links from XML Feed of News website
        f = feedparser.parse(source[categories[news_cat]])
        MAX_LINKS = 5 # Max number of links to extract from each News Source
        for i in range(MAX_LINKS):

            try:
                # Parse links and extract Keywords and Summary using NLP
                article = Article(f['entries'][i]['link'])
                article.download()
                article.parse()
                article.nlp()

                news_links.append(
                    {
                        'url': f['entries'][i]['link'],
                        'keywords': article.keywords,
                        'summary': article.summary,
                        'news_source_id': source['id'],
                        'title': f['entries'][i]['title'],
                    }
                )
            except:
                continue

    # Now compare News links for duplicates
    pop_indexes = []
    for i in range(len(news_links)):
        list1 = news_links[i]['keywords']

        if i <= (len(news_links) - 2):
            remaining_list = news_links[i+1:]
            for element in remaining_list:
                list2 = element['keywords']
                match_percentage = match_lists(list1, list2)

                if match_percentage >= 50:
                    pop_indexes.append(news_links.index(element))

    # Pop the duplicate elements
    for pop_index in pop_indexes:
        news_links.pop(pop_index)

    # Now store the links in the database
    q, _ = models.CategoryUrlsModel.objects.get_or_create(news_cat=news_cat)
    for news_link in news_links:
        q.urls.create(
            url=news_link['url'],
            news_source_id=news_link['news_source_id'],
            keywords=news_link['keywords'],
            summary=news_link['summary'],
            title=news_link['title'],
        )
    q.save()


# Match two Lists and return the Match Percentage
def match_lists(list1, list2):
    match_count = 0

    for element in list1:
        if element in list2:
            match_count = match_count + 1

    match_percentage = int(round(((match_count * 100) / len(list1)), 0))
    return match_percentage
