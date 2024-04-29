
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Public_Spending = [400,300,350,250]
Tax_Revenue = [450,350,400,300]

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(Country,Public_Spending,color="royalblue",label="Public Spending")
ax.bar(Country,Tax_Revenue,bottom=Public_Spending,color="darkorange",label="Tax Revenue")
ax.set_xticks(Country)
ax.set_xlabel("Country",fontsize=14)
ax.set_ylabel("Amount(billion)",fontsize=14)
ax.set_title("Government spending and tax revenue in four countries in 2021",fontsize=18)
ax.legend()
plt.tight_layout()
plt.savefig("bar chart/png/419.png")
plt.clf()