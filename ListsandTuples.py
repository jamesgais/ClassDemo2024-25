ddlist = [
    ['bob','smith',12],
    ['peggy', 'sue',45]
        ]

print(ddlist,'\n')

ddlist.append(['sally','may',45])
print(ddlist)

print('\n')

ddlist[0].append("01/01/1990")
print(ddlist)

ddlist[0][0] = ddlist[0][0].upper()
print(ddlist)



print()
print()
#accessing memory locations.

alist = [1,2,3,4,5]

blist = alist
blist[0] = "ASDF"

print(alist)
print(blist)