
import matplotlib.pyplot as plt
month = ['January','February','March','April','May','June','July']
product_A = [350,450,550,400,500,600,650]
product_B = [400,400,450,500,550,550,600]
product_C = [450,500,500,550,650,700,750]
product_D = [500,550,600,650,700,750,800]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(month, product_A,label="Product A")
ax.plot(month, product_B,label="Product B")
ax.plot(month, product_C,label="Product C")
ax.plot(month, product_D,label="Product D")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4, fancybox=True, shadow=True, fontsize='large')
ax.set_title('Monthly Sales of Four Products in an E-commerce Business')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')
ax.set_xticks(month)
ax.grid(True, linestyle='-', color='0.75')

for i,j in zip(month,product_A):
    ax.annotate(str(j),xy=(i,j), xytext=(0, 7), textcoords='offset points', fontsize='large')
for i,j in zip(month,product_B):
    ax.annotate(str(j),xy=(i,j), xytext=(0, 7), textcoords='offset points', fontsize='large')
for i,j in zip(month,product_C):
    ax.annotate(str(j),xy=(i,j), xytext=(0, 7), textcoords='offset points', fontsize='large')
for i,j in zip(month,product_D):
    ax.annotate(str(j),xy=(i,j), xytext=(0, 7), textcoords='offset points', fontsize='large')

plt.tight_layout()
plt.savefig('line chart/png/246.png')
plt.clf()