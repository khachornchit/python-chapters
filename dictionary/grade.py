GRADES = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']


def input_student_id_grades():
    print("Enter student IDs and grades (e.g., 1111 A):")
    print("Enter 'q' to finish.")
    ids = []
    grades = []

    while True:
        line = input()
        if line.strip() == 'q':
            break
        lines = line.split()
        ids.append(lines[0])
        grades.append(lines[1])

    return ids, grades


def input_upgraded_ids(ids, grades) -> list:
    print("Enter the IDs of upgraded students:")
    final_grades = grades.copy()
    uids = input().split()
    for uid in uids:
        index_id = ids.index(uid)
        final_grades[index_id] = get_upgrade(grades[index_id])

    return final_grades


def get_upgrade(grade):
    index = GRADES.index(grade)
    if index - 1 >= 0:
        return GRADES[index - 1]
    return GRADES[0]


def display_output(ids, grades, final_grades) -> None:
    print('Student IDs : Grade -> Upgraded Grade')
    for i in range(len(ids)):
        print(ids[i], " : ", grades[i], " -> ", final_grades[i])


if __name__ == "__main__":
    ids, grades = input_student_id_grades()
    final_grades = input_upgraded_ids(ids, grades)
    display_output(ids, grades, final_grades)
