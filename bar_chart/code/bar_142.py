
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax=plt.subplot()
plt.bar(["USA","UK","Germany","France"],[20000,30000,18000,23000],label='Hotel Rooms',width=0.4,bottom=0)
plt.bar(["USA","UK","Germany","France"],[450000,500000,400000,470000],label='Tourist Visits',width=0.4,bottom=20000)
plt.xticks(["USA","UK","Germany","France"],["USA","UK","Germany","France"],rotation=45,fontsize=8)
plt.title("Number of hotel rooms and tourist visits in four countries in 2021")
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/420.png")
plt.clf()