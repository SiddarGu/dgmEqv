
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot()
x = ['2020','2021','2022','2023','2024']
y1 = [500,400,300,200,100]
y2 = [50000,40000,30000,20000,10000]
ax.plot(x, y1, marker='o', color='red', label='Donations (million dollars)')
ax.plot(x, y2, marker='o', color='blue', label='Volunteers')
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Amount', fontsize=13)
ax.set_title('Donations and Volunteers to Charity Organizations in the U.S. from 2020 to 2024', fontsize=14)
ax.set_xticks(x)
ax.grid(axis='y', alpha=0.4)
for x_,y1_,y2_ in zip(x,y1,y2):
    ax.annotate(f'{y1_}',xy=(x_,y1_), xytext=(4,4), textcoords='offset points')
    ax.annotate(f'{y2_}',xy=(x_,y2_), xytext=(4,4), textcoords='offset points')
ax.legend()
plt.tight_layout()
plt.savefig('line chart/png/39.png')
plt.clf()