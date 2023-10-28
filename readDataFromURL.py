import requests
import json


def validateId(line):
    try:
        data = json.loads(line)
        if ('_id' in line):
            return data['_id']['$oid']
    except Exception as e:
        return ""

    return ""


def validateTitle(line):
    try:
        data = json.loads(line)
        if ('title' in line):
            return data['title']
    except Exception as e:
        return ""

    return ""


def validateYear(line):
    try:
        data = json.loads(line)
        if ('year' in line):
            return int(data['year']['$numberInt'])
    except Exception as e:
        return ""

    return ""


def validateGenres(line):
    try:
        data = json.loads(line)
        if ('genres' in line):
            return data['genres']
    except Exception as e:
        return ""

    return ""


def validateTomatoes(line):
    try:
        data = json.loads(line)
        if ('tomatoes' in line
            and 'viewer' in line
            and 'meter' in line
                and '$numberInt' in line):
            return int(data['tomatoes']['viewer']['meter']['$numberInt'])

    except Exception as e:
        return ""

    return ""


def load_data_to_movie_dict(link):
    f = requests.get(link)
    lines = f.text.split("\n")
    all_dict = {}

    for line in lines:
        dict = {}
        id = validateId(line)

        if (id != ""):
            dict.update({
                id: {
                    "title": validateTitle(line),
                    "year": validateYear(line),
                    "genres": validateGenres(line),
                    "rating": validateTomatoes(line)
                }
            })

        if (dict != {}):
            all_dict.update(dict)

    return all_dict


if __name__ == "__main__":
    link = 'https://raw.githubusercontent.com/sothornin/file/main/movies_2010_2013.json'
    result = load_data_to_movie_dict(link)
    print(result)
