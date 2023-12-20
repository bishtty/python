# # if divisible by 3 print fizz
# # if divisible by 5 print buzz
# # if divisible by 3 & 5 print fizzbuzz
# # print no. from 1-100

for i in range(1,100+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%7==0:
        print("bazz")
    else:
        print(i)

# the program below will print the output in single line in list form:  
# print(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, 100 + 1)])
