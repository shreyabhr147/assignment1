import csv
import os

def search_no():
    n=int(input("Enter number"))
    with open(filename,"r") as file:
        for row in file:
            if n == row[1]:
                print row

def search_name():
    nam=int(input("Enter name"))
    with open(filename,"r") as file:
        for row in file:
            if nam == row[0]:
                 print row
    
    
current_dir=os.path.dirname(__file__)
filename=os.path.join(current_dir,"contact.csv")


def entry():
    #fields=['Name','Phone no.','Email','Address']
    l=[]
    name=input("Enter the name:")
    phone=input("Enter the phone no:")
    email=input("Enter the email address:")
    add=input("Enter the address:")
    l.append([name,phon,email])


    with open(fname,"a+") as f:
        csvwriter=csv.writer(f)
        #csvwriter.writerow(fields)
        csvwriter.writerows(l)

print("1)Make entry\n2)search")
a=int(input())
if a==1:
    entry()
elif a==2:
    ch=("Search by - 1.Name 2.Phone number")
    if ch==1:
        search_name()
    
    elif n==2:
        search_no()
    
