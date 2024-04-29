
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
# data
degrees = ['Bachelor\'s Degrees', 'Master\'s Degrees','Associate Degrees', 'Specialist Degrees','Doctorate Degrees']
percentage = [45, 25, 15, 10, 5]
# plot
ax.pie(percentage, labels=degrees, 
        autopct='%1.1f%%', textprops={'fontsize': 12})
# xy-axis
ax.set_title('Distribution of Degrees Awarded in the United States in 2023') 
# Legend
ax.legend(degrees, bbox_to_anchor=(1, 1), loc='upper right', fontsize=12)
# adjust the pie
plt.xticks(rotation=45)
plt.tight_layout()
# save fig
plt.savefig('pie chart/png/393.png')
# clear fig
plt.clf()