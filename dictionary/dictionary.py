def dictionary_remove():
    print("\n")
    print("Test function dicRemove()")
    student = {
        "name": "Emma",
        "marks": 75,
        "class": 9,
    }

    # student.pop("marks")
    # del student["marks"]
    student.popitem()
    print(student)


def dictionary_access():
    sample_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    history = sample_dict['class']['student']['marks']['history']
    print("history => ", history)


def dictionary_equal():
    dict1 = {"key1": 1, "key2": 2, "key3": 3}
    dict2 = {"key2": 2, "key1": 1}

    dict3 = dict1

    print(dict1 == dict2)
    print("dict3 => ", dict3)

    # Make equal and update
    dict1 = dict2
    dict2.update({"x": "x"})  # The dict2 updating EFFECT to dict1
    dict2.update({"xx": "xx"})  # The dict2 updating EFFECT to dict1

    dict1.update({"y": "y"})
    print("dict1 => ", dict1)
    print("dict2 => ", dict2)


if __name__ == "__main__":
    dictionary_equal()
    dictionary_remove()
    dictionary_access()

    student = {
        "name": "Emma",
        "class": 9,
        "marks": 75
    }

    print(student.get("marks"))
    print(student["marks"])
