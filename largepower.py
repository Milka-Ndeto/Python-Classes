def large_power(base, exponent):
    # Calculate the power
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False
print(large_power(1000, 3)) 
print(large_power(50, 4))   
print(large_power(2, 1))  
