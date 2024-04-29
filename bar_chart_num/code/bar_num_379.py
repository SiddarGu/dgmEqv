

import matplotlib.pyplot as plt 
import numpy as np 

# set the figure size 
plt.figure(figsize=(12, 6)) 

# data 
region = ["North", "South", "East", "West"] 
voting_age_population = [100000, 140000, 120000, 130000] 
registered_voters = [70000, 85000, 75000, 90000] 


# create bars 
bar_width = 0.25 
bar1 = plt.bar(region, voting_age_population, width=bar_width, 
                label="Voting Age Population", color="blue") 
bar2 = plt.bar(region, registered_voters, width=bar_width, 
                bottom=voting_age_population, label="Registered Voters", 
                color="red") 

# labels and title 
plt.xlabel("\nRegion", fontsize=14) 
plt.ylabel("Population Count\n", fontsize=14) 
plt.title("Voter turnout in four regions in 2021\n", fontsize=14) 

# set axis 
plt.xticks(np.arange(len(region)), region) 
plt.yticks(np.arange(0, 200001, 50000)) 

# add grids  
plt.grid(True, axis="y", alpha=0.3) 

# add legend 
plt.legend(bbox_to_anchor=(1.03, 1.0), loc="upper left") 


# optimize layout 
plt.tight_layout() 

# save figure 
plt.savefig("bar_379.png") 

# clear current figure 
plt.clf()