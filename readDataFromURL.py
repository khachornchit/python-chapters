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


def transformData(line):
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


def loadDataToMovieDict(urlRawData):
    f = requests.get(urlRawData)
    lines = f.text.split("\n")
    data = {}

    for line in lines:
        dict = transformData(line)

        if (dict != {}):
            data.update(dict)

    return data


if __name__ == "__main__":
    urlRawData = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    result = loadDataToMovieDict(urlRawData)
    print(result)
