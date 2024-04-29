
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Country = ['USA', 'UK', 'Germany', 'France']
Manufacturing_Output = [8000, 7000, 9000, 10000]
Production_Cost = [6000, 5500, 6500, 7000]

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(Country, Manufacturing_Output, label='Manufacturing Output (million)', width=0.4, align='center', edgecolor='black')
ax.bar(Country, Production_Cost, label='Production Cost (million)', width= -0.4, align='center', edgecolor='black')

ax.set_title('Manufacturing Output and Production Cost in four countries in 2021', fontsize=16, fontweight='bold')
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.set_xticklabels(Country, rotation=0, fontsize=14)
ax.legend(loc='upper right', fontsize=14)
ax.grid(linestyle='--', linewidth=1)

plt.tight_layout()
plt.savefig('bar chart/png/500.png')
plt.clf()