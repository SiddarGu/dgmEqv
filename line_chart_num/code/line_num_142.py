
import matplotlib.pyplot as plt

age = ["18-24","25-34","35-44","45-54","55-64","65+"]
obese = [30,35,40,45,50,60]
overweight = [50,45,40,35,30,25]
normal = [20,20,20,20,20,15]

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1,1,1)
ax.plot(age,obese, label='Obese Percentage', marker='o', color='blue')
ax.plot(age,overweight, label='Overweight Percentage', marker='s', color='red')
ax.plot(age,normal, label='Normal Weight Percentage', marker='^', color='green')

for a,b in zip(age,obese):
    ax.annotate(str(b)+'%', xy=(a,b), xytext=(0,3), textcoords="offset points")

for a,b in zip(age,overweight):
    ax.annotate(str(b)+'%', xy=(a,b), xytext=(0,3), textcoords="offset points")

for a,b in zip(age,normal):
    ax.annotate(str(b)+'%', xy=(a,b), xytext=(0,3), textcoords="offset points")

ax.set_title("Prevalence of obesity, overweight, and normal weight among adults in the US")
ax.set_xlabel("Age")
ax.set_ylabel("Percentage")

ax.set_xticks(age)

ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig('line chart/png/423.png')
plt.clf()