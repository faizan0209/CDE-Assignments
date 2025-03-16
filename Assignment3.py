# # # # write a program that accept strings as a vowel
# # # # uuser = user("Enter Strings....")
# # # # vowel = 'a','e','i','o','u'
# # # # count =0
# # # # for char in uuser:
# # # #     if char in vowel:
# # # #         count +=1
# # # # print(count)
# # # # ------------------------------------------------------------------------------
# # # # take strings and change into cases
# # # users = user("Enter Strings")
# # # # for uppercase
# # # # print(users.upper())
# # # # # for uppercase
# # # # print(users.lower())
# # # # count =0
# # # # for char in users:
# # # #     count+=1
# # # # print(count)
# # # count =0
# # # char = ' '
# # # if char in users:
# # #         count+=1
# # #         print(count)
# # for replace last and first value

# # user = input("Enter Strings")

# # # Swap the first and last characters using slicing
# # if len(user) > 1:
# #     res = user[-1] + user[1:-1] + user[0]
# # else:
# #     res = user  # For strings of length 1 or less, no swap needed

# # print(res)
# # reverse a string
# user = input("Enter Strings")
# reverse = user[::-1]
# print(reverse)
# shift string right and left
s = "geeksforgeeks"

k = 1  
left_shift = s[k:] + s[:k]
right_shift = s[-k:] + s[:-k]

print("Left Shift:", left_shift)
print("Right Shift:", right_shift)