
import matplotlib.pyplot as plt

data = [['California', 100, 1900, 2500], ['New York', 150, 1200, 3000], ['Texas', 130, 1400, 3500],
        ['Florida', 120, 1700, 4000], ['Illinois', 140, 1500, 3700]]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.set_title('Donation and volunteerism in US states in 2021')
ax.set_xlabel('State')
ax.set_ylabel('Total Amount')
ax.plot([data[0][0], data[1][0],data[2][0],data[3][0],data[4][0]],[data[0][1], data[1][1],data[2][1],data[3][1],data[4][1]], marker='o', color='b', label='Donation Amount (million dollars)')
ax.plot([data[0][0], data[1][0],data[2][0],data[3][0],data[4][0]],[data[0][2], data[1][2],data[2][2],data[3][2],data[4][2]], marker='o', color='r', label='Total Volunteers')
ax.plot([data[0][0], data[1][0],data[2][0],data[3][0],data[4][0]],[data[0][3], data[1][3],data[2][3],data[3][3],data[4][3]], marker='o', color='g', label='Number of Charities')
for i in range(len(data)):
    ax.annotate(data[i][1], xy=(data[i][0], data[i][1]))
    ax.annotate(data[i][2], xy=(data[i][0], data[i][2]))
    ax.annotate(data[i][3], xy=(data[i][0], data[i][3]))

ax.xaxis.set_ticks([x[0] for x in data])
ax.legend(loc='best', ncol=1, frameon=False)
plt.tight_layout()
plt.savefig('line_278.png')
plt.clf()