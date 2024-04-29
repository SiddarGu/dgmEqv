
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot([2000,2001,2002,2003,2004], [10,11,12,13,14], label="Production A(million units)")
ax.plot([2000,2001,2002,2003,2004], [8,9,10,11,12], label="Production B(million units)")
ax.plot([2000,2001,2002,2003,2004], [12,13,14,15,16], label="Production C(million units)")
ax.plot([2000,2001,2002,2003,2004], [15,16,17,18,20], label="Production D(million units)")
ax.set_title("Manufacturing output of four product categories from 2000 to 2004")
ax.set_xlabel("Year")
ax.set_ylabel("Production(million units)")
ax.legend(loc="best")
ax.grid(linestyle="--")
plt.xticks([2000,2001,2002,2003,2004])
for a,b in zip([2000,2001,2002,2003,2004], [10,11,12,13,14]):
    ax.annotate('%.0f' % b, xy=(a,b), xycoords='data', xytext=(-20,5), textcoords='offset points', fontsize=14)
for a,b in zip([2000,2001,2002,2003,2004], [8,9,10,11,12]):
    ax.annotate('%.0f' % b, xy=(a,b), xycoords='data', xytext=(-20,5), textcoords='offset points', fontsize=14)
for a,b in zip([2000,2001,2002,2003,2004], [12,13,14,15,16]):
    ax.annotate('%.0f' % b, xy=(a,b), xycoords='data', xytext=(-20,5), textcoords='offset points', fontsize=14)
for a,b in zip([2000,2001,2002,2003,2004], [15,16,17,18,20]):
    ax.annotate('%.0f' % b, xy=(a,b), xycoords='data', xytext=(-20,5), textcoords='offset points', fontsize=14)
plt.tight_layout()
plt.savefig('line chart/png/188.png')
plt.clf()