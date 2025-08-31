from prettytable import PrettyTable
table = PrettyTable()
x = PrettyTable()
x.field_names = ["Pokomon Name", "Type"]
x.add_row(["Pichacu", "Electric"])
x.add_row(["Bulbasaur", "Grass/Poison"])
x.add_row(["Charmander", "Fire"])
x.align = "l"
print(x)

