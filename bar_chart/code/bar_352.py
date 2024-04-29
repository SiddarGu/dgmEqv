
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.bar('Employee', 'Salary', data=[('John', 5000), ('Michael',4500), ('Alice', 4000), ('David',3800)], width=0.6,label='Salary')
ax.bar('Employee', 'Bonus(%)', data=[('John', 10), ('Michael',15), ('Alice', 12), ('David',11)], bottom=[5000,4500,4000,3800],width=0.6,label='Bonus(%)')
ax.bar('Employee', 'Leave days', data=[('John', 20), ('Michael',18), ('Alice', 25), ('David',22)], bottom=[5000,4500,4000,3800],width=0.6,label='Leave days')
plt.title('Employee salaries, bonuses, and leave days in 2021', fontsize=14, fontweight='bold')
ax.set_xticks(range(4))
ax.set_xticklabels(['John', 'Michael', 'Alice', 'David'], rotation=45, fontsize=12)
ax.legend(fontsize=12)
plt.tight_layout()
plt.savefig('bar chart/png/147.png',dpi=200)
plt.clf()