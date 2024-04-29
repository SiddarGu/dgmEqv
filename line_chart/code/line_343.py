
import matplotlib.pyplot as plt
import pandas as pd

data = [['USA', 7.2, 21.5], 
        ['UK', 3.9, 2.9], 
        ['India', 6.2, 2.9], 
        ['Canada', 7.7, 1.8]] 

df = pd.DataFrame(data, columns = ['Country', 'Unemployment Rate', 'GDP']) 

# Create figure before plotting 
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the data with the type of line chart
ax.plot(df['Country'], df['Unemployment Rate'], marker="o", label='Unemployment Rate')
ax.plot(df['Country'], df['GDP'], marker="o",label='GDP')

# Setting legend
ax.legend(loc=2)

# Setting title
ax.set_title('Economic indicators of the four major countries in 2021')

# Setting x, y labels
ax.set_xlabel('Country')
ax.set_ylabel('Rate/GDP')

# Setting xticks
ax.set_xticks(range(len(df['Country'])))
ax.set_xticklabels(df['Country'], rotation='vertical', wrap=True)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/40.png')

# Clear the current image state
plt.clf()