# ---------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 6: Data Visualization
# Jacob Weikert
# Last Modified: 12.07.2017
# ---------------------------------------------------
# A program that utilizes pandas module to visualize
# data for the MSU assembled Pre-Disaster Mitigation
# Plan.
#
# Graph 1:
# Construction Class vs Fire Sprinklers.
#
# This graph can show a correlation between the construction classes of buildings
# and if they are more of a fire hazard then other construction classes. It can be
# seen that H may be buildings made from a flammable material, where those of
# class F might be made from stone or brick. (Assuming the class determines the
# material the building is made from).
#
# Graph 2 :
# Pie Graph comparing the extra costs associated with the building enhancements.
#
# Compares the cost difference for certain upgrades. For example, the difference
# of cost making a building with Hazmat Risk High vs Hazmat Risk Low,or a
# building with Fire Sprinklers vs one without Fire Sprinklers. Then they are
# all compared on a pie graph, the ones with the higher percents are the ones
# that cost more to build when that particular upgrade is added.
#
# HONORS ENHANCEMENT: 
# Graph 3: Building Size (Nearest 1000 ft**2) vs Building Value (Nearest $100,000)
#
# Was a third graph using a scatter plot to show the correlation between the size
# of a building to the cost. This can be analyzed to save construction costs of
# buildings in future.
# ---------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
import matplotlib 

df = pd.read_csv('buildings.csv')

#--------------------------------------------------------------------------------  
# Graph 1, Construction Class (materials of the exterior), vs Fire Sprinklers.

def graph_1():
    df['num_yes'] = df['Fire Sprinklers'] == 'Y' # Creates T/F column for Y=True and N=False
    df['num_no'] = df['Fire Sprinklers'] == 'N' # "..." for N=True and Y=False
    
    yes = df.groupby('Construction Class').num_yes.sum() # Counts Trues dependent on construction class
    no = df.groupby('Construction Class').num_no.sum() # Counts No's "..."
    
    const_class = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    value_yes = (6,13,17,2,1,0,0,1)  # Values obtained by equations above
    value_no = (13,9,24,30,3,1,2,0)  # Values obtained by equations above

    x_axis = np.arange(len(value_yes)) # Creates Numpy array with length = Num of construction classes
    width = .35 # width of bars

    plt.figure('CSCI 127, Program 6, Graph 1')
    bar_yes = plt.bar(x_axis, value_yes, width, color='g') # Plots bar_yes
    bar_no = plt.bar(x_axis + width, value_no, width, color = 'r') # Plots bar_no to right of bar_yes

    plt.xticks(x_axis+width /2, const_class) # Positions construction class labels in center of the 2 bars
    plt.xlabel('Construction Class') 
    plt.ylabel('Buildings with Fire Sprinklers')
    plt.title('Construction Class of Buildings Built with Fire Sprinklers')
    plt.legend((bar_yes[0], bar_no[0]),('Yes','No')) # first 1/2 of bar = bar_yes and 2nd half = bar_no
    
    return plt.show()

graph_1()

#--------------------------------------------------------------------------------       
# Graph 2, Pie Graph comparing the extra costs associated with the building enhancements.

def graph_2():
    
    def differences(name):
        """Calculates the difference of cost between buildings with upgrades and buildings without.
        For example, the difference of cost making a building with Hazmat Risk High vs Hazmat Risk Low,
        or a building with Fire Sprinklers vs one without."""
        
        df['price_per_sqft'] = df['Building Value'] // df['Square Feet']
        prices = df.groupby(name).price_per_sqft.mean()
        if name == 'Fire Sprinklers' or name == 'Historic Building':
            return (prices[1] - prices[0])
        elif name == 'Seismic Retrofit' or name == 'Backup Power':
            return (prices[2] - prices[0])
        else:
            return (prices[0] - prices[1])

    sprinkler = int(differences('Fire Sprinklers'))
    seismic = int(differences('Seismic Retrofit'))
    power = int(differences('Backup Power'))
    hazmat = int(differences('HazMat Risk'))
    historic = int(differences('Historic Building'))
    compare_all = (sprinkler, seismic, power, hazmat, historic)

    plt.style.use('dark_background')
    build_upgrade = ('Fire Sprinklers', 'Seismic Retrofit', 'Backup Power', 'HazMat Risk', 'Historic Building')
    colors = ('r','brown','orange','green','b')
    
    plt.figure('CSCI 127, Program 6, Graph 2, Showcases Which Enhancements are More Expensive')
    plt.title('Upgrades and Compared Cost Percentages')
    pie_chart = plt.pie(compare_all,
                        labels = build_upgrade,
                        colors=colors,
                        startangle = 90,
                        autopct='%1.1f%%')
    plt.axis('equal')
    return plt.show()   
graph_2()

#--------------------------------------------------------------------------------
#HONORS ENHANCEMENT:
# Graph 3, Building Size (Nearest 1000 ft**2) vs Building Value (Nearest $100,000)

def graph_3():
    value = df['Building Value'] // 100000
    sqr_ft = df['Square Feet'] // 1000
    
    plt.figure('CSCI 127, Program 6, Graph 3')
    plt.plot(sqr_ft, value, 'ro')
    plt.xlabel('Square Feet to the Nearest Thousand')
    plt.ylabel('Cost to the nearest $100,000')
    plt.title('Size vs Value for MSU Buildings')
    return plt.show()
    
graph_3()











