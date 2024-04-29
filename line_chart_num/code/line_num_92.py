

import matplotlib.pyplot as plt
import numpy as np

# Data
Year = np.array([2018,2019,2020,2021,2022])
Voter_Turnout = np.array([45, 46, 48, 50, 52])
Voter_Registration = np.array([60, 62, 65, 68, 70])
Social_Media_Ads = np.array([20000, 25000, 30000, 35000, 40000])

# Create figure
fig = plt.figure(figsize=(10,7))

# Plot Voter Turnout
plt.plot(Year, Voter_Turnout, label='Voter Turnout', color='g', marker='o', linestyle='--')

# Plot Voter Registration
plt.plot(Year, Voter_Registration, label='Voter Registration', color='b', marker='^', linestyle='-.')

# Plot Social Media Ads
plt.plot(Year, Social_Media_Ads, label='Social Media Ads', color='r', marker='s', linestyle=':')

# Annotate each data point
for i,j in zip(Year,Voter_Turnout):
    plt.annotate(str(j),xy=(i,j+0.5))

for i,j in zip(Year,Voter_Registration):
    plt.annotate(str(j),xy=(i,j+0.5))

for i,j in zip(Year,Social_Media_Ads):
    plt.annotate(str(j),xy=(i,j+500))

# Set x ticks
plt.xticks(Year, fontsize=12)

# Set legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3, fontsize=12)

# Set title and labels
plt.title('Trends in Voter Turnout, Registration, and Social Media Ad Spending in the US from 2018 to 2022', fontsize=16, fontweight='bold', wrap=True)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Numbers', fontsize=14)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/182.png', dpi=300)

# Clear current figure
plt.clf()