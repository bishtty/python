# printing multiple of 3
for i in range(3,30+1):
    if i%3==0:
        print(i)

# list comprehension to generate cube of first 10 number
print([i**3 for i in range(1,10+1)])
