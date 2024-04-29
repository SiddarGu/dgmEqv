
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

country = ['USA','UK','Germany','France']
recycling_rate = [30,35,32,37]
energy_usage = [20,25,22,27]

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(country,recycling_rate,bottom=energy_usage,width=0.5,label="Recycling rate")
ax.bar(country,energy_usage,width=0.5,label="Renewable energy usage")
ax.set_title("Recycling rate and renewable energy usage in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Rate (%)")
ax.legend()
ax.xaxis.set_major_locator(ticker.FixedLocator(np.arange(len(country))))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(np.array(country)))
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('bar chart/png/343.png')
plt.clf()