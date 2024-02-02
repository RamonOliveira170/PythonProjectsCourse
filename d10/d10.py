# Functions with outputs

def format_name(f_name, l_name):
    """ Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return f"You didn't provide valid inputs."
    return f"Result: {f_name} {l_name}".title()

name = format_name(input("What is your first name?: "), input("What is your last name?: "))
print(name)

