from django.test import TestCase

from .models import News
# Create your tests here.

class NewsTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        
        # Create News entry
        test_news = News.objects.create(
            uid = 'd7ae399e-d1e3-2626-770b-34c8ae591072',
            title = '¿Cuál es el mejor material para un cubrebocas?',
            body = 'Los científicos han probado',
            url = 'https://www.nytimes.com/es/2020/04/18/espanol/material-mascarillas-virus.html',
            newspaper_uid = 'newyorktimes',
            host = 'www.nytimes.com'
        )
    
    def test_news_content(self):
        news = News.objects.get(id=1)
        uid = f'{news.uid}'
        title = f'{news.title}' 
        body = f'{news.body}'
        url = f'{news.url}'
        newspaper_uid = f'{news.newspaper_uid}'
        host = f'{news.host}'

        self.assertEqual(uid, 'd7ae399e-d1e3-2626-770b-34c8ae591072')
        self.assertEqual(title, '¿Cuál es el mejor material para un cubrebocas?')
        self.assertEqual(body, 'Los científicos han probado')
        self.assertEqual(url, 'https://www.nytimes.com/es/2020/04/18/espanol/material-mascarillas-virus.html')
        self.assertEqual(newspaper_uid, 'newyorktimes')
        self.assertEqual(host, 'www.nytimes.com')
        
