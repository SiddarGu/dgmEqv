
import matplotlib.pyplot as plt 
import numpy as np 

# Create figure 
fig = plt.figure(figsize=(15,7)) 

# Plot data 
data = [[25,100,4.5], [30,110,4.7], [20,90,4.8], [15,80,4.9]] 
quarters = ["Q1 2020", "Q2 2020", "Q3 2020", "Q4 2020"] 

# Create 3 subplots 
ax1 = plt.subplot2grid((2,2),(0,0)) 
ax2 = plt.subplot2grid((2,2),(0,1)) 
ax3 = plt.subplot2grid((2,2),(1,0), colspan=2) 

# Plot data for each quarter 
ax1.plot(data[0], label=quarters[0]) 
ax1.plot(data[1], label=quarters[1]) 
ax1.plot(data[2], label=quarters[2]) 
ax1.plot(data[3], label=quarters[3]) 

# Set titles 
ax1.set_title("Employee Leave (days)") 
ax2.set_title("Employee Overtime (hours)") 
ax3.set_title("Employee Satisfaction Score") 

# Set labels 
ax1.set_xlabel("Quarter") 
ax1.set_ylabel("Employee Leave (days)") 
ax2.set_xlabel("Quarter") 
ax2.set_ylabel("Employee Overtime (hours)") 
ax3.set_xlabel("Quarter") 
ax3.set_ylabel("Employee Satisfaction Score") 

# Set xticks 
ax1.set_xticks(np.arange(len(quarters))) 
ax2.set_xticks(np.arange(len(quarters))) 
ax3.set_xticks(np.arange(len(quarters))) 

# Set xticklabels 
ax1.set_xticklabels(quarters) 
ax2.set_xticklabels(quarters) 
ax3.set_xticklabels(quarters, rotation=45, wrap=True) 

# Add legend 
ax1.legend(loc="best")

# Adjust figure layout 
plt.tight_layout() 

# Save figure 
plt.savefig("line chart/png/347.png") 

# Clear the current image state 
plt.clf()