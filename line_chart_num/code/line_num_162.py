
import matplotlib.pyplot as plt
import numpy as np

data = [['January', 10000, 500], ['February', 15000, 550], ['March', 13000, 450], ['April', 20000, 700], ['May', 18000, 650], ['June', 12000, 400]]

month = [x[0] for x in data]
Manufacturing_Output = [x[1] for x in data]
Raw_Material_Cost = [x[2] for x in data]

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot(111)

ax.plot(month, Manufacturing_Output, label="Manufacturing Output(units)", color="red")
ax.plot(month, Raw_Material_Cost, label="Raw Material Cost(dollars)", color="blue")

ax.set_title("Change in Manufacturing Output and Raw Material Cost during 2021")
ax.set_xlabel("Month")

ax.set_xticks(np.arange(len(month)), minor=False)
ax.set_xticklabels(month, rotation=45, fontsize=14)

ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=3, fancybox=True, shadow=True, fontsize=14)
ax.grid(True, linestyle='-.',which='major', color='grey', alpha=0.3)

for i in range(len(month)):
    ax.annotate(Manufacturing_Output[i], xy=(i, Manufacturing_Output[i]), xytext=(i+0.1, Manufacturing_Output[i]+500))
    ax.annotate(Raw_Material_Cost[i], xy=(i, Raw_Material_Cost[i]), xytext=(i+0.1, Raw_Material_Cost[i]+50))

plt.tight_layout()
plt.savefig('line chart/png/99.png')
plt.clf()