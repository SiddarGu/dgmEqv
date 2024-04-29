
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
ax = plt.subplot()
ax.plot( [20,21,22,23,24,25], [75,76,78,79,80,81], 'b-', label="Weight(kg)")
ax.plot( [20,21,22,23,24,25], [1.7,1.7,1.7,1.7,1.7,1.7], 'g-', label="Height(m)")
ax.plot( [20,21,22,23,24,25], [25.8,26.2,27.1,27.5,27.8,28.2], 'r-', label="BMI")
plt.title("Change in height, weight and BMI of a person from age 20 to 25")
ax.legend(loc='upper left')
ax.set_xticks([20,21,22,23,24,25])
plt.tight_layout()
plt.savefig('line chart/png/262.png')
plt.clf()