# for loops
# 1 divisible by 5 and 7
m = int(input("Enter the upper limit number: "))

print("The Numbers Divisible by both 5 and 7 are:", end=' ')

for number in range(0, m, 5):
    if number % 5 == 0:
        if number % 7 ==0:
            print(number,end=' ')

# method 2
# for number in range(0,m,35):
#   print(number,end=' ')

# 2 sum of series
number_of_terms = int(input("\nEnter the number of terms: "))
total = 0
for i in range(1,number_of_terms+1):
    temp = '2'*i
    total += int(temp)

print(f"sum of the series is {total}")

# while loops
# 3 sum of user inputs
user_input = input("Enter a integer or q to quit: ").lower()
total = 0
while user_input != 'q':
    user_input = int(user_input)
    total += user_input
    user_input = input("Enter a integer to do addition or q to quit: ").lower()
else:
    print(f"You have selected to quit!, The sum of integers entered is: {total}")

# 4 factorial
fact_num = int(input("Enter a number to find factorial: "))
n = fact_num
factorial = 1
while fact_num > 0:
    factorial *= fact_num
    fact_num -= 1

print(f"Factorial of {n} is {factorial}")

# 5 string manipulation
st = "python language is the best programming language"
st = list(st)
main_string = ""
i = 0
while i < len(st):
    if i % 2 == 0:
        st[i] = st[i].upper()
    main_string += st[i]
    if i < len(st)-1 and (st[i] != " " and st[i+1] != " "):
        main_string += '-'
    i += 1

print(main_string)





