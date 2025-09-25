def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
    
print(check_odd_even(20))   
print(check_odd_even(7))    