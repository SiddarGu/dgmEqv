
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plt.plot([2018,2019,2020,2021,2022],[50,45,40,35,30],label='Air Pollution Level(ppm)')
plt.plot([2018,2019,2020,2021,2022],[25,20,25,15,20],label='Water Pollution Level(ppm)')
plt.plot([2018,2019,2020,2021,2022],[65,60,55,50,45],label='Noise Pollution Level(db)')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2),  shadow=True, ncol=3,prop={'size':14})
plt.title('Pollution Levels in the US from 2018 to 2022',fontsize=14)
plt.xticks([2018,2019,2020,2021,2022])
plt.tight_layout()
plt.savefig('line chart/png/331.png')
plt.clf()