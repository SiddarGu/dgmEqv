
import matplotlib.pyplot as plt
import pandas as pd

data = {'Month':['January','February','March','April','May','June','July'],
        'CO2 Emission(Kg)':[1000,900,800,700,800,900,1000],
        'Carbon Monoxide(PPM)':[800,750,700,650,700,750,800],
        'Nitrous Oxide(PPM)':[500,450,400,350,400,450,500],
        'Sulfur Dioxide(PPM)':[100,90,80,70,80,90,100]}

df = pd.DataFrame(data)

x = df['Month']
CO2 = df['CO2 Emission(Kg)']
Carbon = df['Carbon Monoxide(PPM)']
Nitrous = df['Nitrous Oxide(PPM)']
Sulfur = df['Sulfur Dioxide(PPM)']

plt.figure(figsize=(12,6))
ax = plt.subplot(1,1,1)

# plot the data
ax.plot(x, CO2, label='CO2 Emission(Kg)', color='red', marker='o', linestyle='--')
ax.plot(x, Carbon, label='Carbon Monoxide(PPM)', color='green', marker='v', linestyle='-.')
ax.plot(x, Nitrous, label='Nitrous Oxide(PPM)', color='blue', marker='s', linestyle=':')
ax.plot(x, Sulfur, label='Sulfur Dioxide(PPM)', color='orange', marker='*', linestyle='-')

# set label
ax.set_xlabel('Month')
ax.set_ylabel('Pollutant Emission')
ax.set_title('Pollutant Emission Trends in Los Angeles from January to July, 2021')

# set the position of legend
ax.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# set the xticks
plt.xticks(x, rotation=45)

# add annotation
for i,j in zip(x,CO2):
    ax.annotate(str(j),xy=(i,j), xytext=(0,5), textcoords='offset points')
for i,j in zip(x,Carbon):
    ax.annotate(str(j),xy=(i,j), xytext=(0,5), textcoords='offset points')
for i,j in zip(x,Nitrous):
    ax.annotate(str(j),xy=(i,j), xytext=(0,5), textcoords='offset points')
for i,j in zip(x,Sulfur):
    ax.annotate(str(j),xy=(i,j), xytext=(0,5), textcoords='offset points')

# automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/503.png')

# clear the current image state
plt.clf()