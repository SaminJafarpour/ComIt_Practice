# ComIt_Practice
#Write a program in Python that reads an integer from the keyboard and makes the sum of
#the next 100 numbers, showing the result on screen.
#read an integer from keyboard
x=int(input("tell me a number "))
#make the sum of next one hundred numberd
i=0
result=0
while i<=100:
    i=i+1
    result=result+x
    x=x+1
print(result)
