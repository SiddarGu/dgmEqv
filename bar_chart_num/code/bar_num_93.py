
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 200, 450], ['UK', 250, 500], ['Germany', 180, 400], ['France', 230, 470]]

fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111) 

Country = [row[0] for row in data] 
Retail_Store_Revenue = [row[1] for row in data] 
E_commerce_Revenue = [row[2] for row in data] 

ax.bar(Country, Retail_Store_Revenue, width=0.3, color="red", label="Retail Store Revenue")
ax.bar(Country, E_commerce_Revenue, width=0.3, bottom=Retail_Store_Revenue, color="blue", label="E-commerce Revenue")

for i, v in enumerate(Retail_Store_Revenue):
    ax.text(i - 0.15 ,v + 30, str(v), color='black', fontsize=12) 
for i, v in enumerate(E_commerce_Revenue):
    ax.text(i + 0.15 ,v + 30, str(v), color='black', fontsize=12) 

plt.xticks(np.arange(len(Country)), Country, rotation=45) 

plt.title("Revenues of Retail Stores and E-commerce in four countries in 2021")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)

plt.tight_layout()

plt.savefig("Bar Chart/png/182.png")
plt.clf()