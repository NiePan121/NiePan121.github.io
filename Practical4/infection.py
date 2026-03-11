# a is 	the	initial	number	of	infected	students
# b is 	the	growth	rate	over	24	hrs
# c is the day of infection
# d is the number of IBI1 class students
a=5
b=1.4
c=0
d=91
while a<d:
      c=c+1
      a=a*b
      if a>d:
            a=d
      print("day=",c,"infection number=",a)
print("total day is:",c)
      