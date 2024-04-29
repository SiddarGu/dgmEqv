
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
ax = plt.subplot()
ax.set_title('Nutritional Intake of Young Adults from 20-23 years old')
ax.set_xlabel('Age')
ax.set_ylabel('Calories(kcal) and Carbohydrates(g)')
plt.xticks([20,21,22,23])
plt.plot([20,21,22,23], [2000,2200,2100,1800], color="blue", label="Recommended Calories(kcal)")
plt.plot([20,21,22,23], [1900,2000,2200,2000], color="red", label="Actual Calories(kcal)")
plt.plot([20,21,22,23], [220,250,230,200], color="green", label="Carbohydrates(g)")
for a,b,c,d in zip([20,21,22,23], [2000,2200,2100,1800], [1900,2000,2200,2000], [220,250,230,200]):
    ax.annotate('R.C({}) A.C({}) C({})'.format(b,c,d), xy=(a, max(b,c,d)), xytext=(-12, 10), textcoords='offset points')
plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/440.png')
plt.clf()