#Take input from user and generate fibonacci series.
num = int(input("Enter number : "))
first_term = 0
second_term = 1
print("Fibonacci series : ", end = " ")
for i in range(num):
  print(first_term, end = " ")
  next_term = first_term + second_term 
  first_term = second_term 
  second_term = next_term 

