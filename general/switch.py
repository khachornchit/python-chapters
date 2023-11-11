def switch(lang):
    if lang == "JavaScript":
        return "You can become a web developer."
    elif lang == "PHP":
        return "You can become a backend developer."
    elif lang == "Python":
        return "You can become a Data Scientist"
    elif lang == "Solidity":
        return "You can become a Blockchain developer."
    elif lang == "Java":
        return "You can become a mobile app developer"


def week(dd):
    switcher = {
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
        "7": "Sunday"
    }
    return switcher.get(dd, "Please type only number (1-7)")


if __name__ == '__main__':
    print(switch("JavaScript"))
    print(switch("PHP"))
    print(switch("Java"))

    day = input("type num day: ")
    day_name = week(day)
    print(day_name)
