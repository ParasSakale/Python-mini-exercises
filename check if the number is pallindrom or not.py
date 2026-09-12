num = int(input("Enter your number : "))
pali_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if pali_num == reversed_num or (pali_num == reversed_num) < 0:
    print("Your number is a palindrome")
else:
    print("Your number is not a palindrome")

# negative palindromes coming soon!
