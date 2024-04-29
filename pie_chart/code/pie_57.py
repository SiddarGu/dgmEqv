
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.pie(x=[60,25,10,5], labels=['Road','Railway','Waterway','Air'], autopct='%.1f%%',
        textprops={'fontsize': 10, 'color': 'black'}, 
        wedgeprops={'linewidth': 2, 'edgecolor': 'white'}, 
        shadow=True, startangle=90, rotatelabels=True)
plt.title('Breakdown of Transportation Modes in the USA, 2023', fontsize=15)
plt.tight_layout()
plt.savefig('pie chart/png/470.png')
plt.clf()