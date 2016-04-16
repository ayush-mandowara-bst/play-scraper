# -*- coding: utf-8 -*-

import unittest

from play_scraper.scraper import PlayScraper


class TestScraperMethods(unittest.TestCase):
    def setUp(self):
        self.s = PlayScraper()

    def test_fetching_app_and_details(self):
        app = self.s.details('com.android.chrome')

        assert len(app.keys()) == 31
        assert app['app_id'] == 'com.android.chrome'

    def test_fetching_collection_non_detailed(self):
        apps = self.s.collection('NEW_FREE', results=2)
        page2 = self.s.collection('NEW_FREE', page=1)

        assert len(apps) == 2
        assert len(apps[0].keys()) == 9
        assert not apps == page2

    def test_fetching_collection_detailed(self):
        apps = self.s.collection('TOP_FREE', results=1, detailed=True)

        assert len(apps) == 1
        assert len(apps[0].keys()) == 31

    def test_fetching_developer(self):
        apps = self.s.developer('Disney', results=5)

        assert len(apps) == 5
        assert len(apps[0].keys()) == 9
        assert apps[0]


if __name__ == '__main__':
    unittest.main()
