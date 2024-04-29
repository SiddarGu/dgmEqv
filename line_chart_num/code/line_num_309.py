
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(12,9))

# Data
year = [2001,2002,2003,2004]
manufactured_A = [100,110,90,150]
manufactured_B = [80,90,110,120]
manufactured_C = [120,115,130,140]
manufactured_D = [150,160,120,90]

# Plot
plt.plot(year, manufactured_A, label='Manufactured A (million units)', marker='o', color='blue', linewidth=3)
plt.plot(year, manufactured_B, label='Manufactured B (million units)', marker='s', color='green', linewidth=3)
plt.plot(year, manufactured_C, label='Manufactured C (million units)', marker='^', color='red', linewidth=3)
plt.plot(year, manufactured_D, label='Manufactured D (million units)', marker='D', color='orange', linewidth=3)

# Add legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=4, fontsize='large', fancybox=True, shadow=True)

# Add title
plt.title('Production of four types of products in the past four years', fontsize=20)

# Set xticks
plt.xticks(year)

# Annotate
for i,j in zip(year, manufactured_A):
    plt.annotate(str(j),xy=(i,j), xytext=(-20,10), textcoords='offset points', fontsize=12)
for i,j in zip(year, manufactured_B):
    plt.annotate(str(j),xy=(i,j), xytext=(-20,10), textcoords='offset points', fontsize=12)
for i,j in zip(year, manufactured_C):
    plt.annotate(str(j),xy=(i,j), xytext=(-20,10), textcoords='offset points', fontsize=12)
for i,j in zip(year, manufactured_D):
    plt.annotate(str(j),xy=(i,j), xytext=(-20,10), textcoords='offset points', fontsize=12)

# Save
plt.tight_layout()
plt.savefig('line chart/png/446.png')
plt.clf()