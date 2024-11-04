import csv #csv file module
from prettytable import PrettyTable
table = PrettyTable()#class
#using csv file:
'''
with open("C:\\Users\\Suriya\\Downloads\\marksheet.csv.csv") as sp:
    reader = csv.reader(sp)
    for row in reader:
        print(row)
'''
#add by column:
'''
table.add_column("City name",
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])
print(table)
'''
#add by row:
'''
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Adelaide", 1295, 1158259, 600.5])
table.add_row(["Brisbane", 5905, 1857594, 1146.4])
table.add_row(["Darwin", 112, 120900, 1714.7])
table.add_row(["Hobart", 1357, 205556, 619.5])
table.add_row(["Sydney", 2058, 4336374, 1214.8])
table.add_row(["Melbourne", 1566, 3806092, 646.9])
table.add_row(["Perth", 5386, 1554769, 869.4])
print(table)
'''
#add row at once:
'''
table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
print(table)
'''
#sample try:
'''
table.add_column("TOPIC",["SURIYA","PREM","ANISH","SANJAY"],"c")
table.add_column("MARKS",[98,23,92,90],"c")
table.add_column("GRADE",["A+","B","A","D"],"c")
print(table)

'''
