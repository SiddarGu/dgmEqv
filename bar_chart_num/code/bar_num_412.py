
fig, ax = plt.subplots(figsize=(10, 6))

country = ['USA', 'UK', 'Germany', 'France']
renewable_energy_percentage = [25, 35, 45, 30]
non_renewable_energy_percentage = [75, 65, 55, 70]

ax.bar(country, renewable_energy_percentage, label="Renewable Energy(%)", bottom=non_renewable_energy_percentage)
ax.bar(country, non_renewable_energy_percentage, label="Non-Renewable Energy(%)")

ax.set_xticks(country)
ax.set_title('Distribution of Renewable and Non-Renewable Energy in four countries in 2021')
ax.legend()

for i, v in enumerate(renewable_energy_percentage):
    ax.text(i-0.15, v/2, str(v), color='white', fontweight='bold')

for i, v in enumerate(non_renewable_energy_percentage):
    ax.text(i+0.1, v/2+renewable_energy_percentage[i], str(v), color='black', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/48.png')
plt.clf()