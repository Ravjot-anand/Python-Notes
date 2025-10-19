def max(num_1, num_2, num_3):
    
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3

print(max(4, 2, 8))