
import matplotlib.pyplot as plt 
import numpy as np 

fig = plt.figure(figsize=(8, 6)) 
ax = fig.add_subplot(111) 

data=np.array([[2020, 500, 400],  
               [2021, 550, 420],  
               [2022, 600, 440],  
               [2023, 650, 460]])

year, revenue, expense = data.T 

ax.bar(year, revenue, bottom=expense, width=0.5, label="Revenue", color='#CDDC39') 
ax.bar(year, expense, width=0.5, label="Expense", color='#F44336')

ax.set_xlabel('Year') 
ax.set_ylabel('Amount (million)') 
ax.set_title('Revenue and Expense for the years 2020 to 2023') 

ax.legend(loc="upper right") 
ax.annotate('{}M'.format(revenue[0]), xy=(2020, 500), xytext=(2020, 500+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(expense[0]), xy=(2020, 400), xytext=(2020, 400+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(revenue[1]), xy=(2021, 550), xytext=(2021, 550+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(expense[1]), xy=(2021, 420), xytext=(2021, 420+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(revenue[2]), xy=(2022, 600), xytext=(2022, 600+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(expense[2]), xy=(2022, 440), xytext=(2022, 440+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(revenue[3]), xy=(2023, 650), xytext=(2023, 650+20),
            arrowprops=dict(facecolor='black')) 
ax.annotate('{}M'.format(expense[3]), xy=(2023, 460), xytext=(2023, 460+20),
            arrowprops=dict(facecolor='black')) 

plt.xticks(year) 
plt.tight_layout() 
plt.savefig('Bar Chart/png/323.png') 
plt.clf()