
import matplotlib.pyplot as plt; 
fig = plt.figure(figsize=(12,8)) 
ax = fig.add_subplot() 
Country = ['USA', 'UK', 'Germany', 'France'] 
Enrollment_Rate = [90, 88, 85, 92] 
Graduation_Rate = [70, 68, 65, 72] 
width = 0.35  
p1 = ax.bar(Country, Enrollment_Rate, width, label='Enrollment Rate',color='#8c564b') 
p2 = ax.bar(Country, Graduation_Rate, width, bottom=Enrollment_Rate, label='Graduation Rate',color='#e377c2') 
ax.set_title('Education enrollment and graduation rates in four countries in 2021') 
ax.legend(loc='upper center') 
ax.set_xticks(Country) 
ax.set_ylabel('Rates (%)') 
for i in range(len(Country)): 
    ax.annotate(Enrollment_Rate[i], xy=(p1[i].get_x() + p1[i].get_width() / 2, p1[i].get_height() / 2),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom') 
    ax.annotate(Graduation_Rate[i], xy=(p2[i].get_x() + p2[i].get_width() / 2, p2[i].get_height() / 2 + Enrollment_Rate[i]),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom') 
plt.tight_layout()
plt.savefig("Bar Chart/png/578.png")
plt.clf()