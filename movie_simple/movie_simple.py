import requests
import json


def load_data_to_movie_dict(url_raw_data):
    def transform_data(line):
        def validate_id(line):
            try:
                data = json.loads(line)
                return data['_id']['$oid']
            except Exception as e:
                return False

        def validate_title(data):
            try:
                return data['title']
            except Exception as e:
                return ""

        def validate_year(data):
            try:
                return int(data['year']['$numberInt'])
            except Exception as e:
                return ""

        def validate_genres(data):
            try:
                return data['genres']
            except Exception as e:
                return ""

        def validate_tomatoes(data):
            try:
                return int(data['tomatoes']['viewer']['meter']['$numberInt'])
            except Exception as e:
                return ""

        def main():
            id_value = validate_id(line)
            with_id = {}
            no_id = {}

            if id_value != False:
                data = json.loads(line)

                with_id.update({
                    id_value: {
                        "title": validate_title(data),
                        "year": validate_year(data),
                        "genres": validate_genres(data),
                        "rating": validate_tomatoes(data)
                    }
                })

                no_id.update({
                    "title": validate_title(data),
                    "year": validate_year(data),
                    "genres": validate_genres(data),
                    "rating": validate_tomatoes(data)
                })

            return [with_id, no_id]

        return main()

    def main():
        response = requests.get(url_raw_data)
        lines = response.text.split("\n")
        with_ids = []
        no_ids = []

        for line in lines:
            with_id, no_id = transform_data(line)

            if with_id != {}:
                with_ids.append(with_id)
                no_ids.append(no_id)

        return [with_ids, no_ids]

    return main()


def search_query(query, movies):
    def get_keywords(query):
        keywords = []
        words = query.split()
        n = len(words)

        for i in range(len(words)):
            keyword1 = ' '.join(words[i:n])
            keywords.append(keyword1)

            if i > 0:
                keyword2 = ' '.join(words[0:n - i])
                keywords.append(keyword2)

            if i > 0 and i < n - 1:
                keyword3 = ' '.join(words[i:n - 1])
                keywords.append(keyword3)
        return keywords

    def search_by_keyword(keyword):
        results = []
        for movie in movies:
            titles = movie['title'].lower()
            if keyword in titles:
                results.append(movie)
        return results

    def main():
        keywords = get_keywords(query)
        for keyword in keywords:
            results = search_by_keyword(keyword)
            if len(results) > 0:
                return [keywords, results]

        return [keywords, results]

    return main()


if __name__ == "__main__":
    url_raw_data = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    with_ids, no_ids = load_data_to_movie_dict(url_raw_data)
    keywords, results = search_query("my way", no_ids)

    print('Keywords:\n', keywords, '\n')

    print('Search results:')
    for movie in results:
        print(movie)
