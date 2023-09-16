GRADES = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']


def inputStudentIdGrades():
    print("Key student ids and grade such as 1111 A:")
    print("Key q to finish.")
    ids = []
    grades = []

    while (True):
        line = input()
        if (line.strip() == 'q'):
            break
        lines = line.split()
        ids.append(lines[0])
        grades.append(lines[1])

    return ids, grades


def inputUIDs(ids, grades) -> None:
    print("Key ids of the upgraded students:")
    finalGrades = grades.copy()
    uids = input().split()
    for index in range(len(uids)):
        index2 = ids.index(uids[index])
        grade = grades[index2]
        finalGrades[index2] = getUpgrade(grade)

    return finalGrades


def getUpgrade(grade):
    index = GRADES.index(grade)
    if (index-1 >= 0):
        return GRADES[index-1]

    return GRADES[0]


def displayOutput(ids, grades, finalGrades) -> None:
    print('Student Ids : Grade -> Upgrade')
    for i in range(len(ids)):
        print(ids[i], " : ", grades[i], " -> ", finalGrades[i])


if __name__ == "__main__":
    ids, grades = inputStudentIdGrades()
    finalGrades = inputUIDs(ids, grades)
    displayOutput(ids, grades, finalGrades)
