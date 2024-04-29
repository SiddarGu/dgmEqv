
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

Organizations = ['Red Cross', 'UNICEF', 'World Vision', 'Salvation Army']
Donations = [50, 40, 45, 55]
Volunteers = [5000, 7000, 6000, 8000]

ax.bar(Organizations, Donations, label='Donations (million)', width=0.3)
ax.bar(Organizations, Volunteers, label='Volunteers', bottom=Donations, width=0.3)

#Change the x-axis label
ax.set_xticklabels(Organizations, rotation=45, ha='right', wrap=True)
ax.legend()
plt.title('Donations and Volunteers of Four Nonprofit Organizations in 2021')

plt.tight_layout()
# Save chart to a file
plt.savefig('bar chart/png/201.png')

# Clear the current figure
plt.clf()