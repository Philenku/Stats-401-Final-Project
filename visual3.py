import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# EXTRACT DATA FOR THE VISUAL
df = pd.read_csv('extracted_data_vis3.csv')

# EXTRACT DRUG USAGE PER TIME
# The counts in these lists are exclusive, eg people who have used 
# drugs at the time of offence are not counted among those who used 
# drugs 12 months ago.
# 
# The order in the lists is: 
# now, 12 months ago, earlier than 12 months ago, never, don't know

def extract_values(df):
    m_now = df[(df['Marijuana'] == '(1) 1 = Yes')]
    m_12_months_ago = df[(df['Marijuana'] != '(1) 1 = Yes') & (df['Marijuana_12months']=='(1) 1 = Yes')]
    m_before_12_months = df[(df['Marijuana'] != '(1) 1 = Yes') & (df['Marijuana_12months']!='(1) 1 = Yes') \
            & (df['Marijuana_ever'] == '(1) 1 = Yes')]
    m_never = df[(df['Marijuana_ever'] == '(2) 2 = No')]
    m_unknown = df[(df['Marijuana_ever'] != '(1) 1 = Yes') & (df['Marijuana_ever']!='(2) 2 = No')]

    c_now = df[(df['Cocaine'] == '(1) 1 = Yes')]
    c_12_months_ago = df[(df['Cocaine'] != '(1) 1 = Yes') & (df['Cocaine_12months']=='(1) 1 = Yes')]
    c_before_12_months = df[(df['Cocaine'] != '(1) 1 = Yes') & (df['Cocaine_12months']!='(1) 1 = Yes') \
            & (df['Cocaine_ever'] == '(1) 1 = Yes')]
    c_never = df[(df['Cocaine_ever'] == '(2) 2 = No')]
    c_unknown = df[(df['Cocaine_ever'] != '(1) 1 = Yes') & (df['Cocaine_ever']!='(2) 2 = No')]

    h_now = df[(df['Heroin'] == '(1) 1 = Yes')]
    h_12_months_ago = df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']=='(1) 1 = Yes')]
    h_before_12_months = df[(df['Heroin'] != '(1) 1 = Yes') & (df['Heroin_12months']!='(1) 1 = Yes') \
            & (df['Heroin_ever'] == '(1) 1 = Yes')]
    h_never = df[(df['Heroin_ever'] == '(2) 2 = No')]
    h_unknown = df[(df['Heroin_ever'] != '(1) 1 = Yes') & (df['Heroin_ever']!='(2) 2 = No')]
    
    marijuana_values = [len(m_now), len(m_12_months_ago), len(m_before_12_months), len(m_never), len(m_unknown)]
    heroin_values = [len(h_now), len(h_12_months_ago), len(h_before_12_months), len(h_never), len(h_unknown)]
    cocaine_values = [len(c_now), len(c_12_months_ago), len(c_before_12_months), len(c_never), len(c_unknown)]
    
    annotate_marijuana_values = {
# heroin in the same period and cocaine in the same period
       'cocaine': [
            len(m_now[(m_now['Cocaine_ever']=='(1) 1 = Yes')]) / len(m_now) * 100,
            len(m_12_months_ago[(m_12_months_ago['Cocaine_ever']=='(1) 1 = Yes')]) / len(m_12_months_ago) * 100,
            len(m_before_12_months[(m_before_12_months['Cocaine_ever']=='(1) 1 = Yes')]) / len(m_before_12_months) * 100,
            len(m_never[(m_never['Cocaine_ever']=='(1) 1 = Yes')]) / len(m_never) * 100,
            len(m_unknown[(m_unknown['Cocaine_ever']=='(1) 1 = Yes')]) / len(m_unknown) * 100
       ],
        'heroin': [
            len(m_now[(m_now['Heroin_ever']=='(1) 1 = Yes')]) / len(m_now) * 100,
            len(m_12_months_ago[(m_12_months_ago['Heroin_ever']=='(1) 1 = Yes')]) / len(m_12_months_ago) * 100,
            len(m_before_12_months[(m_before_12_months['Heroin_ever']=='(1) 1 = Yes')]) / len(m_before_12_months) * 100,
            len(m_never[(m_never['Heroin_ever']=='(1) 1 = Yes')]) / len(m_never) * 100,
            len(m_unknown[(m_unknown['Heroin_ever']=='(1) 1 = Yes')]) / len(m_unknown) * 100
        ]     
    }
    print(annotate_marijuana_values)

    annotate_cocaine_values = {
# heroin in the same period and cocaine in the same period
       'marijuana': [
           len(c_now[(c_now['Marijuana_ever']=='(1) 1 = Yes')]) / len(c_now) * 100,
            len(c_12_months_ago[(c_12_months_ago['Marijuana_ever']=='(1) 1 = Yes')]) / len(c_12_months_ago) * 100,
            len(c_before_12_months[(c_before_12_months['Marijuana_ever']=='(1) 1 = Yes')]) / len(c_before_12_months) * 100,
            len(c_never[(c_never['Marijuana_ever']=='(1) 1 = Yes')]) / len(c_never) * 100,
            len(c_unknown[(c_unknown['Marijuana_ever']=='(1) 1 = Yes')]) / len(c_unknown) * 100
       ],
        'heroin': [
            len(c_now[(c_now['Heroin_ever']=='(1) 1 = Yes')]) / len(c_now) * 100,
            len(c_12_months_ago[(c_12_months_ago['Heroin_ever']=='(1) 1 = Yes')]) / len(c_12_months_ago) * 100,
            len(c_before_12_months[(c_before_12_months['Heroin_ever']=='(1) 1 = Yes')]) / len(c_before_12_months) * 100,
            len(c_never[(c_never['Heroin_ever']=='(1) 1 = Yes')]) / len(c_never) * 100,
            len(c_unknown[(c_unknown['Heroin_ever']=='(1) 1 = Yes')]) / len(c_unknown) * 100
        ]     
    }

    annotate_heroin_values ={
# heroin in the same period and cocaine in the same period
       'cocaine':  [
            len(h_now[(h_now['Cocaine_ever']=='(1) 1 = Yes')]) / len(h_now) * 100,
            len(h_12_months_ago[(h_12_months_ago['Cocaine_ever']=='(1) 1 = Yes')]) / len(h_12_months_ago) * 100,
            len(h_before_12_months[(h_before_12_months['Cocaine_ever']=='(1) 1 = Yes')]) / len(h_before_12_months) * 100,
            len(h_never[(h_never['Cocaine_ever']=='(1) 1 = Yes')]) / len(h_never) * 100,
            len(h_unknown[(h_unknown['Cocaine_ever']=='(1) 1 = Yes')]) / len(h_unknown) * 100
       ],
        'marijuana': [
            len(h_now[(h_now['Marijuana_ever']=='(1) 1 = Yes')]) / len(h_now) * 100,
            len(h_12_months_ago[(h_12_months_ago['Marijuana_ever']=='(1) 1 = Yes')]) / len(h_12_months_ago) * 100,
            len(h_before_12_months[(h_before_12_months['Marijuana_ever']=='(1) 1 = Yes')]) / len(h_before_12_months) * 100,
            len(h_never[(h_never['Marijuana_ever']=='(1) 1 = Yes')]) / len(h_never) * 100,
            len(h_unknown[(h_unknown['Marijuana_ever']=='(1) 1 = Yes')]) / len(h_unknown) * 100
       ]     
    }

    annotations = [annotate_marijuana_values, annotate_cocaine_values, annotate_heroin_values]
    return marijuana_values, heroin_values, cocaine_values, annotations


def get_annotation_string(annotations, cur_drug_index, people_count, cur_time_index):
    # annotation row contains two values, one for each other drug
    # cur_drug_index: 0 = marijuana, 1 = cocaine, 2 = heroin
    col = cur_time_index
    annotation_string = ''
    if cur_drug_index == 0:
        annotation_string = 'Count: ' + str(people_count) + '\n' + \
               'Cocaine users (ever): ' + str(round(annotations[0]['cocaine'][col], 2)) + '%' + '\n' + \
               'Heroin users (ever): ' + str(round(annotations[0]['heroin'][col], 2)) + '%' #+ '\n'
    
    elif cur_drug_index == 1:
        annotation_string ='Count: ' + str(people_count) + '\n' + \
               'Marijuana users (ever): ' + str(round(annotations[1]['marijuana'][col], 2)) + '%' + '\n' + \
               'Heroin users (ever): ' + str(round(annotations[1]['heroin'][col], 2)) + '%' #+ '\n'
    
    if cur_drug_index == 2:
        annotation_string ='Count: ' + str(people_count) + '\n' + \
               'Cocaine users (ever): ' + str(round(annotations[2]['cocaine'][col], 2)) + '%' + '\n' + \
               'Marijuana users (ever): '+ str(round(annotations[2]['marijuana'][col], 2)) + '%'# + '\n'
    
    return annotation_string


def func_annotations(ax, x, y, annotations, col , row, s):
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    arrow=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.2", fc="w")
    return ax.annotate(get_annotation_string(annotations, row, s, col),
        xy=(x, y), xycoords='data',
        xytext=(10, 10), textcoords='offset points',
        bbox=props, arrowprops=arrow
    )

# GLOBAL
points_with_annotation = list()

def survey(results, category_names, title, annotations):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*.
    category_names : list of str
        The category labels.
    """
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('magma')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())
    
    #points_with_annotation = list()
    annotation = None
    double_loop_j, double_loop_i = 0, 0
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        
        if double_loop_i == len(labels):
            double_loop_i = 0
            double_loop_j += 1

        for y, (x, c) in enumerate(zip(xcenters, widths)):
            point, = plt.plot(x, y, 'o', markersize=10)
            # annotating
            annotation = func_annotations(ax, x, y, annotations, double_loop_j, double_loop_i, c)
            annotation.set_visible(True)
            points_with_annotation.append([point, annotation])
            
            double_loop_i += 1
    
    on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)
    fig.suptitle(title)  
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax


def vis_all_prisoners():
    marijuana_values, heroin_values, cocaine_values, annotations = extract_values(df)
    category_names = ['Upon Commiting the Crime', '12 Months Prior', 'More Than 12 Months Prior', 'Never', "Unknown"]
    results = {
        'Marijuana': marijuana_values,
        'Cocaine': cocaine_values,
        'Heroin': heroin_values
    }
    return survey(results, category_names, 'Drug Usage Among All Prisoners', annotations)


def vis_female_prisoners():
    df_female = df[df['Sex']=='Female']

    fem_marijuana_values, fem_heroin_values, fem_cocaine_values, fem_annotations = extract_values(df_female)
    category_names = ['Upon Commiting the Crime', '12 Months Prior', 'More Than 12 Months Prior', 'Never', "Unknown"]
    results = {
        'Marijuana': fem_marijuana_values,
        'Cocaine': fem_cocaine_values,
        'Heroin': fem_heroin_values
    }
    return survey(results, category_names, 'Drug Usage Among Female Prisoners', fem_annotations)


def vis_male_prisoners():
    # CREATE VIS FOR MALE PRISONERS
    df_male = df[df['Sex']=='Male']

    male_marijuana_values, male_heroin_values, male_cocaine_values, male_annotations = extract_values(df_male)
    category_names = ['Upon Commiting the Crime', '12 Months Prior', 'More Than 12 Months Prior', 'Never', "Unknown"]
    results = {
        'Marijuana': male_marijuana_values,
        'Cocaine': male_cocaine_values,
        'Heroin': male_heroin_values
    }
    return survey(results, category_names, 'Drug Usage Among Male Prisoners', male_annotations)


def on_move(event):
    #print('on_move GETS CALLED')
    print(points_with_annotation)
    visibility_changed = False
    for point, annotation in points_with_annotation:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)

    if visibility_changed:        
        print('issue')
        plt.draw()

#plt.ioff()
#plt.clf()
fig1, ax1 = vis_all_prisoners()
fig2, ax2 = vis_female_prisoners()
fig3, ax3 = vis_male_prisoners()
#plt.ion()
#plt.ion()
plt.show()