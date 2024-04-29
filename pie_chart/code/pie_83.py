
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
ax = plt.subplot()
Education_Levels = ["Doctoral Degrees","Master's Degrees","Bachelor's Degrees","Associate's Degrees","Certificates"]
Percentage = [25,25,30,15,5]
ax.pie(Percentage, labels=Education_Levels, autopct='%1.2f%%', shadow=True, startangle=90)
plt.title("Distribution of Science and Engineering Degrees in the US in 2023")
plt.tight_layout()
plt.savefig("pie chart/png/235.png") 
plt.clf()