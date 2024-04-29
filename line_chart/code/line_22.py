
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

x = ['USA', 'Canada', 'Mexico', 'India', 'China']
y = [300, 40, 130, 1300, 1400]

plt.plot(x, y, color='teal', marker='o', linestyle='dashed', linewidth=2, markersize=8)

plt.xticks(rotation=30, wrap=True)
plt.title('Population of Five Major Countries in 2020')
plt.xlabel('Country')
plt.ylabel('Population (Millions)')

plt.tight_layout()
plt.savefig('line chart/png/161.png')

plt.clf()