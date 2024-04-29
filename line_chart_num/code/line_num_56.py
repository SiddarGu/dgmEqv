
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

ax.plot([2001, 2002, 2003, 2004], [100, 120, 140, 160], label='Music Albums Sold(million units)', color='red', linestyle='solid', marker='o')
ax.plot([2001, 2002, 2003, 2004], [200, 180, 140, 120], label='Books Sold(million units)', color='green', linestyle='solid', marker='o')
ax.plot([2001, 2002, 2003, 2004], [500, 450, 400, 350], label='Movies Released', color='blue', linestyle='solid', marker='o')

ax.annotate('Music Albums Sold(million units):100', xy=(2001, 100), xytext=(2002, 100),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Music Albums Sold(million units):160', xy=(2004, 160), xytext=(2003, 160),
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.annotate('Books Sold(million units):200', xy=(2001, 200), xytext=(2002, 200),
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('Books Sold(million units):120', xy=(2004, 120), xytext=(2003, 120),
            arrowprops=dict(facecolor='green', shrink=0.05))
ax.annotate('Movies Released:500', xy=(2001, 500), xytext=(2002, 500),
            arrowprops=dict(facecolor='blue', shrink=0.05))
ax.annotate('Movies Released:350', xy=(2004, 350), xytext=(2003, 350),
            arrowprops=dict(facecolor='blue', shrink=0.05))

ax.set_title("Popular Arts and Culture Products from 2001 to 2004")
ax.set_xlabel('Year')
ax.set_ylabel('Units')
ax.set_xticks([2001, 2002, 2003, 2004])
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/148.png')
plt.clf()