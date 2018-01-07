# -- coding: utf-8 --

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib as mpl  
  
def draw_bar(labels,title, quants):  
	colors = []
	colors.append("#41B684")
	colors.append("#5255DC")
	colors.append("#D949E4")
	colors.append("#F88836")

	width = 0.4  
	ind = np.linspace(0.5,9.5,4)  
	# make a square figure  
	fig = plt.figure(1)  
	ax  = fig.add_subplot(111)  
	# Bar Plot  
	ax.bar(ind-width/2,quants,width,color=list(colors))  
	# Set the ticks on x-axis  
	ax.set_xticks(ind)  
	ax.set_xticklabels(labels)  
	# labels  
	ax.set_xlabel('Recommend Engine')  
	ax.set_ylabel('Result')  
	# title  
	ax.set_title(title, bbox={'facecolor':'0.8', 'pad':5})  
#	plt.grid(True)  
#	plt.show()  
	plt.savefig(title + ".jpg")  
	plt.close()
  
labels   = ['COLOR base', 'USER base', 'CONTENT base', 'RANDOM']  
quants_ctr = [0.398, 0.38, 0.35, 0.299] 
quants_clicks = [29.4, 28.6, 30, 31] 
quants_statis = [1.33, 0.864, 0.992, 0.71] 
quants_time = [6.092, 5.576, 6.252, 8.318]  
titles = ['CTR', 'Pay Per Click', 'Satisfaction', 'Browse Time']

draw_bar(labels, 'CTR', quants_ctr)
draw_bar(labels, 'Pay Per Click', quants_clicks)
draw_bar(labels, 'Satisfaction', quants_statis)
draw_bar(labels, 'Browse Time', quants_time)