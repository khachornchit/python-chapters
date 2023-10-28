import requests
import json


def validateId(line):
    try:
        data = json.loads(line)
        return data['_id']['$oid']
    except Exception as e:
        return False

def validateTitle(line):
    try:
        data = json.loads(line)
        return data['title']
    except Exception as e:
        return ""

def validateYear(line):
    try:
        data = json.loads(line)
        return int(data['year']['$numberInt'])
    except Exception as e:
        return ""

def validateGenres(line):
    try:
        data = json.loads(line)
        return data['genres']
    except Exception as e:
        return ""

def validateTomatoes(line):
    try:
        data = json.loads(line)
        return int(data['tomatoes']['viewer']['meter']['$numberInt'])

    except Exception as e:
        return ""

def load_data_to_movie_dict(link):
    f = requests.get(link)
    lines = f.text.split("\n")
    all_dict = {}

    for line in lines:
        dict = {}
        id = validateId(line)

        if (id != False):
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
