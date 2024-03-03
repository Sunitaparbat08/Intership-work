# Exercise 4: Incorrect Dictionary Usage
'''Error to Expect: AttributeError
 Hint: This function is supposed to update a dictionary containing student names as keys
 and a list of scores as their values. When adding a score for a student not previously in the
 records, the code does not correctly handle the assignment. How should you structure the
 value associated with each key in the dictionary, especially when introducing a new key'''



def update_record(records, name, score):
    if name in records:
        records[name].insert[0,score]
    else:
        records[name] = score
student_records = {"Alice": [88, 92], "Bob": [70, 85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)
print(student_records)        



def update_record(records, name, score):
    if name in records:
        records[name].append(score)
    else:
        records[name] = [score]

student_records = {"Alice": [88, 92], "Bob": [70, 85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)
print(student_records)
