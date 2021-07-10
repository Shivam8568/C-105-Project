import csv 
import statistics as st 
import statistics as st
with open ("Data.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata =  list(reader)
filedata.pop(0)
newdata = []
for i in range (len(filedata)):
    n_num = filedata[i][1]
    newdata.append(float(n_num))
print ("The data is : ", newdata)
standarddeviation =st.stdev(newdata)
print ("Standard Deviation is :", standarddeviation)