
import matplotlib.pyplot as plt
import numpy as np

# Transform data into variables
data_labels = ["Product Quality","Production Efficiency","Consumer Awareness","Brand Reputation","Sales Volume"]
line_labels = ["Category"]
data = [35,16,9,20,20]

# Plot data
plt.figure(figsize=(7,7))
ax = plt.subplot()
ax.pie(data, startangle=90, counterclock=False, autopct='%1.1f%%')
circle = plt.Circle((0,0), 0.7, color='white')
ax.add_artist(circle)
plt.legend(data_labels, loc="upper right")
plt.title("Food and Beverage Industry Overview - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_84.png')
plt.clf()