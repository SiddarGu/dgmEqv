
import matplotlib.pyplot as plt

Country = ["USA", "UK", "Germany", "France"]
Manufacturing_Output = [20000, 25000, 18000, 23000]
Export_Volume = [18000, 22000, 16000, 21000]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(Country, Manufacturing_Output, bottom=Export_Volume, label='Manufacturing Output', color='blue')
ax.bar(Country, Export_Volume, label='Export Volume', color='orange')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
plt.title("Manufacturing output and export volume of four countries in 2021")
plt.xticks(rotation=45, wrap=True)
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('bar chart/png/57.png')
plt.clf()