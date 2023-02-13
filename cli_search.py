"""
CLI Search utilizing search engines
Author: Brian Morillo
Date: 10/29/2022

"""
from search_factory import SearchFactory
from search import GoogleSearch, DuckDuckGoSearch, RedditSearch
import sys
import webbrowser


def search(search_factory, search_engine_name, q):
    """Searches keyword on the web through a specified engine"""

    # Performs the search on all registered engines if 'all' keyword used
    if search_engine_name == "all":
        search_engines = search_factory.get_search_engines()
        for engine in search_engines:
            webbrowser.open(engine.get_search_url(q))
    else:
        search_engine = search_factory.get_search_engine(search_engine_name)
        webbrowser.open(search_engine.get_search_url(q))


# Create the Search Factory and Register Search Engines
search_factory = SearchFactory()
search_factory.register("google", GoogleSearch)
search_factory.register("duck", DuckDuckGoSearch)
search_factory.register("reddit", RedditSearch)

search(search_factory, sys.argv[1], sys.argv[2])
