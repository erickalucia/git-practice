numbers = [1, 12, 2, 42, 8, 3]

def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    pass


# if __name__ == "__main__":
    largest_num = 0
    for num in numbers:
        if num > largest_num:
            largest_num += num
    return largest_num

print(max_value(numbers))

