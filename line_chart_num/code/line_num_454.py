
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Data
country = ['USA','China','India','Japan']
GDP = [21.44,14.14,2.94,5.04]
edu = [719.8,541.7,93.4,311.5]
health = [1120.5,664.0,119.1,436.3]
defense = [732.6,261.7,72.1,239.2]

# Plot
plt.plot(country, GDP, label='GDP', marker='o')
plt.plot(country, edu, label='Education', marker='o')
plt.plot(country, health, label='Healthcare', marker='o')
plt.plot(country, defense, label='Defense', marker='o')

# Labels
plt.xlabel('Country')
plt.ylabel('Expenditures')

# Setting xticks
plt.xticks(np.arange(4),country)

# Legend
plt.legend(loc='upper right')

# Annotate
plt.annotate("USA: $732.6B", xy=(0,732.6))
plt.annotate("China: $261.7B", xy=(1,261.7))
plt.annotate("India: $72.1B", xy=(2,72.1))
plt.annotate("Japan: $239.2B", xy=(3,239.2))

# Title
plt.title('Government Expenditures on GDP, Education, Healthcare, and Defense in the US, China, India, and Japan')

# Save
plt.tight_layout()
plt.savefig('line chart/png/305.png')

# Clear
plt.clf()