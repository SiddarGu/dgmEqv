
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(["Q1","Q2","Q3","Q4"], [6000,8000,9000,7000], color='b', marker='o', label="Online Sales")
plt.plot(["Q1","Q2","Q3","Q4"], [9000,8000,7000,6000], color='r', marker='*', label="Retail Store Sales")
plt.xticks(["Q1","Q2","Q3","Q4"])
plt.xlabel("Quarter")
plt.ylabel("Sales Amount")
plt.title("Comparison of Online and Retail Store Sales in 2021")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("line chart/png/7.png")
plt.clf()