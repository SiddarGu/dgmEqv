
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.figure(figsize=(10,6))
ax = plt.subplot()
plt.bar(["IT","HR","Finance","Marketing"],[100,50,30,80],label="Employees",width=0.5)
plt.bar(["IT","HR","Finance","Marketing"],[90,95,89,93],bottom=[100,50,30,80],label="Retention Rate",width=0.5)
plt.title("Employee retention rate by department in 2021")
plt.xlabel("Department")
plt.ylabel("Number of employees")
plt.xticks(rotation=90)
plt.legend(loc="best")
mpl.rcParams['font.family'] = 'sans-serif'
plt.tight_layout()
plt.savefig("bar chart/png/114.png")
plt.clf()