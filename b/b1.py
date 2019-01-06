def ctof(c):
  f=(9/5)*c+32
  print(f)
  return f

def ftoc(f):
    c=(f-32)*5/9
    print(c)
    return c

n=0
st=[]
while n!=4:
    n=int(input("1 for ctof\n2 for ftoc\n3 for history\n4 for exit\n"))
    if n==1:
        c=float(input("Enter c\n"))
        st.append((c,ctof(c)))
    elif n==2:
        f=float(input("Enter f\n"))
        st.append((f,ftoc(f)))
    elif n==3:
        sort_by=int(input("Sort by from (1)\nSort by to (2)\n"))
        if sort_by==1:
            print(sorted(st,key=(lambda x:x[0])))
        elif sort_by==2:
            print(sorted(st,key=(lambda x:x[1])))
        else:
            print(st)
    elif n==4:
        exit()
    else:
        print("Invalid choice")
