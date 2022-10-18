import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv("extracted_data_vis5.csv")

# remove missing values in years of education
na_values = [99, 98]
df = df[~df.Highest_Year_Education_Before_Prison.isin(na_values)]

drug_data = df.groupby('Highest_Year_Education_Before_Prison')["Alcohol", 'Marijuana', 'Cocaine', 'Heroin'].apply(lambda r: r[r==1].count())
drug_data["total_prisoners"] = df.groupby('Highest_Year_Education_Before_Prison')['Alcohol'].count().values
drug_data.reset_index(inplace=True)

#GLOBAL
points_with_annotation = []

def main():
    subplots = ZoomingSubplots(4, 1)
    colors = ['#780000', '#c1121f', '#003049', '#669bbc']
    labels = ['Alcohol', 'Marijuana', 'Cocaine', 'Heroin']
    present_data = [drug_data['Alcohol'], drug_data['Marijuana'], drug_data['Cocaine'], drug_data['Heroin']]
    i = -1
    for ax, color in zip(subplots.axes.flat, colors):
        i += 1
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        data = present_data[i]
        ax.set_ylabel(labels[i])
        ax.scatter(x, data, color=color)
        
        for index in range(len(data)):
            print(x[index], data[index])
            point, = ax.plot(x[index], data[index], 'o', markersize=10, alpha=0)
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
            arrow=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", fc="w")
            annotation = ax.annotate('Number of prisoners: ' + str(data[index]) + '\nYears of Education: ' + str(x[index]),
                xy=(x[index], data[index]), xycoords='data',
                xytext=(15, 15), textcoords='offset pixels',
                bbox=props, arrowprops=arrow
            )
            
            annotation.set_visible(True)
            print(ax)
            points_with_annotation.append([point, annotation, ax])
            
            
        if(i==3): 
            ax.get_xaxis().set_visible(True)    
        else:
            ax.get_xaxis().set_visible(False)
        
    #plt.ion()
    subplots.fig.supxlabel('Years of Education before Prison')
    subplots.fig.suptitle('Click on an axes to make it fill the figure.\n'
                 'Click again to restore it to its original position')
    
    plt.show()


class ZoomingSubplots(object):
    def __init__(self, *args, **kwargs):
        """All parameters passed on to 'subplots`."""
        self.fig, self.axes = plt.subplots(*args, **kwargs)
        self._zoomed = False
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_move)
    
    def zoom(self, selected_ax):
        for ax in self.axes.flat:
            ax.set_visible(False)
        self._original_size = selected_ax.get_position()
        selected_ax.set_position([0.125, 0.1, 0.775, 0.8])
        selected_ax.set_visible(True)
        self._zoomed = True

    def unzoom(self, selected_ax):
        selected_ax.set_position(self._original_size)
        for ax in self.axes.flat:
            ax.set_visible(True)
        self._zoomed = False

    def on_click(self, event):
        if event.inaxes is None:
            return
        if self._zoomed:
            self.unzoom(event.inaxes)
        else:
            self.zoom(event.inaxes)
        self.fig.canvas.draw()
    
    def on_move(self, event):
        visibility_changed = False
        for point, annotation, ax in points_with_annotation:
            should_be_visible = (point.contains(event)[0] == True)
            if should_be_visible != annotation.get_visible():
                visibility_changed = True
                annotation.set_visible(should_be_visible)

        if visibility_changed:        
            self.fig.canvas.draw()



if __name__ == '__main__':
    main()