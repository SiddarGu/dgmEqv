
import matplotlib.pyplot as plt
import numpy as np

labels = ["Personal Pension funds", "Occupational Pension funds", "Personal Retirement Savings Accounts", "State Pension funds", "Other Pension funds"]
percentages = [25,20,30,15,10]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})
ax.set_title("Distribution of Pension Funds in the US, 2023")
plt.tight_layout()
plt.savefig("pie chart/png/159.png")
plt.clf()