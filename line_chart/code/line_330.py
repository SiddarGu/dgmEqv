
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

# Setting the parameters of the chart
ax.set_title("Tax Rate Changes and Tax Revenues in the US from 2000-2006")
ax.set_xlabel("Year")
ax.set_ylabel("Tax Rate (%)/Tax Revenues (billion dollars)")
ax.set_xticks(np.arange(2000,2007,1))

# Plotting the data
ax.plot(np.arange(2000,2007,1), [20,25,30,35,40,45,50], label="Tax Rate (%)")
ax.plot(np.arange(2000,2007,1), [700,750,900,1000,1200,1400,1700], label="Tax Revenues (billion dollars)")
ax.legend(loc='best', fontsize='large', frameon=False)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the picture
plt.savefig('line chart/png/539.png')

# Clear the current image state
plt.clf()