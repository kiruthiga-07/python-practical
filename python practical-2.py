#5 Factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
print(f"The factorial is {factorial(num)}")

#6 create array using list iterate and check ach element odd and even and increase the count
import array as a
arr=a.array('i')
x=int(input("Enter number of elements to be inserted:"))
c_odd=0
c_even=0
for i in range(x):
    arr.append(int(input()))
for j in arr:
    if j%2==0:
        c_even+=1
    else:
        c_odd+=1
print(f"The number of odd number is: {c_odd}")
print(f"The number od even number is: {c_even}")

#
import array as a
arr=a.array('i')
x=int(input("Enter number of elements to be inserted:"))
c_odd=0
c_even=0
for i in range(x):
    arr.append(int(input()))
for j in arr:
    if j%2==0:
        c_even+=1
    else:
        c_odd+=1
print(f"The number of odd number is: {c_odd}")
print(f"The number od even number is: {c_even}")



