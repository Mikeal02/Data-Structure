# # function
# def total_sum(*nums):
#     if len(nums)==0:
#         return None
#     sum=0
#     for i in nums:
#         sum+=i

#     return sum

# answer=total_sum(1,2,3,4,5,6,7,8)
# print(answer)

# def customer_info(title,*info, **info2):
#     print(f"Title : {title}")
    
#     print(f"Name is {info[0]}")
#     print(f"age is {info[1]}")

#     print(f"Weight is {info2['weight']}")
#     print(f"Salary is {info2['salary']}")
#     print(f"height is {info2['height']}")

# customer_info("Customer Info", "tushar", 34, salary=23000, weight=55, height=170)

# def say_my_name_loud(func):
#     def say():
#         return func().upper()
#     return say

# @say_my_name_loud
# def say_my_name():
#     return "Tushar Rohilla"

# print(say_my_name())

import functools


def changecase(n):
    def changecase(func):
        @functools.wraps(func)

        def wrapper():
            if n==1:
                return func().split(" ")
            else:
                return func().encode()
        return wrapper
    return changecase



@changecase(2)
def my_name():
    return "tushar rohilla"
print(my_name())
print(my_name.__name__)
