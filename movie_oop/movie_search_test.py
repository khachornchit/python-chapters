
from MovieDataLoader import MovieDataLoader
from MovieSearch import MovieSearch


def test_movie_search():
    url_raw_data = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    movie_loader = MovieDataLoader(url_raw_data)
    with_ids, no_ids = movie_loader.load_data_to_movie_dict()

    movie_search = MovieSearch(no_ids)
    keywords, results = movie_search.search_query("my way")

    assert isinstance(keywords, list)
    assert isinstance(results, list)

    for movie in results:
        assert 'title' in movie
