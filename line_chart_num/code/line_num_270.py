
import matplotlib.pyplot as plt
import numpy as np
 
x = np.array([2001, 2002, 2003, 2004])
y1 = np.array([200, 220, 190, 250])
y2 = np.array([180, 210, 230, 220])
y3 = np.array([100, 120, 110, 130])
 
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="Music Albums Sold(million)", color='red', marker='o', linestyle='--', linewidth=2)
plt.plot(x, y2, label="Movie Tickets Sold(million)", color='blue', marker='^', linestyle='-', linewidth=2)
plt.plot(x, y3, label="Art Gallery Visits(million)", color='green', marker='s', linestyle=':', linewidth=2)
 
plt.title("Arts and culture industry visits and sales in the early 2000s")
plt.xlabel('Year')
plt.ylabel('Number')
plt.xticks(x)
plt.legend()
 
for a, b, c in zip(x, y1, y2):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    plt.text(a, c + 0.05, '%.0f' % c, ha='center', va='bottom', fontsize=10)
plt.text(2004, y3[-1] + 0.05, '%.0f' % y3[-1], ha='center', va='bottom', fontsize=10)
 
plt.savefig('line chart/png/134.png')
plt.tight_layout()
plt.clf()