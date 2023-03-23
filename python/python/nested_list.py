if __name__ == '__main__':

    student = []
    grade = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])

    student.sort(key=lambda col: col[0])

    grade = sorted(set(grade))
    second_lowest = grade[1]

    for name, score in student:
        if score == second_lowest:
            print(name)

    # student = [[123,30], [456,20], [789,90]]
