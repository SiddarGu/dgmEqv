
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
x=['2000','2001','2002','2003','2004','2005']
y_output=[1000,1100,1200,1400,1300,1000]
y_input=[1200,1300,1400,1300,1200,1100]
plt.plot(x,y_output, label='Energy Output(Mega Watts)',color='b', marker='o', linestyle='--', linewidth=2)
plt.plot(x,y_input, label='Energy Input(Mega Watts)',color='r', marker='o', linestyle='--', linewidth=2)
plt.title('Comparison of Energy Output and Input in a Nuclear Reactor from 2000 to 2005')
plt.xlabel('Year')
plt.ylabel('Energy (Mega Watts)')
plt.xticks(x)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, fancybox=True, shadow=True)
plt.tight_layout()
plt.savefig('line chart/png/390.png')
plt.clf()