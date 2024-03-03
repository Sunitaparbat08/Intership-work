def find_average(numbers):
    sum = 0
    count = 0
    for number in numbers :
          try:    
              sum += number
              count +=1
          except:
              print("string is not allowed")    
    average = sum/count
    return average

numbers = [1,2,3,4,5,"6"]
average = find_average(numbers)
print(f"The average is:{average}")


def find_average(numbers):
     sum = 0
     count_numbers = 0
     for number in numbers:
          if isinstance(number,(int,float)):
               sum += number
               count_numbers +=1
          
     average = sum/count_numbers
     return average
numbers = [1,2,3,4,5,"6"]
average = find_average(numbers)
print(f"The average is:{average}")        

