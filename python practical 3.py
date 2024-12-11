#7
user=input()
lower=0
upper=0
for i in user:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print(f"Number of lower letters:{lower}")
print(f"Number of upper letters:{upper}")

#8
n=input()
s=n[::-1]
if n==s:
    print("Palindrome")
else:
    print("Not a Palindrome")
