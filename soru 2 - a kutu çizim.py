# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
data_1 = [350,350,350,358,370,370,370,371,371,372,372,384,391,391,392]

data_2 = [350,354,359,363,365,368,369,371,373,374,376,380,383,388,392]

data_3 = [350,361,362,364,364,365,366,371,377,377,377,379,380,380,392]


data = [data_1, data_2, data_3]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,notch ='True', vert = 0)

colors = ['#0000FF', '#00FF00','#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
	patch.set_facecolor(color)

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
	whisker.set(color ='#8B008B',linewidth = 1.5,linestyle =":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
	cap.set(color ='#8B008B',linewidth = 2)

# changing color and linewidth of
# medians
for median in bp['medians']:
	median.set(color ='red',linewidth = 3)

# changing style of fliers
for flier in bp['fliers']:
	flier.set(marker ='D',color ='#e7298a',alpha = 0.5)
	
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2', 'data_3'])

# Adding title
plt.title("Customized box plot")

# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
	
# show plot
plt.show()
