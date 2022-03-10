# Dominic Pelino March 2022


# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    """Prints simple greeting"""
    print("hello_" + user_name + "!")

hello_name("USERNAME")



# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds(number):
    """Prints odd numbers 1-100"""
    while number < 100:
        number += 1
        if number % 2 == 0:
            continue
        print(number)
     
first_odds(0) 
    


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    """Returns largest number in list"""
    max_number = max(a_list)
    return max_number

number_list = [12, 470, 72, 89, 65, 49]
print(max_num_in_list(number_list))



# Question 4
# Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    """Returns if input is a leap year"""
    year = int(a_year)
    if (year % 4 == 0) and (year % 100 != 0) :
        return True
    elif (year % 400 == 0) and (year % 100 == 0) :
        return True
    else:
        return False

print(is_leap_year("1993"))



# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. 
def is_consecutive(a_list):
    """Returns if numbered list is consecutive or not."""
    largest = max(a_list)
    smallest = min(a_list)
    length = len(a_list)
    largest = int(largest)
    smallest = int(smallest)
    length = int(length)
    if largest == smallest + length - 1:
        return True
    else:
        return False

list_1 = [2, 3, 4, 5, 6, 7]
list_2 = [1, 2, 4, 5]
print(is_consecutive(list_1))
print(is_consecutive(list_2))
