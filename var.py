#what is Variable?
#variable name= value to assign / a container to store some value
"""
var='Badal'
print(Var) #inbuilt function
"""
#python is case sensitive

#conventions of writting code
"""
_var=1
print(_var) #only one symbol i.e _ can be used in starting or between the variable name.
"""
#In pyhton each and everything is an Object.

#SECOND LECTURE ON VARIABLES
"""
data can be :- int point, text, image, video etc.
In Python this variable refers/points to a memory location.

Syntax:-
variablename=data

for variable there are 2 attributes:- name, data
var=2:- storing the value 2 insid this container var.
Identifier:- variable name
#c, c++, java, c#

datatype variablename=data
int var=2

But int var='badal':- (error) statistically typed.
Dynamically typed.
Types of variable depends upon type of data stored in it.

variables are case sensitive.
var=22
print(var)

Rules to name variables:-
1.variable name cannot start with int and symbol except _
2.can't have white space. (simple space)
3.Not matching any keyword:- Reserved words like print
4.variable name is case sensitive
"""

#ways to define variablename:-
"""
1.camelcase: nameOfVariable
2.snakecase: name_of_variable
3.pascalcase: NameOfVariable
"""

#dynamically typed: override over variable
"""
var="badal"
print(var)
"""
#id(): it returns memory address of any particular varaibles.
"""
num=22
print(num,id(num))
"""
#22 is garbage and will be collected in latter.
#variable name is simply pointer which points towards an object.
"""
var2="badal"
print(var2,id(var2))
num="badal"
print(num,id(num))
"""

#variable is constant?
"""
g=9.8
print(type(g))
"""
#type(): return the datatype of any object
#isinstance(): return true if specified data & type of data are same
#syntax:
#isinstance(object,type)
"""
print(isinstance(g,float))
"""
#everything in python is an object
"""
print(isinstance(g,(int,float,tuple,list)))
class man:
    pass
    m1-man()
    print(isinstance(m1,man))

"""
#can we assign single value to the multiple variables.
"""
yes
a=b=c=d=30
print(a,b,c,d)
"""

#can we assign multiple value to the multiple variables.
"""
yes
a,b,c,d=1,2,3,4
print(a,b,c,d)
"""

#Types of Variavbles:
"""
1.local: can be accessed inside any particular function.
2.global: accessed anywhere in program.
"""
#DONE VARIABLES...