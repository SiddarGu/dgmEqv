
import matplotlib.pyplot as plt

# Set up figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

# Draw pie chart
payment_methods = ['Credit Cards', 'PayPal', 'Debit Cards', 'Cash', 'Other']
percentages = [49, 25, 13, 8, 5]
ax.pie(percentages, labels=payment_methods, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12, 'color': 'black'})

# Set parameters
ax.set_title('Popular Payment Methods among Online Consumers, 2023', fontsize=14)
ax.axis('equal')
ax.set_xticks([])

fig.tight_layout()

# Save figure
fig.savefig('pie chart/png/107.png')

# Clear current image state
plt.clf()