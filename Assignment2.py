# # # # # # # # # # # # # # # A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount
# # # # # # # # # # # # # # user = float(input('Enter Your salary'))
# # # # # # # # # # # # # # service = int(input('Enter your serice. Hint:2,3,4'))
# # # # # # # # # # # # # # bonus = 0.05
# # # # # # # # # # # # # # inc = user*bonus
# # # # # # # # # # # # # # if service > 5:
# # # # # # # # # # # # # #     print(f'Your salary with 5% net bonus is {user+inc}')
       
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print(f'Your salary is {user}')
# # # # # # # # # # # # # # -----------------------------------------------------------------
# # # # # # # # # # # # # # Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
# # # # # # # # # # # # # age = int(input('Enter Age:'))
# # # # # # # # # # # # # if age>17:
# # # # # # # # # # # # #     print('Eligible for vote')
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print('underage for vote')
# # # # # # # # # # # # # ---------------------------------------------------------------------------
# # # # # # # # # # # # # Write a program to check whether a number entered by user is even or odd.
# # # # # # # # # # # # user = int(input('Enter the number'))
# # # # # # # # # # # # if user%2 ==0:
# # # # # # # # # # # #     print("even number")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print('odd number')
# # # # # # # # # # # # -------------------------------------------------------------
# # # # # # # # # # # # Write a program to check whether a number is divisible by 7 or not. Show Answer
# # # # # # # # # # # user = int(input('Enter the number'))
# # # # # # # # # # # if user%7==0:
# # # # # # # # # # #     print('it is divisible by 7')
# # # # # # # # # # # else:
# # # # # # # # # # #     print('not divisible by 7')
# # # # # # # # # # # ---------------------------------------------
# # # # # # # # # # # Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
# # # # # # # # # # user = int(input('Enter the number'))
# # # # # # # # # # if user%5 ==0:
# # # # # # # # # #     print('multiple of 5')
# # # # # # # # # # else:
# # # # # # # # # #     print('not multiple of 5')
# # # # # # # # # # -------------------------------------------------
# # # # # # # # # # Write a program to display the last digit of a number.
# # # # # # # # # # user = int(input('Enter the number'))
# # # # # # # # # # lastDigit = user%10
# # # # # # # # # # print(lastDigit)
# # # # # # # # # # -----------------------------------------
# # # # # # # # # # # Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
# # # # # # # # # # a = int(input('Enter the length'))
# # # # # # # # # # b = int(input('Enter the breadth'))
# # # # # # # # # # if a==b:
# # # # # # # # # #     print('its a square')
# # # # # # # # # # else:
# # # # # # # # # #     print('rectangle')
# # # # # # # # # # ---------------------------------------------
# # # # # # # # # # Take two int values from user and print greatest among them.
# # # # # # # # # a = int(input('Enter the number1'))
# # # # # # # # # b = int(input('Enter the number2'))
# # # # # # # # # c = max(a,b)
# # # # # # # # # print(f'max output is {c}')
# # # # # # # # # ----------------------------------------------------
# # # # # # # # # # A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
# # # # # # # # # quantity = int(input("Enter product quantity"))
# # # # # # # # # unit = 100
# # # # # # # # # total_price = quantity*unit
# # # # # # # # # if total_price > 1000:
# # # # # # # # #     print("congratulations you get 10% discount")
# # # # # # # # # else:
# # # # # # # # #     print(f'total = {total_price}')
# # # # # # # # # --------------------------------------------------------------
# # # # # # # # A school has following rules for grading system:
# # # # # # # # a. Below 25 - F

# # # # # # # # b. 25 to 45 - E

# # # # # # # # c. 45 to 50 - D

# # # # # # # # d. 50 to 60 - C

# # # # # # # # e. 60 to 80 - B

# # # # # # # # f. Above 80 - A

# # # # # # # # Ask user to enter marks and print the corresponding grade.
# # # # # # # marks = int(input('Enter Marks'))
# # # # # # # if marks > 80 and marks <=100:
# # # # # # #     print('A grade')
# # # # # # # elif marks > 60 and marks <=80:
# # # # # # #     print('B')
# # # # # # # elif marks >50 and marks<=60:
# # # # # # #     print('C')
# # # # # # # elif marks >45 and marks<=50:
# # # # # # #     print('D')
# # # # # # # elif marks >25 and marks<=45:
# # # # # # #     print('E')
# # # # # # # elif marks <=25 and marks >=0 :
# # # # # # #     print('F')
# # # # # # # else:
# # # # # # #     print('invalid')
# # # # # # -------------------------------------------------
# # # # # # )A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# # # # # # Take following input from user
# # # # # # Number of classes held
# # # # # # Number of classes attended.
# # # # # # And print
# # # # # # percentage of class attended
# # # # # # Is student is allowed to sit in exam or not.
# # # # # a = int(input("Enter number of classes held:"))
# # # # # b = int(input("Enter number of classes attended:"))
# # # # # c = (input("Do u have medical cause Y/N"))
# # # # # c.upper()
# # # # # percent = (b/a)*100
# # # # # percent.__round__(2)
# # # # # print(f'attendece is {percent}%')
# # # # # if percent >=75:
# # # # #     print('you are allow to sit in exam ')
# # # # # elif percent<75 and c == 'Y':
# # # # #     print('you are allowed but make sign from HOD before comming')
# # # # # else:
# # # # #     print('not allowed')
# # # # # ---------------------------------
# # # # year = int(input("Enter a year: "))

# # # # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
# # # #     print(f"{year} is a leap year.")
# # # # else:
# # # #     print(f"{year} is not a leap year.")
# # # # -------------------------------------------
# # # Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# # # if employee is female, then she will work only in urban areas.
# # # if employee is a male and age is in between 20 to 40 then he may work in anywhere
# # # if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
# # # And any other input of age should print "ERROR"
# # age = int(input("Enter Age: "))
# # gender = input("Enter gender M/F: ")
# # marital = input("Enter Marital status Y/N: ")
# # gender.upper()
# # marital.upper()
# # if gender == 'F':
# #     print('you will only work in urban areas')
# # elif gender == 'M' and age>20 and age <=40:
# #     print("you will work in anywhere")
# # elif gender == 'M' and age>40 and age <=60:
# #     print("you will work in anywhere")
# # else:
# #     print('error')
# # ---------------------------------------------
# units = int(input("Enter the number of units consumed: "))
# bill = 0

# if units <= 100:
#     bill = 0
# elif units <= 300:
#     bill = (units - 100) * 5
# else:
#     bill = (200 * 5) + (units - 300) * 10

# print(f"Total bill amount is Rs.{bill}")
# -------------------------------------------
# Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Enter age 1:"))
age2 = int(input("Enter age 2:"))
age3 = int(input("Enter age 3:"))
print(f'older one is {max(age1,age2,age3)}')