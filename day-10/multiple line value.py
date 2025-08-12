def formated_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"result: {formatted_f_name} {formatted_l_name}"
print(formated_name(f_name = input("Enter first name: "), l_name = input("Enter last name: ")))
