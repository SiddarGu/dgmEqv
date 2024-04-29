
import matplotlib.pyplot as plt
import pandas as pd

# Set figure size and create a figure
plt.figure(figsize=(7,7))

# Create a dataframe
df = pd.DataFrame({'Levels':['Primary','Secondary','Tertiary','Vocational','Non-Formal'],
                   'Percentage':[35,30,20,10,5]})

# Plot pie chart
plt.pie(df['Percentage'],
        labels=df['Levels'],
        autopct='%1.1f%%',
        shadow=True,
        startangle=90,
        textprops={'fontsize': 10, 'color': 'black', 'wrap': True},
        rotatelabels=True)

plt.title('Distribution of Educational Levels in the USA, 2023')

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig('pie chart/png/354.png', bbox_inches='tight')

# Clear the current image state
plt.clf()