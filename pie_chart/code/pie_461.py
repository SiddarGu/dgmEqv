
import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))
platforms = ['Social Media','Streaming Services','Online Shopping','Online Gaming','Other']
percentage = [40,25,15,10,10]
plt.pie(percentage, labels=platforms, autopct='%1.1f%%', startangle=90, explode=[0,0.1,0,0,0])
plt.title('Distribution of Digital Platform Usage in the USA, 2023')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/143.png')
plt.clf()