# 1 print indexes of vowels
user_input = input("Enter a string containing vowels: ")
for i in user_input:
    if i in ['a','e','i','o','u']:
        print(user_input.index(i),end=' ')

# reverse words of a string
words = input("\nEnter words seperated by spaces: ").split()
words = words[::-1]
reversed_words = " ".join(words)
print(reversed_words)

# 3 Remove Duplicate elements without using set
user_list = input("Enter list of integers: ").split(",")
user_list = [int(i) for i in user_list]
user_list.sort()

for i in user_list:
    if user_list.count(i) > 1:
        user_list.remove(i)

print(user_list)