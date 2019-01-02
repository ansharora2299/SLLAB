def reverse(string):
    string = "".join(reversed(string))
    return string
l=["No 1","Iam 2", "notcolorblind 3","myworld 4 ","isblackandwhite 5","trytokeep 6"]
for i in range(len(l)):
	if i%2==0:
		print(l[i])
for i in range(len(l)):
	if (i+1)%3==0:
		print(l[i].upper())
l2=[reverse(i) for i in l]
print(l2)
l3=[item for subitem in l for item in subitem.split() if item.isdigit()]
print(l3)
