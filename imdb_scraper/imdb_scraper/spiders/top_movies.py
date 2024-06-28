import scrapy
from scrapy_splash import SplashRequest

class ImdbTop50Spider(scrapy.Spider):
    name = 'top_movies'
    start_urls = ['https://www.imdb.com/list/ls055386972/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        for movie in response.css('li.ipc-metadata-list-summary-item'):
            yield self.parse_movie(movie)

        load_more_button = response.css('a.load-more-data')
        if load_more_button:
            next_page_url = response.urljoin(load_more_button.attrib['href'])
            yield SplashRequest(next_page_url, self.parse_more_movies, args={'wait': 2})

    def parse_more_movies(self, response):
        for movie in response.css('li.ipc-metadata-list-summary-item'):
            yield self.parse_movie(movie)

        load_more_button = response.css('a.load-more-data')
        if load_more_button:
            next_page_url = response.urljoin(load_more_button.attrib['href'])
            yield SplashRequest(next_page_url, self.parse_more_movies, args={'wait': 2})

    def parse_movie(self, movie):
        return {
            'movie_name': movie.css('h3.ipc-title__text::text').get().split(".")[1].strip(),
            'movie_year': movie.css("span.dli-title-metadata-item:nth-of-type(1)::text").get(),
            'movie_duration': movie.css("span.dli-title-metadata-item:nth-of-type(2)::text").get(),
            'movie_rating': movie.css("span.ipc-rating-star--imdb.ratingGroup--imdb-rating::attr(aria-label)").get().split(": ")[1].strip() if movie.css("span.ipc-rating-star--imdb.ratingGroup--imdb-rating::attr(aria-label)").get() else None,
            'movie_director': movie.css("span.sc-74bf520e-6.bbdzqJ:contains('Director') + span a::text").get(),
            'movie_stars': movie.css("span:contains('Stars')").xpath("following-sibling::span/a/text()").getall()
        }
