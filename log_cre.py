import os
import csv
from datetime import datetime
    
current_dir=os.path.dirname(__file__)
filename="log.csv"

mes=input("Enter a message: ")
typ=input("Enter the type of message: ")
now=datetime.now()
c_r=now.strftime("%H:%M:%S")
l=[]
l.append([mes,typ,c_r])
with open(os.path.join(current_dir,filename),'a') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerows(l)

