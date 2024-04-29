
import matplotlib.pyplot as plt
import numpy as np

# Restructure the data so that each category (Home Type) has a corresponding list of five elements (minimum, first quartile, median, third quartile, maximum).
Single_Family_Home = [400000,450000,500000,550000,600000]
Townhome = [250000,290000,350000,410000,450000]
Condo= [200000,250000,310000,370000,420000]
Apartment = [100000,140000,200000,250000,300000]
Mobile_Home = [80000,100000,140000,180000,200000]

# Outliers should be handled separately.
Outlier_Price_Single_Family_Home = []
Outlier_Price_Townhome = [800000]
Outlier_Price_Condo = [100000,150000]
Outlier_Price_Apartment = [400000]
Outlier_Price_Mobile_Home = [250000]

# Plot the data with the type of box plot.
fig, ax = plt.subplots(figsize=(15, 8))
ax.boxplot([Single_Family_Home,Townhome,Condo,Apartment,Mobile_Home], labels=['Single Family Home','Townhome','Condo','Apartment','Mobile Home'])

# Outliers are plotted manually using ax.plot for each category, only if there are outliers for that category.
if Outlier_Price_Single_Family_Home:
    ax.plot(np.repeat(1, len(Outlier_Price_Single_Family_Home)), Outlier_Price_Single_Family_Home, 'o', color ='red')
if Outlier_Price_Townhome:
    ax.plot(np.repeat(2, len(Outlier_Price_Townhome)), Outlier_Price_Townhome, 'o', color ='red')
if Outlier_Price_Condo:
    ax.plot(np.repeat(3, len(Outlier_Price_Condo)), Outlier_Price_Condo, 'o', color ='red')
if Outlier_Price_Apartment:
    ax.plot(np.repeat(4, len(Outlier_Price_Apartment)), Outlier_Price_Apartment, 'o', color ='red')
if Outlier_Price_Mobile_Home:
    ax.plot(np.repeat(5, len(Outlier_Price_Mobile_Home)), Outlier_Price_Mobile_Home, 'o', color ='red')

# Drawing techniques such as background grids can be used.
ax.grid()

# The title of the figure should be  Price Distribution of Real Estate Types in 2021.
plt.title('Price Distribution of Real Estate Types in 2021')

# If the text length of the label is too long, use the method of adding the parameter "rotation" or display label on separate lines seting “wrap=true”.
plt.xticks(rotation=45)

# Automatically resize the image by tight_layout() before savefig().
plt.tight_layout()

# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14_202312251044.png.
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/14_202312251044.png')

# Clear the current image state at the end of the code.
plt.clf()