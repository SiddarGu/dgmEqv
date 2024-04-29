
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(x=['Facebook','Instagram','Twitter','YouTube'],height=[3000,400,200,1500], bottom=0, width=0.6, color='#1490f2', alpha=0.8)
ax.set_xlabel('Platform', fontsize=14, fontweight='bold')
ax.set_ylabel('Monthly Active Users (million)', fontsize=14, fontweight='bold')
ax.set_title('Monthly active users of four major social media platforms in 2021', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar chart/png/209.png')
plt.show()
plt.clf()