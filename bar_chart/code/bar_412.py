
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
country = ('USA', 'UK', 'Germany', 'France')
manufacturing_output = (200, 300, 180, 230)
export_volume = (450, 500, 400, 470)

ax.bar(country, manufacturing_output, label='Manufacturing Output(million)',
       bottom=export_volume, color='green')
ax.bar(country, export_volume, label='Export Volume(million)',
       color='blue')
ax.set_title('Manufacturing output and export volume in four countries in 2021')
ax.legend(loc='upper left')
ax.grid(True)
plt.xticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/280.png')
plt.clf()