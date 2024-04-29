
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.set_title('Academic performance of students in 5th to 10th grade')
ax.set_xlabel('Grade')
ax.set_ylabel('Score')
ax.grid(linestyle='--', linewidth=1, axis='y', alpha=0.5)

x_axis_data = [5,6,7,8,9,10]

math_data = [90,85,80,75,70,65]
ax.plot(x_axis_data,math_data, label='Math Score', linestyle='-', linewidth=3, color='#0080FF')
ax.annotate('90',xy=(5,90), fontsize=10, ha='center')
ax.annotate('85',xy=(6,85), fontsize=10, ha='center')
ax.annotate('80',xy=(7,80), fontsize=10, ha='center')
ax.annotate('75',xy=(8,75), fontsize=10, ha='center')
ax.annotate('70',xy=(9,70), fontsize=10, ha='center')
ax.annotate('65',xy=(10,65), fontsize=10, ha='center')

science_data = [85,90,85,80,75,70]
ax.plot(x_axis_data, science_data, label='Science Score', linestyle='-', linewidth=3, color='#FF0000')
ax.annotate('85',xy=(5,85), fontsize=10, ha='center')
ax.annotate('90',xy=(6,90), fontsize=10, ha='center')
ax.annotate('85',xy=(7,85), fontsize=10, ha='center')
ax.annotate('80',xy=(8,80), fontsize=10, ha='center')
ax.annotate('75',xy=(9,75), fontsize=10, ha='center')
ax.annotate('70',xy=(10,70), fontsize=10, ha='center')

english_data = [80,75,70,65,60,55]
ax.plot(x_axis_data, english_data, label='English Score', linestyle='-', linewidth=3, color='#FFFF00')
ax.annotate('80',xy=(5,80), fontsize=10, ha='center')
ax.annotate('75',xy=(6,75), fontsize=10, ha='center')
ax.annotate('70',xy=(7,70), fontsize=10, ha='center')
ax.annotate('65',xy=(8,65), fontsize=10, ha='center')
ax.annotate('60',xy=(9,60), fontsize=10, ha='center')
ax.annotate('55',xy=(10,55), fontsize=10, ha='center')

history_data = [75,80,75,70,65,60]
ax.plot(x_axis_data, history_data, label='History Score', linestyle='-', linewidth=3, color='#008000')
ax.annotate('75',xy=(5,75), fontsize=10, ha='center')
ax.annotate('80',xy=(6,80), fontsize=10, ha='center')
ax.annotate('75',xy=(7,75), fontsize=10, ha='center')
ax.annotate('70',xy=(8,70), fontsize=10, ha='center')
ax.annotate('65',xy=(9,65), fontsize=10, ha='center')
ax.annotate('60',xy=(10,60), fontsize=10, ha='center')

ax.legend(loc=2)
ax.set_xticks(x_axis_data)

plt.tight_layout()
plt.savefig('line chart/png/142.png')
plt.clf()