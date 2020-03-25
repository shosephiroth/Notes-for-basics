# Exponet Function

# Allow us to take a certain number and raise it to a certain power

# 2 to the 3rd power:

print(2 ** 3)

print()


# Using a for loop that creates a function exponet

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


# tried printing within the function but that didn't work. Per tutorial call the function from within a print statement outside of the function
print(raise_to_power(3, 2))
print(raise_to_power(3, 4))
print(raise_to_power(4, 5))