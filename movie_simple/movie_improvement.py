import requests
import json


def loadDataToMovieDict(urlRawData):
    def transformData(line):
        def validateId(line):
            try:
                data = json.loads(line)
                return data.get('_id', {}).get('$oid')
            except (KeyError, json.JSONDecodeError):
                return None

        def validateTitle(data):
            return data.get('title', '')

        def validateYear(data):
            try:
                return int(data.get('year', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        def validateGenres(data):
            return data.get('genres', '')

        def validateTomatoes(data):
            try:
                return int(data.get('tomatoes', {}).get('viewer', {}).get('meter', {}).get('$numberInt', ''))
            except (KeyError, ValueError):
                return None

        def main():
            id = validateId(line)
            withId = {}
            noId = {}

            if id:
                data = json.loads(line)

                noId = {
                    "title": validateTitle(data),
                    "year": validateYear(data),
                    "genres": validateGenres(data),
                    "rating": validateTomatoes(data)
                }
                withId[id] = noId

            return withId, noId

        return main()

    def main():
        f = requests.get(urlRawData)
        lines = f.text.split("\n")
        withIds = []
        noIds = []

        for line in lines:
            withId, noId = transformData(line)

            if withId and noId:
                withIds.append(withId)
                noIds.append(noId)

        return withIds, noIds

    return main()


def searchQuery(query, movies):
    def getKeywords(query):
        words = query.split()
        keywords = [' '.join(words[i:j+1]) for i in range(len(words))
                    for j in range(i, len(words))]
        return sorted(keywords, key=len, reverse=True)

    def searchByKeyword(keyword):
        return [movie for movie in movies if 'title' in movie and keyword.lower() in movie['title'].lower()]

    def main():
        keywords = getKeywords(query)
        results = []
        for keyword in keywords:
            results = searchByKeyword(keyword)
            if results:
                return keywords, results
        return keywords, results

    return main()


if __name__ == "__main__":
    urlRawData = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    withIds, noIds = loadDataToMovieDict(urlRawData)
    keywords, results = searchQuery("my way", noIds)

    print('Keywords:\n', keywords, '\n')
    print('Search results:')
    for movie in results:
        print(movie)
