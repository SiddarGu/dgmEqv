
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

x_data = ["2001","2002","2003","2004","2005"]
y_high_data = [45000,40000,43000,48000,42000]
y_college_data = [10000,11000,13000,15000,17000]

ax.plot(x_data, y_high_data, label='High School Graduates', marker='o', linestyle='--')
ax.plot(x_data, y_college_data, label='College Graduates', marker='*', linestyle='--')

ax.set_xticks(x_data)
plt.title('Number of Graduates from High School and College in the U.S. Between 2001 and 2005')
plt.legend(loc='best')
plt.tight_layout()

plt.savefig('line chart/png/356.png')
plt.clf()