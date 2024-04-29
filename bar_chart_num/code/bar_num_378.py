
import matplotlib.pyplot as plt

data = [[250,50,120], [50,20,30], [120,30,50], [90,15,40]]
country = ["USA", "UK", "Germany", "France"]
fb_users = [item[0] for item in data]
tw_users = [item[1] for item in data]
ig_users = [item[2] for item in data]
x_pos = [i for i, _ in enumerate(country)]

fig, ax = plt.subplots(figsize=(10,7))
ax.bar(x_pos, fb_users, width=0.8, color='#EE3224', label='Facebook Users')
ax.bar(x_pos, tw_users, width=0.8, color='#F78F1E', bottom=fb_users, label='Twitter Users')
ax.bar(x_pos, ig_users, width=0.8, color='#FFC222', bottom=[i+j for i,j in zip(fb_users, tw_users)], label='Instagram Users')

ax.set_ylabel('Users (million)')
ax.set_title('Number of Social Media users in four countries in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(country)
ax.legend()

for i, v in enumerate(fb_users):
    ax.text(i-.2, v/2, str(v), fontsize=12, color='white')
for i, v in enumerate(tw_users):
    ax.text(i, fb_users[i] + v/2, str(v), fontsize=12, color='white')
for i, v in enumerate(ig_users):
    ax.text(i+.2, fb_users[i] + tw_users[i] + v/2, str(v), fontsize=12, color='white')

plt.tight_layout()
plt.savefig('Bar Chart/png/130.png')
plt.clf()