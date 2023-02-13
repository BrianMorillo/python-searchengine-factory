"""
Module composed of search engine classes
Author: Brian Morillo
Date: 10/29/2022
"""
from abc import ABC, abstractmethod


class SearchEngine(ABC):
    """The Search Engine Base Class."""

    @abstractmethod
    def get_search_url(self, q):
        """Search the service with the specified q parameter."""
        pass


class RedditSearch(SearchEngine):
    """Concrete RedditSearch."""

    def get_search_url(self, q):
        """Search Reddit with the specified q parameter."""
        return f"https://www.reddit.com/search/?q={q}"


class DuckDuckGoSearch(SearchEngine):
    """Concrete DuckDuckGoSearch."""

    def get_search_url(self, q):
        """Search DuckDuckGoSearch with the specified q parameter."""
        return f"https://duckduckgo.com/?q={q}"


class GoogleSearch(SearchEngine):
    """Concrete GoogleSearch."""

    def get_search_url(self, q):
        """Search Google with the specified q parameter."""
        return f"https://www.google.com/search?q={q}"
