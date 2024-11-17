def divisible_by_ten(num):
    # Check if num is divisible by 10 using modulo operator
    if num % 10 == 0:
        return True
    else:
        return False

    print(divisible_by_ten(20))   
print(divisible_by_ten(25))  
print(divisible_by_ten(100))  
print(divisible_by_ten(37))   
print(divisible_by_ten(200))
