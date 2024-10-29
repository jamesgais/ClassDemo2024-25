import os
os.system("cls")

people = ["jim","bob","sally"]

#for elements in people:
#    print(elements)
#print()

#for x in range(0,3):
#    print(people[x])

#for num in range(1,100,2):
#    print(num)


#for num in range(100,1,-2):
#    print(num)

phrase = "Hello my name is Inigyo Montoya"

#x=0
#for letter in phrase[::2]:
   
    #if x % 2 == 0:
#    print(letter.upper())

    #x+=1
#print("seperator")

#for num in range(0,len(phrase),2):
#    print(phrase[num].upper())

print(range(1,10))

menuChoice = input("make a choice from the menu")
while menuChoice not in ('1',"2","B","b"):
    print("please make a valid choice")
    menuChoice = input("make a choice from the menu")

while True:
    x= input("press enter")
    if x== "-1":
        break