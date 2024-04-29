
import matplotlib.pyplot as plt
plt.figure(figsize=(6,4))
sources=['Solar','Wind','Hydropower','Geothermal','Biomass','Other']
percentage=[30,25,20,10,10,5]
plt.pie(percentage,labels=sources,explode=(0.1,0,0,0,0,0),autopct='%.1f%%',shadow=True)
plt.title('Distribution of Renewable Energy Sources in the U.S., 2023')
plt.xticks(rotation=90,wrap=True)
plt.tight_layout()
plt.savefig('pie chart/png/174.png')
plt.clf()