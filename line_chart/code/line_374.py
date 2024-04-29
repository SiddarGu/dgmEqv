
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,6))
x = np.array(['Individual', 'Corporations', 'Foundations', 'Government']) 
y = np.array([1000, 2000, 1500, 4000])
plt.plot(x, y, color='blue', marker='o', linestyle='solid')
plt.title("Donations Received by a Charity Organization in 2021")
plt.xlabel("Donation")
plt.ylabel("Amount")
plt.xticks(rotation=45, ha="right",rotation_mode="anchor")
plt.tight_layout()
plt.savefig("line chart/png/70.png")
plt.clf()