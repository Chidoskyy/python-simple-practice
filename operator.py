# Arithumetic
y = 10
x = 4
total = x + y
print("The total numbe is {}" .format(total))

# subtraction

sub = x - y 
print(f"The total sub number is {sub}")

# multiplcation
multi = y * x

print("Multiply x and y and get", multi)

#modular operator returns the remainder value
modu = y/x
print(f"the remainder is {modu}")


#exponent operator raises it to the power
expo = y**x
print(f"the exponent is {expo}")



#Comparism operator
a = 60
b = 45
out = a < b
print(out)

a = 60
b = 45
out = a > b
print(out)

a = 60
b = 45
out = a == b
print(out)

a = 60
b = 45
out = a != b
print(out)



#Assighment Operators exanple =, +=, -=, 
c = 0
d = 5
c+=d
print(c)

c = 0
d = 5
c-=d
print(c)



#Logical Operators

# and all the operators must be true to return true
# or this returns true of any of the operations are true

q = 40
f = 60

d =2
t =3

out = (d < t) or (q > f)
print(out)

out = (d > t) or (q < f)
print(out)

out = (d < t) and (q > f)
print(out)

out = (d < t) and (q < f)
print(out)

out = not(d < t)
print(out)



#Menbership operators

skills = ("devops", "AWS", "jenkins", "Python", "Ansible", "Developement", "Java", "node Js", ".net")
check = "devops" in "skills"
print(check)

check = "devops" not in "skills"
print(check)