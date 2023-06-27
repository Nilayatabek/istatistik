# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Creating dataset
data_1 = [194, 228,205, 209, 209,205,184,209,198,203,213,228,194,214,188,236,229,187,223,208]
data_2 = [193,207,204,184,173,182,218,219,214,251,206,241,197,201,191,185,151,215,227,192]
data = [data_1, data_2]

fig = plt.figure(figsize =(10, 7))
ax = fig.add_subplot(111)

# Creating axes instance
bp = ax.boxplot(data, patch_artist = True,
				notch ='True', vert = 0)

colors = ['#0000FF', '#00FF00',
		'#FFFF00', '#FF00FF']

for patch, color in zip(bp['boxes'], colors):
	patch.set_facecolor(color)

# changing color and linewidth of
# whiskers
for whisker in bp['whiskers']:
	whisker.set(color ='#8B008B',
				linewidth = 1.5,
				linestyle =":")

# changing color and linewidth of
# caps
for cap in bp['caps']:
	cap.set(color ='#8B008B',
			linewidth = 2)

# changing color and linewidth of
# medians
for median in bp['medians']:
	median.set(color ='red',
			linewidth = 3)

# changing style of fliers
for flier in bp['fliers']:
	flier.set(marker ='D',
			color ='#e7298a',
			alpha = 0.5)
	
# x-axis labels
ax.set_yticklabels(['data_1', 'data_2'])

# Adding title
plt.title("Customized box plot")

# Removing top axes and right axes
# ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
	
# show plot
plt.show()
