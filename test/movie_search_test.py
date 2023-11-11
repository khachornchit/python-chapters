
from ..oop.MovieDataLoader import MovieDataLoader
from ..oop.MovieSearch import MovieSearch


def test_movie_search():
    url_raw_data = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    m_loader = MovieDataLoader(url_raw_data)
    with_ids, no_ids = m_loader.load_data_to_movie_dict()

    m_search = MovieSearch(no_ids)
    keywords, results = m_search.search_query("my way")

    assert isinstance(keywords, list)
    assert isinstance(results, list)

    for movie in results:
        assert 'title' in movie
