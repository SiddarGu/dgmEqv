

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Draw line chart
plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.plot(['2001', '2002', '2003', '2004'], [200, 250, 150, 300], marker='o', label='Profits A(million dollars)')
ax.plot(['2001', '2002', '2003', '2004'], [150, 200, 250, 350], marker='o', label='Profits B(million dollars)')
ax.plot(['2001', '2002', '2003', '2004'], [250, 300, 350, 300], marker='o', label='Profits C(million dollars)')
ax.plot(['2001', '2002', '2003', '2004'], [300, 350, 400, 250], marker='o', label='Profits D(million dollars)')
plt.xlabel('Year')
plt.ylabel('Profits (million dollars)')
plt.title('Profit analysis of four business units from 2001 to 2004')
ax.xaxis.set_major_locator(mtick.MaxNLocator(integer=True))
plt.legend(loc='best', ncol=2)
for a, b in zip(['2001', '2002', '2003', '2004'], [200, 250, 150, 300]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(['2001', '2002', '2003', '2004'], [150, 200, 250, 350]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(['2001', '2002', '2003', '2004'], [250, 300, 350, 300]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(['2001', '2002', '2003', '2004'], [300, 350, 400, 250]):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.grid(True, linestyle='--', linewidth=0.4)
# Set figure size
plt.tight_layout()
# Save figure
plt.savefig('line chart/png/549.png') 
# Clear figure
plt.clf()