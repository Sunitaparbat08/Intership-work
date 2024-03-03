# Exercise 4: Incorrect Dictionary Usag
'''Error to Expect: AttributeError
 Hint: This function is supposed to update a dictionary containing student names as keys
 and a list of scores as their values. When adding a score for a student not previously in the
 records, the code does not correctly handle the assignment. How should you structure the
 value associated with each key in the dictionary, especially when introducing a new key'''

 

def update_scores(records, student_name, new_score):   
    if student_name in records:
        records[student_name].insert(0, new_score)
    else:
        records[student_name] = [new_score]

student_records = {}
update_scores(student_records, "Charlie", 91)
update_scores(student_records, 'Bob', 85)
update_scores(student_records, 'Alice', 95)
print(student_records)