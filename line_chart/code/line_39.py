
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {"Location": ["Los Angeles", "New York", "Tokyo", "Berlin"], 
        "Number of Artists": [1000, 1200, 900, 1100], 
        "Number of Musicians": [500, 700, 800, 600], 
        "Number of Painters": [400, 600, 300, 500], 
        "Number of Writers": [800, 900, 700, 600]}

df = pd.DataFrame(data)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

ax.plot(df["Location"], df["Number of Artists"], label="Number of Artists")
ax.plot(df["Location"], df["Number of Musicians"], label="Number of Musicians")
ax.plot(df["Location"], df["Number of Painters"], label="Number of Painters")
ax.plot(df["Location"], df["Number of Writers"], label="Number of Writers")

ax.set_title("Number of Artists, Musicians, Painters, and Writers in Four Major Cities")
ax.set_xlabel("Location")
ax.set_ylabel("Number")
ax.set_xticks(df["Location"])
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("line chart/png/481.png")
plt.clf()