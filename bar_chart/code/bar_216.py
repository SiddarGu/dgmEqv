
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
ax = plt.gca()
ax.bar(["USA","UK","Germany","France"],[4.5,3.4,3.8,2.9],label="Government Spending (billion)",bottom=[5.2,4.1,4.5,3.2],width=0.4)
ax.bar(["USA","UK","Germany","France"],[5.2,4.1,4.5,3.2],label="Public Expenditure (billion)",width=0.4)
plt.title("Government and public spending in four countries in 2021")
plt.xticks(["USA","UK","Germany","France"])
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
plt.tight_layout()
plt.savefig('bar chart/png/80.png')
plt.clf()