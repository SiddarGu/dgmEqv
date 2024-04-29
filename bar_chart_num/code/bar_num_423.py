
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 8))

State = ["California", "Texas", "Arizona", "Nevada"]
Power_Generation = [10000, 12000, 9000, 8000]
Solar_Generation = [4000, 5000, 4500, 4800]
Wind_Generation = [5000, 6000, 5500, 5200]

ax.bar(State, Power_Generation, color='C0', label="Power Generation (MWh)")
ax.bar(State, Solar_Generation, bottom=Power_Generation, color='C1', label="Solar Generation (MWh)")
ax.bar(State, Wind_Generation, bottom=np.array(Power_Generation)+np.array(Solar_Generation), color='C2', label="Wind Generation (MWh)")

for i, v in enumerate(Power_Generation):
    ax.text(i, v + 0.2, str(v), color='black', fontweight='bold')
for i, v in enumerate(Solar_Generation):
    ax.text(i, v + Power_Generation[i] + 0.2, str(v), color='black', fontweight='bold')
for i, v in enumerate(Wind_Generation):
    ax.text(i, v + Power_Generation[i] + Solar_Generation[i] + 0.2, str(v), color='black', fontweight='bold')

plt.title("Power and renewable energy generation in four states in 2021")
plt.xticks(np.arange(len(State)), State, rotation=45)
plt.legend(loc="upper right")

plt.tight_layout()

plt.savefig("Bar Chart/png/437.png")
plt.clf()