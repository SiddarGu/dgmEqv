
import matplotlib.pyplot as plt
import numpy as np

# restructure the data
single_family_homes = [200000,400000,600000,750000,800000]
condos = [150000,300000,400000,450000,600000]
townhouses = [175000,325000,400000,475000,625000]
duplex = [225000,350000,500000,536000,650000]
multi_family_homes = [250000,400000,550000,620000,700000]

# draw and save chart
plt.figure(figsize=(10,8))

# create box plot
plt.boxplot(np.array([single_family_homes,condos,townhouses,duplex,multi_family_homes]).T,
            labels=["Single Family Homes","Condos","Townhouses","Duplex","Multi-Family Homes"],
            showmeans=True,
            patch_artist=True,
            notch=True,
            meanline=True)

# plot outliers
plt.plot(2, 900000, marker='x', color='red', zorder=3)
plt.plot(4, 750000, marker='x', color='red', zorder=3)
plt.plot(3, 1000000, marker='x', color='red', zorder=3)
plt.plot(5, 800000, marker='x', color='red', zorder=3)

# set background grid
plt.grid(linestyle='--',alpha=0.5)

# set title
plt.title("Property Price Distribution in the Housing Market (2020)", fontsize=15)

# resize the image
plt.tight_layout()

# save as png
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/16_202312251044.png')

# clear the current image
plt.clf()