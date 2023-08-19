def is_integer(value):
    try:
        int(value)
        return True
    except:
        return False


value = "2023"

if is_integer(value):
    print(int(value) + 543)
else:
    print(value + " is not integer!")
