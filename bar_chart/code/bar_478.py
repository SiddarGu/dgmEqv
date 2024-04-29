
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111) 
ax.bar(["USA", "UK", "Germany", "France"], [20, 30, 18, 23], label="Theaters", color="blue") 
ax.bar(["USA", "UK", "Germany", "France"], [45, 50, 40, 47], bottom=[20, 30, 18, 23], label="Museums", color="red") 
ax.bar(["USA", "UK", "Germany", "France"], [50, 60, 45, 53], bottom=[20+45, 30+50, 18+40, 23+47], label="Galleries", color="green") 
ax.set_xticklabels(["USA", "UK", "Germany", "France"], rotation=45, ha="right", wrap=True) 
ax.set_title("Number of theaters, museums, and galleries in four countries in 2021") 
plt.legend(loc="best") 
plt.tight_layout() 
plt.savefig("bar chart/png/59.png") 
plt.clf()