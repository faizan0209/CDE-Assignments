# # # # # # # Q1 write a program that accept strings as a vowel
# # # # # # # uu ser = user("Enter Strings....")
# # # # # # # vowel = 'a','e','i','o','u'
# # # # # # # count =0
# # # # # # # for char in uuser:
# # # # # # #     if char in vowel:
# # # # # # #         count +=1
# # # # # # # print(count)
# # # # # # # ------------------------------------------------------------------------------
# # # # # # # take strings and change into cases
# # # # # # users = user("Enter Strings")
# # # # # # # for uppercase
# # # # # # # print(users.upper())
# # # # # # # # for uppercase
# # # # # # # print(users.lower())
# # # # # # # count =0
# # # # # # # for char in users:
# # # # # # #     count+=1
# # # # # # # print(count)
# # # # # # count =0
# # # # # # char = ' '
# # # # # # if char in users:
# # # # # #         count+=1
# # # # # #         print(count)
# # # # # for replace last and first value

# # # # # user = input("Enter Strings")

# # # # # # Swap the first and last characters using slicing
# # # # # if len(user) > 1:
# # # # #     res = user[-1] + user[1:-1] + user[0]
# # # # # else:
# # # # #     res = user  # For strings of length 1 or less, no swap needed

# # # # # print(res)
# # # # # reverse a string
# # # # user = input("Enter Strings")
# # # # reverse = user[::-1]
# # # # print(reverse)
# # # # shift string right and left
# # # s = "geeksforgeeks"

# # # k = 1  
# # # left_shift = s[k:] + s[:k]
# # # right_shift = s[-k:] + s[:-k]

# # # print("Left Shift:", left_shift)
# # # print("Right Shift:", right_shift)
# # -------------------------------------------------------------------------
# # s = input("Enter a string: ")
# # n = len(s)
# # is_palindrome = True

# # for i in range(n // 2):
# #     if s[i] != s[n - i - 1]:
# #         is_palindrome = False
# #         

# # if is_palindrome:
# #     print("The string is a palindrome.")
# # else:
# #     print("The string is not a palindrome.")
# # ------------------------------------------------------
# word = "shift"

# for i in range(len(word)):
#     print(word[i:] + word[:i])
# password valdation
password = input("Enter Password!")
if len(password) <8:
        print("passowrd atleast 8 characters long")
        
elif not any (char.isdigit() for char in password):
        print("Must contain number")
        
elif not any (char.isalpha() for char in password):
        print("must contain letter")
        
elif  (char.upper()for char in password):
        print("must contain uppercase")
        
elif   (char.lower() for char in password):
        print("must contain lower")
        
else:
        print("Password Created Sucessfull..")
        
