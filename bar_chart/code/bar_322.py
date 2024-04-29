

import matplotlib.pyplot as plt 
import numpy as np

# Create figure 
fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot()

# Data 
Platform = ["Facebook","Instagram","Twitter","YouTube"]
Monthly_Users = [2.5,1.5,0.8,2.3]
Monthly_Avg_Usage = [4.2,2.7,1.3,3.4]
x_pos = np.arange(len(Platform))

# Plotting 
ax.bar(x_pos, Monthly_Users, width=0.4, align="center", label="Monthly Users (Million)")
ax.bar(x_pos, Monthly_Avg_Usage, bottom=Monthly_Users, width=0.4, align="center", label="Monthly Average Usage (Hours)")

# Setting 
ax.set_xticks(x_pos)
ax.set_xticklabels(Platform, rotation=45, ha="right", wrap=True)
ax.set_ylabel("Numbers")
ax.set_title("Monthly Users and Average Usage for Social Media Platforms in 2021")
ax.legend(loc="upper left")
ax.autoscale_view()
plt.tight_layout()

# Save
plt.savefig("bar chart/png/435.png")

# Clear
plt.clf()