
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(['January','February','March','April','May','June','July','August'],[25,30,40,50,45,40,35,41], label="In-Store Sales(million dollars)")
plt.plot(['January','February','March','April','May','June','July','August'],[58,54,60,66,72,75,81,76], label="Online Sales(million dollars)")
plt.xticks(['January','February','March','April','May','June','July','August'])
plt.xlabel("Month", fontsize = 10)
plt.ylabel("Sales (million dollars)", fontsize = 10)
plt.title("Monthly sales comparison in retail industry")
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/448.png', dpi=300)
plt.clf()