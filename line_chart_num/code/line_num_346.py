
import matplotlib.pyplot as plt
import pandas as pd

# Create dataframe
df = pd.DataFrame({'Month': ['January', 'February', 'March', 'April','May','June','July','August','September','October','November','December'],
                   'Total Visits': [2500,3000,3500,4000,4500,5000,4500,4000,3500,3000,2500,2000],
                   'Hotel Room Bookings': [300,270,320,400,450,500,400,350,290,280,270,250],
                   'Average Spend': [50,52,60,65,70,75,80,75,68,60,50,45]})

# Create figure
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(1, 1, 1)

# Set label and title
ax.set_xlabel('Month')
ax.set_ylabel('Total Visits/Hotel Room Bookings/Average Spend')
ax.set_title('Monthly tourism trends in a popular tourist destination in 2021')

# Plot lines
ax.plot(df['Month'], df['Total Visits'], color="red", label="Total Visits", linewidth=2)
ax.plot(df['Month'], df['Hotel Room Bookings'], color="green", label="Hotel Room Bookings", linewidth=2)
ax.plot(df['Month'], df['Average Spend'], color="blue", label="Average Spend", linewidth=2)

# Set ticks
ax.set_xticks(df.index)
ax.set_xticklabels(df.Month, rotation=45, ha="right", wrap=True)

# Add legend
ax.legend()

# Add annotate
for i, txt in enumerate(df['Total Visits']):
    ax.annotate(txt, (df.index[i], df['Total Visits'][i]),
                xytext=(df.index[i], df['Total Visits'][i]))
for i, txt in enumerate(df['Hotel Room Bookings']):
    ax.annotate(txt, (df.index[i], df['Hotel Room Bookings'][i]),
                xytext=(df.index[i], df['Hotel Room Bookings'][i]))
for i, txt in enumerate(df['Average Spend']):
    ax.annotate(txt, (df.index[i], df['Average Spend'][i]),
                xytext=(df.index[i], df['Average Spend'][i]))

# Save the figure
plt.tight_layout()
plt.savefig('line chart/png/593.png', format='png', dpi=600)
plt.clf()