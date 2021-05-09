# common list
common_list = [1, 2, 4, 3, 6, 12, 8, 9, 5]

# 1 even and odd count
even = 0
odd = 0
for i in common_list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Count of even numbers is {even}.\nCount of odd numbers is {odd}.")

# 2 find maximum and minimum of list
common_list.sort()
print(f"Maximum number in list is {common_list[-1]}.\nMinimum number in list is {common_list[0]}.")

# 3 check if whole list is palindrome or not
user_input = input("Enter numbers separated by comas: ").split(",")
actual_list = [int(i) for i in user_input]
reversed_list = list(reversed(actual_list))

if actual_list == reversed_list:
    print(f"{actual_list} is Palindrome!")
else:
    print(f"{actual_list} is Not Palindrome!")

# 4 check if each number is palindrome in the list
user_input = input("Enter numbers separated by comas: ").split(",")
actual_list = [int(i) for i in user_input]
reverse_number = 0
for i in actual_list:
    n = i
    while n > 0:
        remainder = n % 10
        reverse_number = (reverse_number * 10) + remainder
        n = n // 10
    if i == reverse_number:
        print(reverse_number, end=' ')
        reverse_number = 0
