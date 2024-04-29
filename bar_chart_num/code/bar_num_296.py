
import matplotlib.pyplot as plt 

# Create figure and set figsize 
fig = plt.figure(figsize=(10,7)) 

# Create subplot using add_subplot 
ax = fig.add_subplot(111) 

# Define the data 
states =['California','Texas','New York','Florida'] 
hospitals = [100,120,150,110] 
doctors = [800,900,1000,950] 
nurses = [3000,3500,3800,4000] 

# Create the bar chart 
ax.bar(states, hospitals, label='Hospitals', color='#e87722') 
ax.bar(states, doctors, label='Doctors', bottom=hospitals, color='#0080b3') 
ax.bar(states, nurses, label='Nurses', bottom=[hospitals[i] + doctors[i] for i in range(len(states))], color='#91b7d4') 

# Set the title and labels 
ax.set_xlabel("States") 
ax.set_ylabel("Number of Healthcare Services") 
ax.set_title("Healthcare services in four US states in 2021") 

# Add legend 
ax.legend() 

# Add grid 
ax.grid() 

# Add the value of each data points for every variables 
for x,y in zip(states,hospitals): 
    label = "{:.2f}".format(y) 
    ax.annotate(label, # this is the text 
                (x,y), # this is the point to label 
                textcoords="offset points", # how to position the text 
                xytext=(0,10), # distance from text to points (x,y) 
                ha='center') # horizontal alignment can be left, right or center 

for x,y in zip(states,doctors): 
    label = "{:.2f}".format(y) 
    ax.annotate(label, # this is the text 
                (x,y+hospitals[states.index(x)]), # this is the point to label 
                textcoords="offset points", # how to position the text 
                xytext=(0,10), # distance from text to points (x,y) 
                ha='center') # horizontal alignment can be left, right or center 

for x,y in zip(states,nurses): 
    label = "{:.2f}".format(y) 
    ax.annotate(label, # this is the text 
                (x,y+doctors[states.index(x)]+hospitals[states.index(x)]), # this is the point to label 
                textcoords="offset points", # how to position the text 
                xytext=(0,10), # distance from text to points (x,y) 
                ha='center') # horizontal alignment can be left, right or center 

# Auto adjust the size of the figure 
plt.tight_layout() 

# Prevent interpolation 
plt.xticks(states) 

# Save the figure 
plt.savefig('Bar Chart/png/4.png') 

# Clear the current image state 
plt.clf()