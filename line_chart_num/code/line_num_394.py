
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 6)) 
plt.plot(["0-20","21-40","41-60","61-80","81-100"], [90, 120, 150, 180, 200], color='blue', linestyle='solid', marker='o', markerfacecolor='red', markersize=8) 
plt.plot(["0-20","21-40","41-60","61-80","81-100"], [60, 65, 70, 75, 80], color='green', linestyle='dashed', marker='*', markerfacecolor='black', markersize=8) 
plt.xlabel('Age') 
plt.ylabel('Average Weight (lbs) & Average Height (inches)') 
plt.title('Average Weight and Height of People Aged 0-100') 
plt.legend(['Average Weight', 'Average Height'], loc='lower right') 
for x, y in zip(["0-20","21-40","41-60","61-80","81-100"], [90, 120, 150, 180, 200]): 
    label = "{}".format(y) 
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,10), ha='center') 
for x, y in zip(["0-20","21-40","41-60","61-80","81-100"], [60, 65, 70, 75, 80]): 
    label = "{}".format(y) 
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0,-10), ha='center') 
plt.xticks(["0-20","21-40","41-60","61-80","81-100"]) 
plt.tight_layout() 
plt.savefig('line chart/png/231.png') 
plt.clf()