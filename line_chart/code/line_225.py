
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(8,6))
ax=fig.add_subplot(1,1,1)
ax.plot([2018,2019,2020,2021,2022,2023], [400,500,600,700,800,900], label='Donation A(million dollars)')
ax.plot([2018,2019,2020,2021,2022,2023], [300,400,500,600,700,800], label='Donation B(million dollars)')
ax.plot([2018,2019,2020,2021,2022,2023], [200,250,300,400,500,600], label='Donation C(million dollars)')
plt.xticks([2018,2019,2020,2021,2022,2023])
ax.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.title('Increase of donations to three nonprofit organizations from 2018 to 2023')
plt.tight_layout()
plt.savefig('line chart/png/274.png')
plt.clf()