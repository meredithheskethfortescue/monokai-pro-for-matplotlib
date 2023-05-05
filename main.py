"""Monokai Pro for Matplotlib"""
import matplotlib.pyplot as plt


# get list of available parameters and their current value
for key, value in zip(plt.rcParams, plt.rcParams.values()):
	print(f"{key} : {value}")

# palette
color_base_bg = '#1d2528'
color_text_white = '#8b9798'

# set parameter
plt.rcParams['axes.facecolor'] = color_base_bg
plt.rcParams['figure.facecolor'] = color_base_bg
plt.rcParams['axes.edgecolor'] = color_text_white
plt.rcParams['xtick.color'] = color_text_white
plt.rcParams['ytick.color'] = color_text_white
