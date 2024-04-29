
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country = np.array(['USA', 'UK', 'Germany', 'France'])
Voting_Age_Population = np.array([200000000,70000000,80000000,60000000])
Voters = np.array([15000000,5000000,5500000,4000000])
Voter_Turnout = np.array([75,70,68,66])

# Set figure size
plt.figure(figsize=(20,10))

# Create subplots
ax = plt.subplot()

# Plot bar chart
ax.bar(Country, Voting_Age_Population, label='Voting Age Population (in Millions)', color='b')
ax.bar(Country, Voters, bottom=Voting_Age_Population, label='Voters (in Millions)', color='g')

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

# Set title
ax.set_title('Voter turnout in four countries in 2021')

# Set x axis
ax.set_xticks(Country)

# Annotate values
for Country, Voters in zip(Country,Voters):
    ax.annotate(str(Voters/1000000)+'M', xy=(Country, Voters), xytext=(0, 10), 
                textcoords="offset points", ha='center', va='bottom')

for Country, Voting_Age_Population in zip(Country,Voting_Age_Population):
    ax.annotate(str(Voting_Age_Population/1000000)+'M', xy=(Country, Voting_Age_Population), xytext=(0, 10), 
                textcoords="offset points", ha='center', va='bottom')

# Adjust to display labels correctly
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/396.png')

# Clear current image state
plt.clf()