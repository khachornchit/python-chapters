import requests
import json


def transformData(line):

    def validateId(line):
        try:
            data = json.loads(line)
            return data['_id']['$oid']
        except Exception as e:
            return False

    def validateTitle(data):
        try:
            return data['title']
        except Exception as e:
            return ""

    def validateYear(data):
        try:
            return int(data['year']['$numberInt'])
        except Exception as e:
            return ""

    def validateGenres(data):
        try:
            return data['genres']
        except Exception as e:
            return ""

    def validateTomatoes(data):
        try:
            return int(data['tomatoes']['viewer']['meter']['$numberInt'])

        except Exception as e:
            return ""

    def main():
        id = validateId(line)
        withId = {}
        noId = {}

        if (id != False):
            data = json.loads(line)

            withId.update({
                id: {
                    "title": validateTitle(data),
                    "year": validateYear(data),
                    "genres": validateGenres(data),
                    "rating": validateTomatoes(data)
                }
            })

            noId.update({
                "title": validateTitle(data),
                "year": validateYear(data),
                "genres": validateGenres(data),
                "rating": validateTomatoes(data)
            })

        return [withId, noId]

    return main()


def loadDataToMovieDict(urlRawData):
    f = requests.get(urlRawData)
    lines = f.text.split("\n")
    withIds = []
    noIds = []

    for line in lines:
        [withId, noId] = transformData(line)

        if (withId != {}):
            withIds.append(withId)
            noIds.append(noId)

    return [withIds, noIds]


def searchQuery(query, movies):

    def getKeywords(query):
        keywords = []
        words = query.split()
        n = len(words)

        for i in range(len(words)):
            keyword1 = ' '.join(words[i:n])
            keywords.append(keyword1)

            if (i > 0):
                keyword2 = ' '.join(words[0:n-i])
                keywords.append(keyword2)

            if (i > 0 and i < n-1):
                keyword3 = ' '.join(words[i:n-1])
                keywords.append(keyword3)
        return keywords

    def searchByKeyword(keyword):
        results = []
        for movie in movies:
            titles = movie['title'].lower()
            if (keyword in titles):
                results.append(movie)
        return results

    def main():
        keywords = getKeywords(query)
        for keyword in keywords:
            results = searchByKeyword(keyword)
            if (len(results) > 0):
                return [keywords, results]

        return [keywords, results]

    return main()


if __name__ == "__main__":
    urlRawData = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    [withIds, noIds] = loadDataToMovieDict(urlRawData)
    [keywords, results] = searchQuery("my way", noIds)

    print('Keywords: \n', keywords, '\n')

    print('Search results:')
    for movie in results:
        print(movie)
