#TYPES OF ARGUMENTS...
#simple Arguments
"""
def state(Punjab):
    print("Iam from"+" "+Punjab)
state("Ludhiana")
"""
#more than one Arguments
"""
def me(fname, lname):
  print("My name is" + " " + fname + " " + lname)
me("Badal","Jha")
"""
"""
def me(fname,mname,lname):
  print("My name is" + " " + fname + " " + mname + " " + lname)
me(fname="Badal",mname="Kumar",lname="Jha")
"""
#Arbitrary Arguments
"""
def lucky(*names):
        print("The lucky name is", names[2])
lucky("Jerry", "Sid", "Bunny", "Aditya")
"""
