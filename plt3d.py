# -- coding: utf-8 --

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib as mpl  
  
def draw_bar(labels, title, quants, colors): 

	width = 0.4  
	ind = np.linspace(0.3, 3, len(labels))  
	# make a square figure  
	fig = plt.figure(1)  
	ax  = fig.add_subplot(111)  
	# Bar Plot  
	ax.bar(ind-width/2,quants,width,color=list(colors), alpha = 0.8)  
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

def one2one():
	labels_1   = ['COLOR-base', 'RANDOM']
	labels_2   = ['COLOR-base', 'USER-base']
	labels_3   = ['COLOR-base', 'CONTENT-base']

	quants_1 = [1.33, 0.71] 
	quants_2 = [1.33, 0.864] 
	quants_3 = [1.33, 0.992] 

	colors_1 = ["#41B684", "#F88836"]
	colors_2 = ["#41B684", "#5255DC"]
	colors_3 = ["#41B684", "#D949E4"]

#	draw_bar(labels_1, 'mean Satisfaction', quants_1, colors_1)
#	draw_bar(labels_2, 'mean Satisfaction', quants_2, colors_2)
	draw_bar(labels_3, 'mean Satisfaction', quants_3, colors_3)

def one2one_color_user():
	labels_1   = ['COLOR_USER', 'RANDOM']
	labels_2   = ['COLOR_USER', 'USER-base']
	labels_3   = ['COLOR_USER', 'CONTENT-base']
	labels_4   = ['COLOR_USER', 'COLOR-base']

	quants_1 = [1.746, 0.71] 
	quants_2 = [1.746, 0.864] 
	quants_3 = [1.746, 0.992] 
	quants_4 = [1.746, 1.33] 

	colors_1 = ["#EE1556", "#F88836"]
	colors_2 = ["#EE1556", "#5255DC"]
	colors_3 = ["#EE1556", "#D949E4"]
	colors_4 = ["#EE1556", "#41B684"]

#	draw_bar(labels_1, 'mean Satisfaction', quants_1, colors_1)
#	draw_bar(labels_2, 'mean Satisfaction', quants_2, colors_2)
#	draw_bar(labels_3, 'mean Satisfaction', quants_3, colors_3)
	draw_bar(labels_4, 'mean Satisfaction', quants_4, colors_4)

def draw_test_1():
	labels   = ['COLOR-base', 'USER-base', 'CONTENT-base', 'RANDOM']  
	quants_ctr = [0.398, 0.38, 0.35, 0.299] 
	quants_clicks = [29.4, 28.6, 30, 31] 
	quants_statis = [1.33, 0.864, 0.992, 0.71] 
	quants_time = [6.092, 5.576, 6.252, 8.318]  

	colors = []
	colors.append("#41B684")
	colors.append("#5255DC")
	colors.append("#D949E4")
	colors.append("#F88836")

	draw_bar(labels, 'mean CTR', quants_ctr, colors)
	draw_bar(labels, 'mean Pay-Per-Click', quants_clicks, colors)
	draw_bar(labels, 'mean Satisfaction', quants_statis, colors)
	draw_bar(labels, 'mean Browse-Time', quants_time, colors)

def draw_test_2():
	labels   = ['COLOR_USER', 'COLOR-base', 'USER-base', 'CONTENT-base', 'RANDOM']  
	quants_ctr = [0.39, 0.398, 0.38, 0.35, 0.299] 
	quants_clicks = [24.4, 29.4, 28.6, 30, 31] 
	quants_statis = [1.746, 1.33, 0.864, 0.992, 0.71] 
	quants_time = [5.232, 6.092, 5.576, 6.252, 8.318]  
	titles = ['CTR', 'Pay-Per-Click', 'Satisfaction', 'Browse Time']

	colors = []
	colors.append("#EE1556")
	colors.append("#41B684")
	colors.append("#5255DC")
	colors.append("#D949E4")
	colors.append("#F88836")

	draw_bar(labels, 'mean CTR', quants_ctr, colors)
	draw_bar(labels, 'mean Pay-Per-Click', quants_clicks, colors)
	draw_bar(labels, 'mean Satisfaction', quants_statis, colors)
	draw_bar(labels, 'mean Browse-Time', quants_time, colors)

# t检定，改善前/改善后的分布
def draw_test_3():
	labels   = ['C', 'C', 'C', 'CU', 'C', 'CU', 'C', 'CU', 'CU', 'CU']  
	quants_statis = [1.0,1.25,1.3,1.33,1.5,1.58,1.62,1.8,2.0,2.0] 

	titles = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
	colors = ["#41B684","#41B684","#41B684","#EE1556","#41B684","#EE1556","#41B684","#EE1556","#EE1556","#EE1556"]
	draw_bar(labels, 'Satisfaction', quants_statis, colors)

one2one_color_user()