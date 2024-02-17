chai = "Masala Tea"

print(chai)

updated = chai.replace("Masala" , "Lemon")

print(updated)

#Stripping Method for removing extra spaces.

abc = "  Devawayan  "

print(abc.strip())

#Spliting Techique in Python.
#Using this technique you can convert string to list.

name = "Dev , Divyansh , Pratyush"
print(name)
print(name.split(", "))

name_one = "Dev"
print(name_one.find("D"))

repeat_name = "Dev Dev Devawayan Dev"
print(repeat_name.count("Dev"))

#in this between the string if you add {} it is known as placeholders and it is used to add Variables.

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"

print(order.format(quantity , chai_type))

#In this the join opreation is performed to convert list into string
#in it the "" are given usually to match the gap bydefault.

chai_variety = ["Lemon" , "Masala" , "Ginger"]
print(", ".join(chai_variety))