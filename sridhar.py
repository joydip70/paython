import cmath
print("Find the two roots from the equation ax²+bx+c=0 \n")
a=int(input("Enter number for a: "))
b=int(input("Enter number for b: "))
c=int(input("Enter number for c: "))
y=b**2-(4*a*c)
if(y<0):
    y=abs(y)
    print(y)
res1=(-b+cmath.sqrt(y))/(2*a)
res2=(-b-cmath.sqrt(y))/(2*a)
print("ax^2+bx+c=0")
print(f"{a}x^2+{b}x+{c}=0")
print("X=",res1,"\nX=",res2)