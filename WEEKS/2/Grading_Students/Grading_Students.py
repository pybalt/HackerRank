def gradingStudents(grades):
    result = list()
    for grade in grades:
        next_multiple = int()
        if grade < 38:
            result.append(grade)
            continue
        if grade % 5 == 0:
            result.append(grade)
            continue
        for num in range(grade, 101):
            if num % 5 == 0:
                next_multiple = num
                break
        if (next_multiple - grade) < 3:
            result.append(next_multiple)
        else:
            result.append(grade)
    return result
