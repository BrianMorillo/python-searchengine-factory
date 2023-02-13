"""
Example of the Factory Pattern with known search engines
Author: Brian Morillo
Date: 10/29/2022
"""


class SearchFactory:
    """Factory of search engines."""

    def __init__(self):
        """Init the search engine dictionary."""
        self._search_engines = {}

    def register(self, site, search_class):
        """Register a new search service."""
        self._search_engines[site] = search_class

    def get_search_engine(self, site):
        """
        Create object, based on the service name.
        This is the factory method.
        Depending on the site parameter,
        a different object is created and returned.
        """
        if site in self._search_engines:
            service = self._search_engines[site]

            # Here, we instantiante the object
            return service()

    def get_search_engines(self):
        """Returns all stored search engines in a list of objects"""
        search_engines = []
        for engine in self._search_engines:
            search_engines.append(self.get_search_engine(engine))
        return search_engines
