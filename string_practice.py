# Print the first letter of the following string

school = "McHenry County College"




# print the length of the school string
print(len(school))


# Use a while loop to print each character (including spaces) in the school variable
index = 0
while index < len(school):
    letter = school[index]
    print letter
    index += 1




# Slice school into three variables, print the variables
a = "McHenry County College"
print a[]
print a[]
print a[]


# use a while statement to search for the letter "e" in the contents of the school variable
# print the index of every location with the letter "e"
# rembember, you should not use the same variable twice in the same program
# so if you used the variable index, use something else
e = 0
while e < len(school):
    if school[e] == 'e':
        print e
    e += 1



# Write the code to count the number of times the letter y appears in the school variable
# print the total
count = 0
for letter in school:
    if letter == 'y':
        count += 1
print count



# create a variable named college and store the upper case version of the variable school in it
college = school.upper()
print(college)

# check to see if Count is in the school variable
check = school.find('count')
print check
# check to see if count is in the school variable
check = school.find('count')
print check
