def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_1 = str(num1)
    str_2 = str(num2)

    count_num1 = {}
    count_num2 = {}

    for num in str_1:
        count_num1[num] = count_num1.get(num, 0) + 1
    for num in str_2:
        count_num2[num] = count_num2.get(num, 0) + 1
    return count_num1 == count_num2