
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Data
data = {'Organization': ['Red Cross', 'Habitat for Humanity', 'United Way', 'Salvation Army', 'American Cancer Society', 'Boys & Girls Club', 'St. Jude Children\'s Research Hospital', 'Feeding America', 'Make-A-Wish Foundation', 'Goodwill Industries International', 'YMCA of the USA', 'World Vision', 'ASPCA', 'American Heart Association', 'American Red Cross'],
        'Donations (in thousands)': [250, 350, 500, 300, 400, 200, 450, 550, 150, 300, 350, 400, 200, 450, 500]}

#Convert to DataFrame
df = pd.DataFrame(data)

#Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

#Set figsize parameter
plt.figure(figsize=(10,6))

#Set axis labels
plt.xlabel('Organization')
plt.ylabel('Donations (in thousands)')

#Set title
plt.title('Donations to Charity and Nonprofit Organizations')

#Set background grid lines
plt.grid(linestyle='--', alpha=0.5)

#Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

#Ceil max total value up to nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value/10)*10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/1000)*1000

#Set yticks
plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

#Set xticks
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

#Plot area chart
plt.stackplot(df['Organization'], df['Donations (in thousands)'], colors=['lightblue'], alpha=0.8)

#Set legend
plt.legend(['Donations'], loc='upper left')

#Automatically resize image
plt.tight_layout()

#Save the chart
plt.savefig('output/final/area_chart/png/20231228-131755_10.png', bbox_inches='tight')

#Clear current image state
plt.clf()