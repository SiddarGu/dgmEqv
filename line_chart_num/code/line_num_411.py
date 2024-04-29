
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.plot([2001,2002,2003,2004,2005,2006],[220,200,180,170,190,210],label="Average Home Price (thousands of dollars)")
ax.plot([2001,2002,2003,2004,2005,2006],[14,13,12,11,13,15],label="Average Rent (thousands of dollars)")
plt.title("Average Home Prices and Rents in the US, 2001-2006")
ax.set_xticks([2001,2002,2003,2004,2005,2006])
ax.set_xlabel("Year")
ax.set_ylabel("Price/Rent (thousands of dollars)")
for i,j in zip([2001,2002,2003,2004,2005,2006],[220,200,180,170,190,210]):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip([2001,2002,2003,2004,2005,2006],[14,13,12,11,13,15]):
    ax.annotate(str(j),xy=(i,j))
ax.legend()
plt.tight_layout()
plt.savefig("line chart/png/48.png")
plt.clf()