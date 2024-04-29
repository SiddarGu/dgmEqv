
import matplotlib.pyplot as plt

education_level = ['Elementary School','Middle School','High School','College','Postgraduate']
percentage = [20, 25, 30, 15, 10] 

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(percentage, labels=education_level, autopct='%.2f%%', 
        shadow=True, radius=1.2, textprops={'fontsize':12, 'wrap': True},rotatelabels=True)
ax.set_title('Education Level Distribution among US Population, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/203.png')
plt.clf()