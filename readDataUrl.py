import requests
import json


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


def transformDataWithId(line):
    dict = {}
    id = validateId(line)

    if (id != False):
        data = json.loads(line)
        dict.update({
            id: {
                "title": validateTitle(data),
                "year": validateYear(data),
                "genres": validateGenres(data),
                "rating": validateTomatoes(data)
            }
        })

    return dict


def transformDataNoId(line):
    dict = {}
    id = validateId(line)

    if (id != False):
        data = json.loads(line)
        dict.update({
            "title": validateTitle(data),
            "year": validateYear(data),
            "genres": validateGenres(data),
            "rating": validateTomatoes(data)
        })

    return dict


def loadDataToMovieDict(urlRawData):
    f = requests.get(urlRawData)
    lines = f.text.split("\n")
    movieWithIds = []
    movieNoIds = []

    for line in lines:
        movieWithId = transformDataWithId(line)

        if (movieWithId != {}):
            movieWithIds.append(movieWithId)

        movieNoId = transformDataNoId(line)

        if (movieNoId != {}):
            movieNoIds.append(movieNoId)

    return [movieWithIds, movieNoIds]


def searchQuery(query, movies):
    words = query.lower().split()
    n = len(words)

    stage1s = []
    stage2s = []
    stage3s = []

    # Search by keywords
    for i in range(len(words)):
        keywords = []
        keyword1 = ' '.join(words[i:n])
        keywords.append(keyword1)

        # Search movies stage1
        for movie in movies:
            titles = movie['title'].lower()
            if (keyword1 in titles):
                stage1s.append(movie)

        if (len(stage1s) > 0):
            return [keywords, stage1s]

        keywords = []
        if (i > 0):
            keyword2 = ' '.join(words[0:n-i])
            keywords.append(keyword2)

            # Search movies stage2
            for movie in movies:
                titles = movie['title'].lower()
                if (keyword2 in titles):
                    stage2s.append(movie)
            if (len(stage2s) > 0):
                return [keywords, stage2s]

        keywords = []
        if (i > 0 and i < n-1):
            keyword3 = ' '.join(words[i:n-1])
            keywords.append(keyword3)

            # Search movies stage3
            for movie in movies:
                titles = movie['title'].lower()
                if (keyword3 in titles):
                    stage3s.append(movie)

        return [keywords, stage3s]


if __name__ == "__main__":
    urlRawData = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    [movieWithIds, movieNoIds] = loadDataToMovieDict(urlRawData)
    [keywords, movies] = searchQuery("happy", movieNoIds)

    for movie in movies:
        print(movie)
