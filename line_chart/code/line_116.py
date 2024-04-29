
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1,1,1)

ax.plot([2020, 2021, 2022, 2023], [1000, 1500, 800, 1200], label='Crop Yield A (tons)', marker='o')
ax.plot([2020, 2021, 2022, 2023], [1200, 1000, 900, 1300], label='Crop Yield B (tons)', marker='o')
ax.plot([2020, 2021, 2022, 2023], [1500, 800, 1100, 1400], label='Crop Yield C (tons)', marker='o')
ax.plot([2020, 2021, 2022, 2023], [1100, 1300, 1200, 900], label='Crop Yield D (tons)', marker='o')

ax.set_title("Global Crop Yields from 2020-2023") 
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_xlabel("Year")
ax.set_ylabel("Crop Yield (tons)")
ax.set_xticks([2020, 2021, 2022, 2023])
ax.grid()
plt.tight_layout()
plt.savefig("line chart/png/169.png")
plt.clf()