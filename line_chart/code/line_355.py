
import matplotlib.pyplot as plt

# set font
plt.rcParams['font.family']='SimHei'

# create figure
fig=plt.figure(figsize=(10,6))

# plot line chart
plt.plot(['2015','2016','2017','2018','2019'],
         [25000,22000,21000,19000,17000],label='CO2 Emissions(tons)',linestyle='--', marker='o')
plt.plot(['2015','2016','2017','2018','2019'],
         [200,220,240,260,280],label='Water Consumption(cubic meters)',linestyle='--', marker='o')
plt.plot(['2015','2016','2017','2018','2019'],
         [500,600,580,650,700],label='Electricity Usage(kWh)',linestyle='--', marker='o')
plt.plot(['2015','2016','2017','2018','2019'],
         [400,500,460,480,500],label='Waste Produced(tons)',linestyle='--', marker='o')

# setting x,y labels
plt.ylabel('Units')
plt.xlabel('Years')

# setting x,y limits
plt.ylim(0,30000)

# add legend
plt.legend(bbox_to_anchor=(1.0,1.0))

# add title
plt.title('Environmental Impact of a Company from 2015 to 2019')

# setting grid
plt.grid()

# setting x ticks
plt.xticks(['2015','2016','2017','2018','2019'],rotation=45, wrap=True)

# auto adjust figure
plt.tight_layout()

# save figure
plt.savefig('line chart/png/306.png')

# clear current image
plt.clf()