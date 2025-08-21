born_in = int(input("What year were you born?\n"))
if born_in > 1946 and born_in < 1964:
    print("You are a Baby Boomer.")
elif born_in > 1965 and born_in < 1980:
    print("You are a Generation X.")
elif born_in > 1981 and born_in < 1996:
    print("You are a Millennial.")
elif born_in > 1997 and born_in < 2012:
    print("You are a Generation Z.")
elif born_in > 2013:
    print("You are Generation Alpha.")
else:
    print("You are not in any generation category.")