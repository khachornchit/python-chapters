import requests
import json


def load_data_to_movie_dict(url_raw_data):
    def transform_data(line):
        def validate_id(line):
            try:
                data = json.loads(line)
                return data.get('_id', {}).get('$oid')
            except (KeyError, json.JSONDecodeError):
                return None

        def validate_title(data):
            return data.get('title', '')

        def validate_year(data):
            try:
                return int(data.get('year', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        def validate_genres(data):
            return data.get('genres', '')

        def validate_tomatoes(data):
            try:
                return int(data.get('tomatoes', {}).get('viewer', {}).get('meter', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        def main():
            movie_id = validate_id(line)
            with_id = {}
            no_id = {}

            if movie_id:
                data = json.loads(line)

                no_id = {
                    "title": validate_title(data),
                    "year": validate_year(data),
                    "genres": validate_genres(data),
                    "rating": validate_tomatoes(data)
                }
                with_id[movie_id] = no_id

            return with_id, no_id

        return main()

    def main():
        response = requests.get(url_raw_data)
        lines = response.text.split("\n")
        with_ids = []
        no_ids = []

        for line in lines:
            with_id, no_id = transform_data(line)

            if with_id and no_id:
                with_ids.append(with_id)
                no_ids.append(no_id)

        return with_ids, no_ids

    return main()


def search_query(query, movies):
    def get_keywords(query):
        words = query.split()
        keywords = [' '.join(words[i:j+1]) for i in range(len(words))
                    for j in range(i, len(words))]
        return sorted(keywords, key=len, reverse=True)

    def search_by_keyword(keyword):
        return [movie for movie in movies if 'title' in movie and keyword.lower() in movie['title'].lower()]

    def main():
        keywords = get_keywords(query)
        results = []
        for keyword in keywords:
            results = search_by_keyword(keyword)
            if results:
                return keywords, results
        return keywords, results

    return main()


if __name__ == "__main__":
    url_raw_data = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    with_ids, no_ids = load_data_to_movie_dict(url_raw_data)
    keywords, results = search_query("my way", no_ids)

    print('Keywords:\n', keywords, '\n')
    print('Search results:')
    for movie in results:
        print(movie)
