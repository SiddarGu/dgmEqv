
            
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Smartphone_Users =  [300, 150, 120, 140]
Internet_Users = [320, 210, 190, 220]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.bar(Country, Smartphone_Users, label="Smartphone Users", bottom=0)
ax.bar(Country, Internet_Users, label="Internet users", bottom=Smartphone_Users)
plt.title("Number of smartphone users and internet users in four countries in 2021")
plt.xticks(Country, rotation=45)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/564.png')
plt.clf()