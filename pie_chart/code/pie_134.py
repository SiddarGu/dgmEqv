
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

Levels = ['Primary', 'Secondary', 'Tertiary', 'Vocational', 'Other'] 
Percentage = [20,30,35,10,5] 

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.pie(Percentage, labels=Levels, autopct='%1.1f%%', startangle=90, 
       textprops={'fontsize': 14}, wedgeprops={'linewidth': 2})
plt.title('Education Levels in the US in 2023', fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/158.png')
plt.clf()