import unittest

from apps.core.models import News


class NewsTests(unittest.TestCase):
    def setUp(self):
        self.news_data = {
            'title': 'Title1',
            'content': 'Content1',
        }
        self.news = News.objects.create(**self.news_data)

    def test_create_news(self):
        news = News.objects.get(id=self.news.id)
        for field, value in self.news_data.items():
            self.assertEqual(getattr(news, field), value)

    def test_update_news(self):
        new_data = {
            'title': 'Title2',
            'content': 'Content2',
        }
        #
        for field, value in new_data.items():
            setattr(self.news, field, value)
        self.news.save()
        #
        news_updated = News.objects.get(id=self.news.id)
        for field, value in new_data.items():
            self.assertEqual(getattr(news_updated, field), value)

    def test_delete_news(self):
        news_id = self.news.id
        self.news.delete()
        with self.assertRaises(News.DoesNotExist):
            News.objects.get(id=news_id)

    def tearDown(self):
        News.objects.all().delete()
