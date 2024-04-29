
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
x = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+'] 
y1 = [20, 25, 30, 35, 40, 45]
y2 = [25, 30, 35, 40, 45, 50]
y3 = [30, 35, 40, 45, 50, 55] 

plt.plot(x, y1, label="Tobacco (%)")
plt.plot(x, y2, label="Alcohol (%)")
plt.plot(x, y3, label="Smoking (%)")

plt.xticks(x)
plt.title("Prevalence of Tobacco, Alcohol and Smoking Habits in Different Age Groups")
plt.xlabel("Age Group")
plt.ylabel("Prevelance (%)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.tight_layout()
plt.savefig('line chart/png/192.png')
plt.clf()