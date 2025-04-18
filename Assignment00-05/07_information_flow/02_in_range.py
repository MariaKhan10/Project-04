def in_range(n, low, high):
 
    if n >= low and n <= high:
        return True

        
    return False

print(in_range(5, 1, 10))  # True
print(in_range(1, 1, 10))  # True
print(in_range(10, 1, 10)) # True
print(in_range(0, 1, 10))  # False
print(in_range(11, 1, 10)) # False

