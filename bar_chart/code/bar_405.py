
import matplotlib.pyplot as plt
import numpy as np

# Setting figure size
plt.figure(figsize=(10,6))

# Data
Stadium = ["Wembley Stadium", "Emirates Stadium", "Old Trafford", "Anfield"]
Attendance = [80000, 60000, 70000, 90000]
Expected_Revenue = [1000000, 750000, 850000, 1100000]

# Plotting bar chart
ax = plt.subplot()
ax.bar(Stadium, Attendance, bottom=Expected_Revenue, color='#FF9F33', label='Attendance')  
ax.bar(Stadium, Expected_Revenue, color='#3F51B5', label='Expected Revenue')

# Adding labels, title and legend
ax.set_title('Attendance and expected revenue of four stadiums in 2021')
ax.set_xlabel('Stadiums')
ax.set_ylabel('Amount(USD)')
plt.legend()

# Preventing x-axis values from overlapping
plt.xticks(rotation=45, ha='right')

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/97.png')

# Clear the current image state 
plt.clf()