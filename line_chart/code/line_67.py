
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = 'SimHei' 
plt.rcParams['axes.unicode_minus'] = False 
x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August'] 
y1 = [50, 45, 35, 40, 50, 55, 60, 65] 
y2 = [20, 25, 30, 35, 38, 40, 45, 50] 
plt.figure(figsize=(10, 6)) 
plt.plot(x, y1, label='Carbon Emission') 
plt.plot(x, y2, label='Air Pollution') 
plt.xticks(x, rotation=45, wrap=True) 
plt.xlabel('Month') 
plt.ylabel('Values') 
plt.title('Carbon Emission and Air Pollution in California, 2021') 
plt.legend() 
plt.tight_layout() 
plt.savefig('line chart/png/9.png') 
plt.clf()