print(format(1.2341234567892345678,'08'))
print(format(1.234,'>8.3'))
print(format(1234567,'^15,'))
print(format(.12,'.1%'))
print(format(1.234,'f'))
print(format(1234567890,'.2e'))
print(format(5,'08b'))

name = "jim"

print(format(name,"<10"))
print(format(name,">10"))
print(format(name,"^10"))

name= 'Inigio Montoya'
print("Hello my name is" , format(name,"^20"), "Prepare to die")
print(f"Hello my name is {name:^20} Prepare to die")

name = input("Enter your first name")
age = input(f"Hello {name} please enter your age.")
print(age)