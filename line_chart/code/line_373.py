
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
plt.plot(['Renaissance','Baroque','Rococo','Impressionism'],[100,120,90,150],label='Painting A')
plt.plot(['Renaissance','Baroque','Rococo','Impressionism'],[80,90,110,120],label='Painting B')
plt.plot(['Renaissance','Baroque','Rococo','Impressionism'],[120,110,130,140],label='Painting C')
plt.plot(['Renaissance','Baroque','Rococo','Impressionism'],[150,160,120,80],label='Painting D')
plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.05),ncol=4)
plt.xticks(['Renaissance','Baroque','Rococo','Impressionism'])
plt.title('Number of Paintings Produced by Artistic Movement')
plt.tight_layout()
plt.savefig('line chart/png/358.png')
plt.clf()