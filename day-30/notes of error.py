
"""File not found error. data.text file is missing."""
'''with open ("data.text", "r") as file:
    data = file.read()
    print(data)'''

'''keyword error example'''
'''a_dict = {"key": "value"}
value = a_dict["non_existing_key"]
print(value)'''

'''index error example'''
'''fruit_list =['apple', 'banana', 'cherry']
print(fruit_list[5])
'''

'''type error example'''
'''text = 'abc'
print(text + 5)'''

'''try : something that might cause an error
except : do this if there is an error
finally : do this no matter what'''

try:
    file = open("day-30/data.text") #file not found error
    a_dict = {"key" : "value"}
    print(a_dict["sdfsdf"])
except FileNotFoundError:
    file = open("day-30/data.txt", "w")
    file.write("New file created.")
except KeyError as error_message:
    print(f"The key {error_message} does  not exist.")
else:
    content = file.read()
    print(content)

#this opens a file if it exists, if not it creates a new file.
#except should not used barely, only for specifin errors you are expecting.
###The error message should be used specifically to catch the error, if not used then
###it can hide other bugs in the code.###
finally:
    file.close()
    print("File was closed.")
#it closes the file no matter what.