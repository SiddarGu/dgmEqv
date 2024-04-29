
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Plotting the data
ax.plot(['2001', '2002', '2003', '2004', '2005'], 
        [25, 30, 32, 28, 30], label = 'Income Tax Rate', 
        marker = 'o', color = 'blue')
ax.plot(['2001', '2002', '2003', '2004', '2005'], 
        [35, 38, 40, 36, 38], label = 'Corporate Tax Rate', 
        marker = 'o', color = 'red')

# Setting title
plt.title('Changes in Tax Rates from 2001 to 2005')

# Adding legend
ax.legend()

# Adding annotations
for xy in zip(['2001', '2002', '2003', '2004', '2005'], 
              [25, 30, 32, 28, 30]):
    ax.annotate('(%s,%s)' % xy, xy=xy, textcoords='data')
for xy in zip(['2001', '2002', '2003', '2004', '2005'], 
              [35, 38, 40, 36, 38]):
    ax.annotate('(%s,%s)' % xy, xy=xy, textcoords='data')

# Setting xticks
plt.xticks(['2001', '2002', '2003', '2004', '2005'])

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/520.png')

# Clear the current image state
plt.clf()