
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6)) 
ax=plt.subplot()
plt.bar(["Facebook", "Instagram", "Twitter", "YouTube"],[2.5, 1.2, 1.5, 2], width=0.4,label='Users (million)')
ax.bar(["Facebook", "Instagram", "Twitter", "YouTube"],[50, 25, 35, 45], width=0.4,bottom=[2.5, 1.2, 1.5, 2],label='Ads')
ax.set_title("Number of users and ads on social media platforms in 2021")
plt.xticks(rotation=30, ha='right', wrap=True)
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/529.png")
plt.clf()