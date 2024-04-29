
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))

Industry = ['Automotive','Aerospace','Electronics','Textile','Pharmaceuticals','Metal','Wood']
Percentage = [30,15,20,10,10,10,5]
 
colors = ['#414141','#A9A9A9','#708090','#00FFFF','#7FFFD4','#FFA500','#00FF7F'] 
explode = [0,0,0,0,0,0,0.1]

plt.pie(Percentage, explode=explode, labels=Industry, colors=colors, autopct='%1.2f%%',
        shadow=True, startangle=90)

plt.tight_layout()
plt.title("Distribution of Manufacturing Industries in the USA,2023")
plt.xticks(rotation=45)

plt.savefig('pie chart/png/119.png')
plt.clf()