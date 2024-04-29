
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

platform = ['Facebook', 'Twitter', 'Instagram', 'YouTube']
users = [2.7, 0.2, 1.1, 2.2]
revenue = [70, 3, 20, 15]

ax.bar(platform, users, width=0.4, label='Users (million)', 
       color='orange', align='edge', edgecolor='black')
ax.bar(platform, revenue, width=0.4, label='Revenue($million)', 
       bottom=users, color='lightblue', align='edge', edgecolor='black')

ax.set_title('Number of users and revenue generated by four major social media platforms in 2021', 
             fontsize=24, fontweight='bold', pad=20)
ax.set_xlabel('Platform', fontsize=18, fontweight='bold', labelpad=20)
ax.set_ylabel('Amount', fontsize=18, fontweight='bold', labelpad=20)

ax.set_xticks(platform)
ax.tick_params(labelsize=16)

ax.legend(fontsize=14, loc='upper right')

plt.tight_layout()
plt.savefig('bar chart/png/536.png')
plt.clf()