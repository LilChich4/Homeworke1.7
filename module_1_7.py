grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
grades_0 = (sum(grades[0])/len(grades[0]))
grades_1 = (sum(grades[1])/len(grades[1]))
grades_2 = (sum(grades[2])/len(grades[2]))
grades_3 = (sum(grades[3])/len(grades[3]))
grades_4 = (sum(grades[4])/len(grades[4]))
grades = [round(grades_0,2), round(grades_1,2), round(grades_2,2), round(grades_3,2), round(grades_4,2)]
dict_students = dict(zip(students, grades))
print(dict_students)
print(grades)
print(students)