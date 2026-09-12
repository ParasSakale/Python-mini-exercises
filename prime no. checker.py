number = int(input("Enter a number: "))
is_prime = True
i = 2
while i <= number - 1:
    if number % i == 0:
        is_prime = False
        break
    i = i + 1
if is_prime:
    print("Prime")
else:
    print("Not prime")
