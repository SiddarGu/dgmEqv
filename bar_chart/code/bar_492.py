
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(['USA', 'UK', 'Germany', 'France'], [500, 400, 300, 200], width=0.2,label='Solar Energy (kWh)',bottom=[600,700,800,900])
ax.bar(['USA', 'UK', 'Germany', 'France'], [600, 700, 800, 900], width=0.2,label='Wind Energy (kWh)',bottom=[800,900,1000,1100])
ax.bar(['USA', 'UK', 'Germany', 'France'], [800, 900, 1000, 1100], width=0.2,label='Hydro Energy (kWh)')
ax.set_title('Energy usage from solar, wind and hydro sources in four countries in 2021')
ax.set_xticks(['USA', 'UK', 'Germany', 'France'])
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/230.png')
plt.clf()