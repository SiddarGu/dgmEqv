
import matplotlib.pyplot as plt

# Define data
Year = [2001, 2002, 2003, 2004]
Unemployment_Rate = [5.7, 5.8, 5.9, 5.7]
Inflation_Rate = [2.2, 2.8, 3.2, 2.7]
GDP_Growth_Rate = [3.4, 2.2, 3.6, 3.5]
Government_Spending = [2.2, 2.3, 2.4, 2.5]

# Create figure
plt.figure(figsize=(10, 4))

# Add subplot
ax = plt.subplot(111)

# Plot line chart
ax.plot(Year, Unemployment_Rate, label='Unemployment Rate(%)', color='blue')
ax.plot(Year, Inflation_Rate, label='Inflation Rate(%)', color='green')
ax.plot(Year, GDP_Growth_Rate, label='GDP Growth Rate(%)', color='red')
ax.plot(Year, Government_Spending, label='Government Spending(trillion dollars)', color='orange')

# Set xticks
plt.xticks(Year)

# Set title
ax.set_title("Economic Indicators in the USA from 2001 to 2004", fontsize=14)

# Set legend
ax.legend(loc="best", fontsize=12)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig("line chart/png/430.png")

# Clear the current image state
plt.clf()