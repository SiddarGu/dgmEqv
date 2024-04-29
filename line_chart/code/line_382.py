
import matplotlib.pyplot as plt 
import numpy as np 

# Create figure 
fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot(1, 1, 1) 

# Set up data
year = [2017, 2018, 2019, 2020, 2021] 
TicketsSold = [50, 60, 70, 80, 90] 
GamesPlayed = [100, 110, 120, 130, 140] 
GrossProfits = [2, 3, 4, 5, 6] 

# Plotting the line chart
ax.plot(year, TicketsSold, color="purple", label='Tickets Sold', marker="o") 
ax.plot(year, GamesPlayed, color="blue", label='Games Played', marker="o") 
ax.plot(year, GrossProfits, color="green", label='Gross Profits', marker="o") 

# Setting up x-axis
ax.set_xlabel("Year")

# Setting up y-axis
ax.set_ylabel("Value") 

# Setting up xticks
ax.set_xticks(year)

# Setting up legend
ax.legend(loc="upper left") 

# Setting title
ax.set_title("Trends of Ticket Sales and Games Played in the Entertainment Industry from 2017 to 2021") 

# Automatically resize the image by tight_layout
plt.tight_layout() 

# Save image
plt.savefig("line chart/png/511.png") 

# Clear current image state
plt.cla()