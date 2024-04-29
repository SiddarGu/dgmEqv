
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))#set size
ax=plt.subplot() #create figure
plt.title("Raw material usage in three categories from January to April 2021") 
month=['January','February','March','April']
Raw_Material_A=[100000,90000,110000,80000]
Raw_Material_B=[130000,140000,150000,160000]
Raw_Material_C=[80000,110000,120000,140000]
x=range(len(month))
ax.bar(x,Raw_Material_A,label='Raw Material A(KG)',bottom=0,width=0.3)
ax.bar(x,Raw_Material_B,label='Raw Material B(KG)',bottom=Raw_Material_A,width=0.3)
ax.bar(x,Raw_Material_C,label='Raw Material C(KG)',bottom=[i+j for i,j in zip(Raw_Material_A,Raw_Material_B)],width=0.3)
ax.set_xticks(x)
ax.set_xticklabels(month, rotation=45, ha='right', wrap=True)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25),
          fancybox=True, shadow=True, ncol=5)
plt.tight_layout()
plt.savefig("bar chart/png/31.png")
plt.clf()