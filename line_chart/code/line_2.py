
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 8)) 
plt.plot(['North', 'South', 'East', 'West'], [60, 65, 70, 75])
plt.xticks(['North', 'South', 'East', 'West'])
plt.title('Voter Participation in Four US Regions in the 2021 Election')
plt.xlabel('Region')
plt.ylabel('Percentage of Voters')
plt.tight_layout()
plt.savefig('line chart/png/27.png')
plt.clf()