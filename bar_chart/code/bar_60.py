
import matplotlib.pyplot as plt
plt.figure(figsize=(15,7))
ax = plt.subplot()
ax.bar(['North','South','East','West'],[500000,600000,450000,700000],width=0.5, label="Average Home Value")
ax.bar(['North','South','East','West'],[3000,3500,2500,4000],width=0.5, bottom=[500000,600000,450000,700000], label="Average Rental Price")
ax.set_title("Average home values and rental prices in four regions in 2021")
ax.set_xlabel("Region")
ax.set_ylabel("Price($)")
ax.legend(loc='upper right')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar chart/png/25.png')
plt.clf()