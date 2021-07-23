
import warnings

import matplotlib.pyplot as plt #module which plot 
import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec
import matplotlib as mpl
import pandas as pd
import numpy as np #basic module of python
import glob #module wich create list of strings of a directory
import sys
import os 
import shutil #module which moves files
import math #module which import mathematical packages
from astropy.table import Table, Column
from astropy.io import ascii
import matplotlib._layoutbox as layoutbox
import shutil 
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.ticker as tick
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#------------------
#Values asociated with columns in .txt 

column_1   = 0  #Index
column_2   = 1  #Start potential(V) = 0
column_3   = 2  #Upper vertex potential (V) =0.01
column_4   = 3  #Stop potential (V) = -1
column_5   = 4  #Lower vertex potential (V) =-0.01
column_6   = 5  #Scan rate (V/s) =0.01
column_7   = 6  #Step (V) =-0.00244
column_8   = 7  #Time (s)

column_9   = 8  #Potential applied (V)
column_10  = 9  #WE(1).Current (A)
column_11  = 10 #WE(1).Potential (V)
column_12  = 11 #Scan
column_13  = 12 #RPM
column_14  = 13 #ω (rad/s)

column_15   = 14  #Frequency
column_16   = 15  #Z'
column_17   = 16  #-Z''
column_18   = 17  #Z
column_19   = 18  #Phase
column_20   = 19  #Time
column_21   = 20  #Y'
column_22   = 21  #-Y''


#---------------------------------------------------------------------------------------
#Text remarks
input_delimiter= ";"
input_skip_space=2
#---------------------------------------------------------------------------------------
#Graphics remarks
color_list_N2 = ['black','red','blue'] #colors
label_list_N2=['0 rpm','1000 rpm','2000 rpm']#full list of rotatory electrode rpm values used in N2 analysis
color_list_O2 = ['black','red','blue',"green","orange","purple","yellow","gray","pink","brown"] #colors set for graphs
label_list_O2=['0 rpm','250 rpm','500 rpm','750 rpm','1000 rpm','1200 rpm','1400 rpm','1600 rpm','1800 rpm','2000 rpm']#full list of rotatory electrode rpm values used in O2 analysis
#---------------------------------------------------------------------------------------
#Output files remarks
fname_output_graf="ORR_graphs" #filename of ORR graph
format_plot= ".png" #format of ORR graph
#---------------------------------------------------------------------------------------
#List N2 & O2 files
path=os.getcwd() #get path of directory
files_N2 = glob.glob('N2*.txt') #list al the files which start with N2
print("List of N2 files loaded: " + str(files_N2)+ "\n")

files_O2 = glob.glob('O2*.txt') #list al the files which start with O2
files_O2_ordered=sorted(files_O2) #list al the files which start with O2 ordered
print("List of O2 files loaded ordered are : " + str(files_O2_ordered))
#---------------------------------------------------------------------------------------
#rpm list used in the ORR experiment
rpms=[0,250,500,750,1000,1200,1400,1600,1800,2000]
#---------------------------------------------------------------------------------------
#Reference to RHE 
#Our electrode is Ag/AgCl (1M KCl)
# E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
#Eo(Ag/AgCl) = 0.1976 V at 25ºC
#E(Ag/AgCl) = Working potential = Ag/AgCl (1M KCl) +0.235
#E(Ag/AgCl) = Working potential = Ag/AgCl (3.5M KCl) +0.205
#pH = pH of solution
#pH = pH of solution of NaOH 12.8
# for more information: 
#http://www.consultrsr.net/resources/ref/refpotls3.htm
#http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
E_RHE_factor = [(0.059*(13))  +  0.205 ] # 0.972
#---------------------------------------------------------------------------------------
#Interpolated points in ORR graph 
x_new=[-0.200,-0.225,-0.250,-0.275,-0.300,-0.350,-0.400,-0.450,-0.500,-0.600,-0.700,-0.800] #point list interpolated in each rpm curve #point list interpolated in each rpm curve
#x_new_RHE=[ 0.772,0.747,0.722,0.697,0.672,0.622,0.572,0.522,0.472,0.372,0.272,0.172] #point list interpolated in each rpm curve #point list interpolated in each rpm curve for RHE 
x_new_RHE=[0.956,0.94,0.924,0.908,0.892,0.876,0.86,0.844,0.828,0.812,0.796,0.78]



Area_electrode=0.19625  #cm2


#---------------------------------------------------------------------------------------

#Functions modules

def new_directories(folder1,folder2):

    #This  function create new folders named as folder1 and folder2 in where will be stored figures and data separately and has been created 
    #by Gaspar Carrasco. gasparcarrascohuertas@gmail.com for contact


    folder_1= folder1 #folder 1
    folder_2= folder2 #folder 2
    path= os.getcwd() + "\\" #obtain path
    dir1 = path+folder_1  #'path_to_my_folder_1'
    dir2 = path+folder_2  #'path_to_my_folder_2'

    print(dir1)
    print(dir2)

    if not os.path.exists(dir1 and dir2): # if the directory does not exist
        os.makedirs(dir1 ) # make the directory 1
        os.makedirs(dir2)  # make the directory 2
    else: # the directory exists
        #removes all files in a folder
        for the_file in os.listdir(dir1 and dir2):
            file_path = os.path.join(dir1, the_file)
            file_path = os.path.join(dir2, the_file)
    print("-------------------------------------END CREATE NEW DIRECTORIES FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def removing_files_in_folder(folder1,folder2):

    #This  function remove every file in new folders named as folder1 and folder2  and has been created 
    #by Gaspar Carrasco. gasparcarrascohuertas@gmail.com for contact

    path= os.getcwd() + "\\" #Obtain path 
    folder_1= folder1 #folder 1
    folder_2= folder2 #folder 2

    list_files = os. listdir(path+folder1)  #list all the files in folder 1

    files_figures = glob.glob(path+folder1+ "/*") 
    for f in files_figures:  #for every file  file in folder 2 remove
     os.remove(f)  

    files_data = glob.glob(path+folder2+ "/*")
    for f in files_data:   #for every file  file in folder 2 remove
     os.remove(f) 

    print("-------------------------------------END REMOVING FILES IN FOLDERS FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
"""
def replace_dots_commas(imput,old_character,new_character):

    for file in imput:

        file_input = file    # Entrada
        file_output = file_input.replace('.txt', '_nocomas.txt')    # Salida, nuevo archivo

        finput = open(file, 'r')    # Leo el archivo de entrada
        foutput = open(file_output, 'w')    # Creo el archivo nuev

        ## Bucle que recorre linea a linea el archivo
        for line in finput:
            line_nocomas = line.replace(old_character, new_character)

            ## Escribo esta linea nueva en el archivo de salida
            foutput.write(line_nocomas)

        finput.close()
        foutput.close()
        print(file_output, 'GUARDADO!')
"""
#---------------------------------------------------------------------------------------
def O2_file_change_name(imput):

    #This  function change the name of O2 files in order to obtain ordered list in our directory and has been created by Gaspar Carrasco. gasparcarrascohuertas@gmail.com for contact

    for name_old in imput: #for every file in our O2 list 

        a=name_old[3:-7] # characters located between 3 and -7 position
        b = float(a) # convert characters selected to float
        c = '%04i' % b # add 0 up to 4 positions before numbers converted to float 
        print("The file name with 0 placed is: " + c)
        name_new= name_old.replace(a, c)
        print("Renamed file is: " + name_new)
        print(name_old, ' ------- ',   name_new)
        os.rename(name_old,name_new)
    print("-------------------------------------END CHANGE NAME OF OXYGEN FILES FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def electrochemical_parameteres(imput):
    """This function obtain electrochemical info of input analysis files performed in ORR experiments. Colum association must be set in equipment previously   
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact"""
    
    cycles= float(input("Introduce numer of scan to perform: ")) 

    for file in imput:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space)

        #------------------
        #Electrochemical info 

        start_potential = f[:1, column_2] #Define our column and position associated to start potential selected in equipment
        upper_vertex_potential = f[:1, column_3]  #Define our column and position associated to upper vertex potential  selected in equipment
        stop_potential = f[:1, column_4]  #Define our column and position associated to stop potential selected in equipment
        lower_vertex_potential = f[:1, column_5]  #Define our column and position associated to lower vertex potential selected in equipment
        scan_rate = f[:1, column_6]  #Define our column and position associated to scan rate selected in equipment
        step = f[:1, column_7]  #Define our column and position associated to analysis step selected in equipment
        cycle_selected= f[:1, column_12] #Define our column and position associated to start cycle we have selected in equipment

        print("\n")
        print("Start potential is : " + str(start_potential) + "V")
        print("Upper_vertex_potential is: " + str(upper_vertex_potential) + "V")
        print("Stop potential is: " + str(stop_potential) + "V")
        print("Lower vertex potential is: " + str(lower_vertex_potential) + "V")
        print("Scan rate is: " + str(scan_rate)  + "V/seg")
        print("Step is: " + str(step)  + "V")
        print("Scan selected is : " + str(cycle_selected) )
        print("\n")
     
        #------------------
        #Operations with upper & lower vertex potential 
        rango=upper_vertex_potential-lower_vertex_potential
        print("Potential range scaned for 1 branch is : " + str(rango)+ "V")
        total_range=rango*2
        print("Potential range scaned for 2 branch is : " + str(total_range)+ "V")

        #------------------
        brach_values=rango
        step_values=brach_values/step
        print("Step values for one brach are : " + str(step_values) + " positions") # This value is the number of calculated positions (a.u.) in one branch based on step value selected
        print("Step values for both branches are : " + str(step_values*2) + " positions") # This value is the number of calculated positions (a.u.) in both branches based on step value selected

        #------------------
        #Analysis time  (seg)
        #------------------
        interval_scan_time=step/scan_rate
        print("Interval time : " + str(interval_scan_time)+ "seg")
        branch_time=rango/scan_rate
        print("Time spend in measuring one brach is : " + str(branch_time) + "seg")
        time_both_braches=branch_time*2
        print("Scan time  " + str(cycle_selected) + " is : " + str(time_both_braches) + "seg")
        time_analysis=(branch_time*2)*cycles
        print("Time used for  " + str(cycles) + " is : " + str(time_analysis) + "seg")
        print("\n")

    print("-------------------------------------END ELECTROCHEMICAL PARAMETERS FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------  
def plot_LSV(imput,color1,label1, plot_out):
    """ This function plot Nitrogen files listed
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """
    n=0 #counter
    for file in imput:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput

        """
        Index = f[:, column_1] #Define our column associated to index 
        start_potential = f[:, column_2] #Define our column associated to start potential selected in equipment
        upper_vertex_potential= f[:, column_3] #Define our column associated to upper vertex potential selected in equipment
        stop_potential = f[:, column_4] #Define our column associated to stop potential selected in equipment 
        lower_vertex_potential = f[:, column_5] #Define our column associated to lower vertex potential selected in equipment
        scan_rate = f[:, column_6] #Define our column associated to scan rate selected in equipment 
        step = f[:, column_7] #Define our column associated to step selected in equipment
        time = f[:, column_8] #Define our column associated to time in equipment
        potential_applied = f[:, column_9] #Define our column associated to potential applied 
        """
        WE_current = f[:360, column_10] #Define our column associated to Working electrode current (A) performed in equipment
        WE_current_corrected=(WE_current*1000000)/Area_electrode # this line converse amperes(A) to microamperes(microA) and divided in area to convert to current density
        WE_potential = f[:360, column_11] #Define our column associated to Working electrode potential (V) performed in equipment

        Scan = f[:, column_12] #Define our column associated to Scan performed in equipment

        rpm= f[:, column_13] #Define our column associated to revolutions per minute set in rotatory electrode  
        w= f[:, column_14] #Define our column associated to angular speed (rad/seg)

        ###############################################################################
        #Reference to RHE 
        #Our electrode is Ag/AgCl (1M KCl)
        # E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
        #Eo(Ag/AgCl) = 0.1976 V at 25ºC
        #E(Ag/AgCl) = Working potential = Ag/AgCl (1M KCl) +0.235
        #E(Ag/AgCl) = Working potential = Ag/AgCl (3M KCl) +0.205
        #pH = pH of solution
        #pH = pH of solution of NaOH 12.8
        # for more information: 
        #http://www.consultrsr.net/resources/ref/refpotls3.htm
        #http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
        E_RHE = WE_potential + (0.059*(13))  +  0.205 

        #If the number in y-axe is so large we can use this function

        def y_fmt(tick_val, pos):
            if tick_val > 10000:
                val = int(tick_val)/10000
                return '{:d} M'.format(val)
            elif tick_val > 1000:
                val = int(tick_val) / 1000
                return '{:d} k'.format(val)
            else:
                return tick_val


        plt.plot(E_RHE, WE_current_corrected,color=color1[n],label=label1[n]) #plot 
        n=n+1 #counter +1 


    plt.title( " \n Linear sweep voltammetry") #graph title
    plt.legend(loc='upper right', prop={'size':12}) #graph legend
    plt.xlim(0,1.6)   #X axis limit
    plt.ylim(-6000,10)  #Y axis limit 
    #plt.yaxis.set_major_formatter(tick.FuncFormatter(y_fmt))
    plt.xlabel(' E vs. RHE ( V) ') #X axis label
    #ax.plt.ylabel(' WE Current (\u00B5A) ') #Y axis label
    plt.ylabel(("Current density (\u00B5A x  " ) + str((r"$cm^{2}$ (rad/s) "))) #Y axis label




    plt.grid() #graph grid
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    shutil.move(plot_out,  "figures")
    plt.clf()
    print("-------------------------------------END PLOT LSV FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------    
def plot_EIS_Nyquist_N2(imput,color1,label1,graph_title, plot_out):
    """ This function plot Nitrogen files listed
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """
    n=0 #counter
    fig, (ax) = plt.subplots()
    for file in imput:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput

        Frequency = f[:, column_15] #Define our column associated to frequency
        Z_dev = f[:, column_16] #Define our column associated to Z'
        Z_doubledev_neg = f[:, column_17] #Define our column associated to -Z''
        Z = f[:, column_18] #Define our column associated to Z
        Phase = f[:, column_19] #Define our column associated to Phase
        Time = f[:, column_20] #Define our column associated to Time
        Y_dev = f[:, column_21] #Define our column associated to Y'
        Y_doubledev_neg = f[:, column_22] #Define our column associated to -Y'

        ax.plot(Z_dev, Z_doubledev_neg,color=color1[n],label=label1[n]) #plot 
        ax.set_title( graph_title + " \n Nyquist plot ") #graph title
        ax.set_xlim(0,5000)  # X axis limits 
        ax.set_ylim(0,6000)  # Y axis limits 
        ax.legend(loc='upper right', prop={'size':12}) #graph legend
        ax.set_xlabel(' Z  ( \u03A9)') #X axis label
        ax.set_ylabel(' -Z´´  ( \u03A9)') #Y axis label
        ax.grid()

        #-------------inset-------------
        axins = inset_axes(ax, width="50%", height="50%", loc=4)
        axins.plot(Z_dev, Z_doubledev_neg,color=color1[n],label=label1[n])
        axins.set_xlim(20,50)  # X axis limits 
        axins.set_ylim(0,5)  # Y axis limits 
        axins.tick_params(labelleft=True, labeltop=True,labelbottom=False)
        axins.grid() #graph grid

        #-------------Local minimum ----------------
        x1=(0) #Starting value of interval
        x2=(100) #End value of interval
        np.warnings.filterwarnings('ignore')
        i_interval_min = np.where( (Z_dev < x2) & (Z_dev > x1) )[0] #interval with x value
        x_interval_min = Z_dev[i_interval_min]#X value in interval
        y_interval_min = Z_doubledev_neg[i_interval_min]#Y value in interval
        min_y = np.min( y_interval_min )
        index = np.where(y_interval_min == min_y)[0]  # array of positions where y is the ymin
        min_x = x_interval_min[index]   ## xmin is the value of x which fits ymin
        print("Minimum value of x  0rpm is : " + str(min_x) +" ( \u03A9)")

        n=n+1 #counter +1 

    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    shutil.move(plot_out,  "figures")
    plt.clf()

    print("-------------------------------------END PLOT NYQUIST N2 FUNCTION---------------------------------------------------")

def plot_EIS_Nyquist_O2(imput,graph_title, plot_out):
    """ This function plot Nitrogen files listed
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """
    n=0 #counter
    fig, (ax) = plt.subplots()

    f1 = np.genfromtxt(files_O2[0], delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput
    f2 = np.genfromtxt(files_O2[7], delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput
    
    Z_dev1 = f1[:, column_16] #Define our column associated to Z'
    Z_doubledev_neg1 = f1[:, column_17] #Define our column associated to -Z''
    
    Z_dev2 = f2[:, column_16] #Define our column associated to Z'
    Z_doubledev_neg2 = f2[:, column_17] #Define our column associated to -Z''


    ax.plot(Z_dev1, Z_doubledev_neg1,color="black",label="0 rpm") #plot
    ax.plot(Z_dev2, Z_doubledev_neg2,color="gray",label="1600 rpm") #plot  
    ax.set_title( graph_title + " \n Nyquist plot ") #graph title
    ax.set_xlim(0,5000)  # X axis limits 
    ax.set_ylim(0,2000)  # Y axis limits 
    ax.legend(loc='upper right', prop={'size':12}) #graph legend
    ax.set_xlabel(' Z  ( \u03A9)') #X axis label
    ax.set_ylabel(' -Z´´  ( \u03A9)') #Y axis label
    ax.grid()


    #-------------inset-------------
    axins = inset_axes(ax, width="50%", height="50%", loc=4)
    axins.plot(Z_dev1, Z_doubledev_neg1,color="black",label="0 rpm")
    axins.plot(Z_dev2, Z_doubledev_neg2,color="gray",label="1600 rpm")
    axins.set_xlim(28,34)  # X axis limits 
    axins.set_ylim(0,2)  # Y axis limits 
    axins.tick_params(labelleft=True, labeltop=True,labelbottom=False)
    axins.grid() #graph grid


    n=n+1 #counter +1 

    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    shutil.move(plot_out,  "figures")
    plt.clf()


    #-------------Local minimum ----------------
    x1=(0) #Starting value of interval
    x2=(100) #End value of interval
    i_interval_min1 = np.where( (Z_dev1 < x2) & (Z_dev1 > x1) )[0] #interval with x value
    i_interval_min2 = np.where( (Z_dev2 < x2) & (Z_dev2 > x1) )[0] #interval with x value

    x_interval_min1 = Z_dev1[i_interval_min1]#X value in interval
    y_interval_min1 = Z_doubledev_neg1[i_interval_min1]#Y value in interval
    x_interval_min2 = Z_dev2[i_interval_min2]#X value in interval
    y_interval_min2 = Z_doubledev_neg2[i_interval_min2]#Y value in interval

    min_y1 = np.min( y_interval_min1 )
    index1 = np.where(y_interval_min1 == min_y1)[0]  # array of positions where y is the ymin
    min_x1 = x_interval_min1[index1]   ## xmin is the value of x which fits ymin

    min_y2 = np.min( y_interval_min2 )
    index2 = np.where(y_interval_min2 == min_y2)[0]  # array of positions where y is the ymin
    min_x2 = x_interval_min2[index2]   ## xmin is the value of x which fits ymin

    print("Minimum value of x  0rpm is : " + str(min_x1) +" ( \u03A9)")
    print("Minimum value of y 1600rpm is: " + str(min_y1)+" ( \u03A9)")

    print("Minimum value of x 1600rpm is : " + str(min_x2) +" ( \u03A9)")
    print("Minimum value of y 1600rpm is: " + str(min_y2)+" ( \u03A9)")


    print("-------------------------------------END PLOT NYQUIST O2 FUNCTION---------------------------------------------------")

def plot_EIS_Bode_phase_modulus_N2(imput,color1,label1,graph_title, plot_out):
    """ This function plot Nitrogen files listed
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """
    n=0 #counter
    fig, ax1 = plt.subplots()
    for file in imput:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput


        Frequency = f[:, column_15] #Define our column associated to frequency
        Z_dev = f[:, column_16] #Define our column associated to Z'
        Z_doubledev_neg = f[:, column_17] #Define our column associated to -Z''
        Z = f[:, column_18] #Define our column associated to Z
        Phase = f[:, column_19] #Define our column associated to Phase
        Phase_positive= Phase*(-1)
        Time = f[:, column_20] #Define our column associated to Time
        Y_dev = f[:, column_21] #Define our column associated to Y'
        Y_doubledev_neg = f[:, column_22] #Define our column associated to -Y'

        #----------------------------
        
        ax1.plot(Frequency, Z,color=color1[n],label=label1[n])
        ax1.set_ylim(10,100000)  # we already handled the x-label with ax1
        ax1.set_xlim(0.1,100000000)  # we already handled the x-label with ax1
        ax1.legend(loc='upper right', prop={'size':12}) #graph legend
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

        ax2.plot(Frequency, Phase_positive,color=color1[n])
        ax2.set_ylim(-90,0)  # we already handled the x-label with ax1

        n=n+1 #counter +1 
        #----------------------------
    ax1.set_xlabel('Frequency  ( Hz)')
    ax1.set_xscale('log')
    ax1.set_ylabel('Z ( \u03A9)', color="blue")
    ax1.tick_params(axis='y', labelcolor="blue")
    ax1.set_yscale('log')
    ax2.set_ylabel('Phase \N{DEGREE SIGN}', color="red")  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor="red")
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    plt.title( graph_title + " \n Bode plot") #graph title
    ax1.grid() #graph grid
    ax2.grid() #graph grid
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    shutil.move(plot_out,  "figures")
    plt.clf()
    print("-------------------------------------END PLOT BODE FUNCTION---------------------------------------------------")

def plot_EIS_Bode_phase_modulus_O2(imput,graph_title, plot_out):
    """ This function plot Nitrogen files listed
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """
    n=0 #counter
    fig, ax1 = plt.subplots()

    f1 = np.genfromtxt(files_O2[0], delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput
    f2 = np.genfromtxt(files_O2[7], delimiter=input_delimiter, skip_header=input_skip_space) #array of each file listed in imput


    Frequency1 = f1[:, column_15] #Define our column associated to frequency
    Z1 = f1[:, column_18] #Define our column associated to Z
    Phase1 = f1[:, column_19] #Define our column associated to Phase
    Phase_positive1= Phase1*(-1)

    Frequency2 = f2[:, column_15] #Define our column associated to frequency
    Z2 = f2[:, column_18] #Define our column associated to Z
    Phase2 = f2[:, column_19] #Define our column associated to Phase
    Phase_positive2= Phase2*(-1)

    #----------------------------
        
    ax1.plot(Frequency1, Z1,color="black",label="0 rpm")
    ax1.plot(Frequency2, Z2,color="gray",label="1600 rpm")

    ax1.set_ylim(10,100000)  # we already handled the x-label with ax1
    ax1.set_xlim(0.1,100000000)  # we already handled the x-label with ax1
    ax1.legend(loc='upper right', prop={'size':12}) #graph legend
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    ax2.plot(Frequency2, Phase_positive2,color="black")
    ax2.plot(Frequency2, Phase_positive2,color="gray")
    ax2.set_ylim(-90,0)  # we already handled the x-label with ax1

    #----------------------------
    ax1.set_xlabel('Frequency  ( Hz)')
    ax1.set_xscale('log')
    ax1.set_ylabel('Z ( \u03A9)', color="blue")
    ax1.tick_params(axis='y', labelcolor="blue")
    ax1.set_yscale('log')
    ax2.set_ylabel('Phase \N{DEGREE SIGN}', color="red")  # we already handled the x-label with ax1
    ax2.tick_params(axis='y', labelcolor="red")
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    plt.title( graph_title + " \n Bode plot") #graph title
    ax1.grid() #graph grid
    ax2.grid() #graph grid
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    shutil.move(plot_out,  "figures")
    plt.clf()
    print("-------------------------------------END PLOT BODE FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def subtract(imput,plot_out,data_out):
    """This function subtract Nitrogen specific file to Oxigen specific file data
    The files we want to substract will be:

    O2_0rpm - N2_0rpm

    O2_250rpm - N2_1000rpm
    O2_500rpm - N2_1000rpm
    O2_750rpm - N2_1000rpm
    O2_1000rpm - N2_1000rpm

    O2_1200rpm - N2_2000rpm
    O2_1400rpm - N2_2000rpm
    O2_1600rpm - N2_2000rpm
    O2_2000rpm - N2_2000rpm

    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact"""
    #---------------------------------------------------------------------------------------
    lista_datos_sustraidos = [ ]

    #------------------
    #Color lists
    #------------------
    color_list_O2_1 = ('black')  #colors
    color_list_O2_2 = ('red','blue',"green","orange") #colors
    color_list_O2_3 = ("purple","yellow","gray","pink","brown") #colors
    #------------------
    #Label lists  
    #------------------
    label_list_O2_1=('0 rpm')#values
    label_list_O2_2=('250 rpm','500 rpm',"750 rpm",'1000 rpm')#values
    label_list_O2_3=('1200 rpm','1400 rpm','1600 rpm','1800 rpm','2000 rpm')#modified #values
    #------------------
    #Counters 
    #------------------
    contador_0=0
    contador_1=0
    contador_2=0
    #------------------
    
    imput_N2_0rpm=np.genfromtxt("N2_0rpm.txt", delimiter=input_delimiter, skip_header=input_skip_space)
    WE_current_1 = imput_N2_0rpm[:360, column_10] #Define our column associated to Working electrode current (A) 
    WE_potential_1 = imput_N2_0rpm[:360, column_9] #Define our column associated to Working electrode potential (V)

    
    imput_N2_1000rpm=np.genfromtxt("N2_1000rpm.txt", delimiter=input_delimiter, skip_header=input_skip_space)
    WE_current_2 = imput_N2_1000rpm[:360, column_10] #Define our column associated to Working electrode current (A)
    WE_potential_2 = imput_N2_1000rpm[:360, column_9] #Define our column associated to Working electrode potential (V)


    imput_N2_2000rpm=np.genfromtxt("N2_2000rpm.txt", delimiter=input_delimiter, skip_header=input_skip_space)
    WE_current_3 = imput_N2_2000rpm[:360, column_10] #Define our column associated to Working electrode current (A)
    WE_potential_3 = imput_N2_2000rpm[:360, column_9] #Define our column associated to Working electrode potential (V)

    
    #--------Sustraccion O2_0000rpm - N2_0rpm-----------
    f = np.genfromtxt("O2_0000rpm.txt", delimiter=input_delimiter, skip_header=input_skip_space) #charge files O2_0rpm
    
    WE_current = f[:360, column_10] #WE_current 
    WE_potential = f[:360, column_9]
    WE_current_corrected=(WE_current*1000000)



    right_WE_current_corrected=WE_current-WE_current_1
    lista_datos_sustraidos.append(right_WE_current_corrected)
    t = Table(lista_datos_sustraidos)

    ###############################################################################
    #Reference to RHE 
    #Our electrode is Ag/AgCl (1M KCl)
    # E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
    #Eo(Ag/AgCl) = 0.1976 V at 25ºC
    #E(Ag/AgCl) = Working potential = Ag/AgCl (1M KCl) +0.235
    #E(Ag/AgCl) = Working potential = Ag/AgCl (3M KCl) +0.205
    #pH = pH of solution
    #pH = pH of solution of NaOH 12.8
    # for more information: 
    #http://www.consultrsr.net/resources/ref/refpotls3.htm
    #http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
    E_RHE = WE_potential + (0.059*(13))  +  0.205 



    plt.plot(E_RHE, (right_WE_current_corrected*1000000/Area_electrode),color='black',label='0 rpm')

    #--------Sustraccion O2_xrpm - N2_1000rpm-----------
    for file in imput[1:5]:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space) #charge files O2_250rpm; O2_500rpm; O2_750rpm; O2_1000rpm

        WE_current = f[:360, column_10] #WE_current 
        WE_potential = f[:360, column_9]
        right_WE_current_corrected=WE_current-WE_current_2

        lista_datos_sustraidos.append(right_WE_current_corrected)
        t = Table(lista_datos_sustraidos)

        ###############################################################################
        #Reference to RHE 
        #Our electrode is Ag/AgCl (1M KCl)
        # E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
        #Eo(Ag/AgCl) = 0.1976 V at 25ºC
        #E(Ag/AgCl) = Working potential = Ag/AgCl (3.5M KCl) +0.205
        #pH = pH of solution
        #pH = pH of solution of NaOH 12.8
        # for more information: 
        #http://www.consultrsr.net/resources/ref/refpotls3.htm
        #http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
        E_RHE = WE_potential + (0.059*(13))  +  0.205 


        plt.plot(E_RHE,(right_WE_current_corrected*1000000/Area_electrode),color=color_list_O2_2[contador_1],label=label_list_O2_2[contador_1])

        contador_1=contador_1+1 #modified

    for file in imput[5:]:

        f = np.genfromtxt(file, delimiter=input_delimiter, skip_header=input_skip_space) #charge files O2_1200rpm; O2_1400rpm; O2_1600rpm; O2_1800rpm; O2_2000rpm

        WE_current = f[:360, column_10] #WE_current 
        WE_potential = f[:360, column_9]


        right_WE_current_corrected=WE_current-WE_current_3
        lista_datos_sustraidos.append(right_WE_current_corrected)
        t = Table(lista_datos_sustraidos)
        t.write(data_out, format='ascii')

        ###############################################################################
        #Reference to RHE 
        #Our electrode is Ag/AgCl (1M KCl)
        # E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
        #Eo(Ag/AgCl) = 0.1976 V at 25ºC
        #E(Ag/AgCl) = Working potential = Ag/AgCl (1M KCl) +0.235
        #E(Ag/AgCl) = Working potential = Ag/AgCl (3M KCl) +0.205
        #pH = pH of solution
        #pH = pH of solution of NaOH 12.8
        # for more information: 
        #http://www.consultrsr.net/resources/ref/refpotls3.htm
        #http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
        E_RHE = WE_potential + (0.059*(13))  +  0.205 


        plt.plot(E_RHE, (right_WE_current_corrected*1000000/Area_electrode),color=color_list_O2_3[contador_2],label=label_list_O2_3[contador_2]) #color=color_list_O2_3[contador_2],label=label_list_O2_3[contador_2]

        contador_2=contador_2+1 #modified
    


    plt.xlabel(' E vs.RHE ( V) ') #X axis label
    #plt.ylabel(' WE Current (\u00B5A) ') #Y axis label
    plt.ylabel(("Current density (\u00B5A x  " ) + str((r"$cm^{2}$ (rad/s) "))) #Y axis label
    plt.title( "O2 substracted N2 \n Linear sweep voltammetry")
    plt.legend(loc='upper right', prop={'size':12}) #graph legend
    plt.xlim(0,1.6)   #X axis limit
    plt.ylim(-6000,10)  #Y axis limit 
    plt.grid() #graph grid
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    plt.clf()
    shutil.move(plot_out,  "figures")

    print("-------------------------------------END SUBSTRACT OXYGEN MINUS NITROGEN FILES FUNCTION---------------------------------------------------")

def matriz_substract_ordered(imput):

    imput_matriz = np.genfromtxt(imput, delimiter=" ", skip_header=1) 
    new_array = np.array(imput_matriz) #Array of valuew stored in data list
    tabla_1=Table(new_array)

    imput_2= np.genfromtxt("O2_0000rpm.txt", delimiter=input_delimiter, skip_header=input_skip_space)
    WE_potential = imput_2[:360, column_9]
    new_array_2= np.array(WE_potential)
    new_column=Column(new_array_2, name='WE_potential(V)')
    tabla_1.add_column(new_column, index=0)
    print(tabla_1)
    tabla_1.write("data_1_substract_oxygen_nitrogen_ordered_1.txt", format='ascii')

    imput_file = np.genfromtxt("data_1_substract_oxygen_nitrogen_ordered_1.txt", delimiter=" ", skip_header=1)
    array = np.array(imput_file) #Array of valuew stored in data list
    np.savetxt("data_1_substract_oxygen_nitrogen_ordered.txt", array) #Transpose array

    os.remove("data_1_substract_oxygen_nitrogen_ordered_1.txt")
    os.remove("data_1_substract_oxygen_nitrogen.txt")
    print("-------------------------------------END SUBSTRACT MATRIX ORDERED ---------------------------------------------------")
#---------------------------------------------------------------------------------------
def interpolate_points(data_imput,plot_out,data_out):

    """This function interpolate points x_new list and Y axis values. x_new list is defined the preamble and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    
    """
    rcParams.update({'figure.autolayout': False})
    new_file=open(data_out, "a+") #create new file name as  interpolación; format: .txt ; mode : append+
    data = [ ] #data list where data generated in for-loop will be stored 
    #------------------
    #Colours list
    #------------------
    color_list = ('black','red','blue',"green","orange","purple","yellow","gray","pink","brown") #colours for third part of graph
    #------------------
    #Labels list
    #------------------
    label_list_O2=('0 rpm','250 rpm','500 rpm','750 rpm','1000 rpm','1200 rpm','1400 rpm','1600 rpm',"1800 rpm",'2000 rpm')#labels for third part of graph
    #------------------
    #File
    file = np.genfromtxt(data_imput, delimiter=' ')
    #------------------
    #Counters 
    #------------------
    counter=0
    #------------------
    x = file[:, 0] #WE_potential 
    microA_factor=1000000
    ###############################################################################
    #Reference to RHE 
    #Our electrode is Ag/AgCl (1M KCl)
    # E(RHE) = E(Ag/AgCl) + 0.059*(pH) + Eo(Ag/AgCl)
    #Eo(Ag/AgCl) = 0.1976 V at 25ºC
    #E(Ag/AgCl) = Working potential = Ag/AgCl (1M KCl) +0.235
    #E(Ag/AgCl) = Working potential = Ag/AgCl (3M KCl) +0.205
    #pH = pH of solution
    #pH = pH of solution of NaOH 12.8
    # for more information: 
    #http://www.consultrsr.net/resources/ref/refpotls3.htm
    #http://www.consultrsr.net/resources/ref/refpotls.htm#ssce
    E_RHE_factor = [(0.059*(12.8))  +  0.205 ]


    for i in range(1, 11):

        y = file[:, i] #WE_current 
        y_corrected=y*microA_factor

        idx=np.argsort(x) #Arange values of vector in increasing order. VERY IMPORTANT!!!
        #print(x[idx])

        #Curve generated from substraction of Oxygen-Nitrogen curve 
        plt.plot(x[idx]+E_RHE_factor  , y[idx]*microA_factor/Area_electrode,color=color_list[counter],label=label_list_O2[counter])
        #----------------------
        yinterp = np.interp(x_new_RHE, x[idx]+E_RHE_factor , y[idx]) #Interpolate x_new list values in the curve amperios
        print(yinterp)
        plt.plot(x_new_RHE, yinterp*microA_factor/Area_electrode,".",color="red")
        #print("Shape of yiterp matrix is: " +str(yinterp.shape))
        #----------------------
        data.append(yinterp)  #Matrix generated will be stored in data list 
        counter=counter+1
    #---------------------------------------------------------------------------------------   

    new_array = np.array(data) #Array of valuew stored in data list
    np.savetxt(data_out, new_array.transpose()) #Transpose array
    #----------------------
    #Graphs remarks
    #----------------------
    plt.vlines(x_new_RHE, 100,-6000,color='k', linestyle='-') # vertical lines in interpolate X axis values; color black 
    plt.xlim(0,1.6)   #X axis limit
    plt.ylim(-6000,10)  #Y axis limit 
    plt.legend(loc='upper right', prop={'size':12}) #graph legend
    plt.xlabel(' E vs.RHE ( V) ') #X axis label
    #plt.ylabel(' WE Current (\u00B5A) ') #Y axis label
    plt.ylabel(("Current density (\u00B5A x  " ) + str((r"$cm^{2}$ (rad/s) "))) #Y axis label
    plt.title( " Reduction branch \n Linear sweep voltammetry") #graph title
    plt.grid() #graph grid
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    plt.clf()
    shutil.move(plot_out,  "figures")
    #----------------------
    new_file.close()
    print("-------------------------------------END INTERPOLATIONS OS POINTS IN LSV SUBSTRACTED GRAPH FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def Redox_peak(imput):

    """This function obtain electrochemical info , in particular REDOX peak of 0 rpm substracted analysis files performed in ORR experiments.  
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact"""



    f = np.genfromtxt(imput, delimiter=" ") #array of each file listed in impu
    WE_current = f[:350, 1] #Define our column associated to Working electrode current (A) performed in equipment
    WE_current_corrected=(WE_current*1000000)/Area_electrode # this line converse amperes(A) to microamperes(microA) and divided in area to convert to current density
    
    WE_potential = f[:350, 0] #Define our column associated to Working electrode potential (V) performed in equipment
    E_RHE = WE_potential + (0.059*(13))  +  0.205 



    #-------------Local minimum ----------------
    x1=(0) #Starting value of interval
    x2=(349) #End value of interval
    np.warnings.filterwarnings('ignore')
    i_interval_min = np.where( (E_RHE < x2) & (E_RHE > x1) )[0] #interval with x value
    x_interval_min = E_RHE[i_interval_min]#X value in interval
    y_interval_min = WE_current_corrected[i_interval_min]#Y value in interval
    min_y = np.min( y_interval_min )
    index = np.where(y_interval_min == min_y)[0]  # array of positions where y is the ymin
    min_x = x_interval_min[index]   ## xmin is the value of x which fits ymin
    print("Redox peak at 0 rpm is : " + str(min_x) +" V")
    np.savetxt("data_7_redox_peak_0rpm.txt", min_x) 
    print("-------------------------------------END REDOX PEAK FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def Add_index_data1(imput):

    df = pd.read_csv(imput, sep=" ")
    df.rename(index={0:'Index'})
    # changing columns using .columns() 
    df.columns = ['WE Potential ', 'col1', 'col2','col3','col4','col5','col6','col7','col8','col9','col10'] 
    # creating a list of dataframe columns 
    columns = list(df) 
    print(columns)

    color_list_O2 = ['black','red','blue',"green","orange","purple","yellow","gray","pink","brown"] #colors set for graphs
    label_list_O2=['0 rpm','250 rpm','500 rpm','750 rpm','1000 rpm','1200 rpm','1400 rpm','1600 rpm','1800 rpm','2000 rpm']#full list of rotatory electrode rpm values used in O2 analysis

    counter=0 #counter set to 0

    data_list_1=[] #empty data list
    data_list_2=[] #empty data list
    data_list_3=[] #empty data list
    data_list_4=[] #empty data list

    tabla = Table.from_pandas(df)
    microA_factor=1000000


    fname = "data_1_substract_oxygen_nitrogen_ordered.txt"
    num_lines = -1
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
    print("Number of lines:")
    print(num_lines)
    l = [i for i in range(num_lines)]
    print(l)
    new_column=Column(l, name="Index")
    tabla.add_column(new_column)
    print(tabla)
    tabla.write(imput, format='ascii',delimiter="\t", overwrite=True)

    print("---------------------------------------------------ADD INDEX TO  DATA ---------------------------------------------------")

def Halfwave_potential_reduction_branch(imput):
    #data_1_substract_oxygen_nitrogen_ordered


    #This  function plot all the reduction branch of scan rates performed in electrochemical surface area analysis  and has been created 
    #by Gaspar Carrasco. gasparcarrascohuertas@gmail.com for contact

    file = np.genfromtxt(imput, delimiter="\t", skip_header=1) #array of each file listed in imput




    microA_factor=1000000/Area_electrode

    data_list_1=[] #empty data list
    data_list_2=[] #empty data list
    data_list_3=[] #empty data list
    data_list_4=[] #empty data list
    data_list_5=[] #empty data list
    counter=0 #counter set to 0


    for i in range(1, 2):   ## For each file in files
        WE_current = file[:, i] #WE_current 
        WE_current_corrected=WE_current*microA_factor

        index=  file[:, 11] #Load from the file the column asociated to index (a.u.)
        #print(index)
        WE_potential = file[:, 0] #WE_potential 
        #print(WE_potential)
        E_RHE_factor = [(0.059*(12.8))  +  0.205 ]
        E_RHE = WE_potential + (0.059*(13))  +  0.205 

        
        #--------------------LINEAR REGRESSION--------------------------
        #we need to define two analysis ranges for the regression
        #---------FIRST-----------
        time1=0 #Start interval
        time2=3 #End interval
        i_interval_1 = np.where( (index< time2) & (index > time1) )[0] # defining interval
        x_interval_1 = E_RHE[i_interval_1] #Find in my interval values asociated to x (WE potential (V))
        y_interval_1 = WE_current_corrected[i_interval_1]#Find in my interval values asociated to y (WE current (microA))
        #print("x-interval 1 is:", x_interval_1)
        
        #---------SECOND-----------
        time3=0 #Start interval
        time4=3 #End interval
        i_interval_2 = np.where( (index < time4) & (index > time3) )[0] # defining interval
        x_interval_2 = E_RHE[i_interval_2]#Find in my interval values asociated to x (WE potential (V))
        y_interval_2 = WE_current_corrected[i_interval_2]#Find in my interval values asociated to y (WE current (microA))
        #print("x-interval  2 is:", x_interval_2)
        #print("y-interval  2 is:", y_interval_2)

        #---------LINEAR REGRESSION-----------
        
        adjust = np.polyfit(x_interval_2, y_interval_2, deg=1) # linealice the x-values and y-values of the interval to polynomial function order 1
        print("x-value and y-value fits the linear regression as A and B(x)= "+  str(adjust))

        
        y_adjust = np.polyval(adjust, x_interval_1) #applying the polynomial function which you got using polyfit
        #print(y_adjust)
        data_list_1.append(adjust)
        

        #--------------------FIND  MINIMUM--------------------------
        x1=(0) #Starting value of interval
        x2=(349) #End value of interval
        np.warnings.filterwarnings('ignore')
        i_interval_min = np.where( (E_RHE < x2) & (E_RHE > x1) )[0] #interval with x value
        x_interval_min = E_RHE[i_interval_min]#X value in interval
        y_interval_min = WE_current_corrected[i_interval_min]#Y value in interval
        min_y = np.min( y_interval_min )
        index = np.where(y_interval_min == min_y)[0]  # array of positions where y is the ymin
        min_x = x_interval_min[index]   ## xmin is the value of x which fits ymin
        text_min = (str(min_x)+ ";"+ str(min_y)+ "\n")
        print("Minimum x-value of function is:", min_x, "with y-value:", min_y)
        data_list_2.append(min_x) 
        data_list_3.append(min_y) 
        

        #--------------------FIND INTERSECTION MINIMUM--------------------------
        #we need to know the intersection between the linear regression and the x-minimum  value
        y_intersec = np.polyval(adjust, min_x)
        print("El valor de x en la intersección es " + str(min_x))
        print("El valor de y en la intersección es " + str(y_intersec))
        data_list_4.append(y_intersec) 
        print("----------------------------------------------------------------------------- " )

        
        #--------------------PLOTS--------------------------
        plt.vlines(min_x, -6000, 0,color='k', linestyle='--') # plot vertical lines in x-value for minimum from -100 to 100 color black
        plt.plot(min_x, y_intersec, 'Xr') #plot green point in the x-value for minimum and y-value for intersection 
        
        plt.plot(x_interval_1, y_adjust,'k',linestyle='--') #plot 
        plt.plot(x_interval_1, y_interval_1,'-',color='k',linewidth=1)
        plt.plot(E_RHE,WE_current_corrected,color=color_list_O2[counter],label=label_list_O2[counter]) #plot x-values for potential(V) and y-values for current(microA) 
        
        counter=counter+1
    
    #--------------------TABLES--------------------------
    data = (data_list_2,data_list_3,data_list_4) 
    data_array=np.array(data)
    tabla= Table(data_array.transpose(),names=('Min. in x ', 'Min. in y', 'Intersect. in y '))



    new_column=Column([0], name="RPM ")
    tabla.add_column(new_column)

    print("----------------------------------------------------------------------------- " )
    n=0
    for i in data_list_3:
        ipc=i-data_list_4[n]
        #print(ipc)
        data_list_5.append(ipc)
        n=n+1
    #print(data_list_5)
    new_column2=Column(data_list_5, name="ipc ")
    tabla.add_column(new_column2)
    print(tabla)

    
    #tabla.write("data_info_minimum", format='ascii',delimiter="\t", overwrite=True)

    #--------------------PLOTS OPTIONS--------------------------
    plt.xlabel(' E vs.RHE ( V) ') #X axis label
    plt.ylabel(("Current density (\u00B5A x  " ) + str((r"$cm^{2}$ (rad/s) "))) #Y axis label
    plt.title("Halfwave potential \n Cathodic current") # graph titl
    plt.legend(loc='upper right', prop={'size':12}) #graph legend
    plt.xlim(0,1.6)   #X axis limit
    plt.ylim(-6000,10)  #Y axis limit 
    #plt.grid() #graph grid
    #plt.show()
    plt.savefig("figure_anodic.png",overwrite=True)
    
    shutil.move("figure_anodic.png",  "figures")
    plt.clf()



    
    print("---------------------------------------------------END ECSA REDUCION BRANCH FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def Limiting_current_E_onset(imput):
    file = np.genfromtxt(imput, delimiter="\t", skip_header=1) #array of each file listed in imput

    microA_factor=1000000/Area_electrode
    counter=7

    for i in range(7, 8):   ## For each file in files
        WE_current = file[:, i] #WE_current 
        WE_current_corrected=WE_current*microA_factor
        index=  file[:, 11] #Load from the file the column asociated to index (a.u.)
        #print(index)
        WE_potential = file[:, 0] #WE_potential 
        #print(WE_potential)
        E_RHE_factor = [(0.059*(12.8))  +  0.205 ]
        E_RHE = WE_potential + (0.059*(13))  +  0.205 
        idx=np.argsort(WE_potential) #Arange values of vector in increasing order. VERY IMPORTANT!!!


        #--------------------FIND A VALUE FOR LIMITING CURRENT--------------------------
        desired_value_of_x = 0.2
        yinterp = np.interp(desired_value_of_x, E_RHE[idx], WE_current_corrected[idx]) #Interpolate x_new list values in the curve amperios
        print("Limiting current at 0.2 Volts vs RHE is:", yinterp)

                
        #--------------------FIND A VALUE FOR E_ONSET--------------------------
        desired_value_of_y = 100
        xinterp = np.interp(desired_value_of_y,  WE_current_corrected[idx],E_RHE[idx]) #Interpolate x_new list values in the curve amperios
        print(" E_ONSET for 0.1 mA / cm2  is:", xinterp)
        #----------------------------------------------

        plt.vlines(desired_value_of_x, -6000, 0,color='k', linestyle='--') # plot vertical lines in x-value for minimum from -100 to 100 color black
        plt.axhline(desired_value_of_y, 0, 1.6,color='k', linestyle='--') # plot vertical lines in x-value for minimum from -100 to 100 color black
        plt.plot(desired_value_of_x, yinterp, 'Xr') #plot green point in the x-value for minimum and y-value for intersection 
        plt.plot(xinterp, desired_value_of_y, 'Xr') #plot green point in the x-value for minimum and y-value for intersection 

        plt.plot(E_RHE,WE_current_corrected,color=color_list_O2[counter],label=label_list_O2[counter]) #plot x-values for potential(V) and y-values for current(microA) 
        counter=counter+1


    #--------------------PLOTS OPTIONS--------------------------
    plt.xlabel(' E vs.RHE ( V) ') #X axis label
    plt.ylabel(("Current density (\u00B5A x  " ) + str((r"$cm^{2}$ (rad/s) "))) #Y axis label
    plt.title("Limiting current \n Cathodic current") # graph titl
    plt.legend(loc='upper right', prop={'size':12}) #graph legend
    plt.xlim(0,1.6)   #X axis limit
    plt.ylim(-6000,200)  #Y axis limit 
    #plt.grid() #graph grid
    #plt.show()
    plt.savefig("figure_limiting_current.png",overwrite=True)
    
    shutil.move("figure_limiting_current.png",  "figures")
    plt.clf()

    print("---------------------------------------------------LIMITING CURRENT FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------

def radians(data_in_out): 

    #This  function ceate new document .txt from x_new list for operating   and has been created 
    #by Gaspar Carrasco. gasparcarrascohuertas@gmail.com for contact


    np.savetxt("data_3_revolutions.txt", rpms)

    lista=[0]
    n=0

    files_rpm = np.genfromtxt("data_3_revolutions.txt", delimiter=" ") 
    print("La lista de datos de revoluciones cargados son " + "\n" +str(files_rpm))   
    print("La dimensión de los datos de revoluciones son: ")
    print(files_rpm.shape)

    for valor in rpms[1:]:

        operacion=1/((valor*2*np.pi)/60)**0.5
        lista.append(operacion)


        n=n+1

    print("La lista de datos obtenidos para generar columna es" + "\n" +str(lista))    
    col_a= np.array(lista)

    #Me dice la dimensión del archivo col_new y de la nueva columna generada
    print("La dimensión de col_a es: ")
    print(col_a.shape)

    array = np.array((files_rpm,col_a))
    nueva_matriz= np.transpose(array)
    print(nueva_matriz)

    np.savetxt(data_in_out,nueva_matriz)

    #archivo_nuevo.close()
    print("-------------------------------------END RADIANS FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def table_operation(data_in,data_out):

    archivo_nuevo=open(data_out, "a+") #create new file name as  interpolación; format: .txt ; mode : append+
    array = np.genfromtxt(data_in, delimiter=" ") 
    print("La dimensión de los datos de revoluciones son: ")
    print(array.shape)

    operacion=(-1/(array*1000/(0.2)))

    t = Table(operacion)

    a=np.savetxt(data_out,operacion)
    #archivo_nuevo.close(data_out)

    print(t)
    print("-------------------------------------END TABLE OPERATION FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def transpose(data_in,data_out):

    """ This function tranpose matrix generated previously and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """

    archivo_nuevo=open(data_out, "a+") #create new file name as  interpolación; format: .txt ; mode : append+
    imput_intensidad_puntos = np.genfromtxt(data_in, delimiter=" ")
    transpuesta= np.transpose(imput_intensidad_puntos)
    
    a=np.savetxt(data_out,  transpuesta)
    #archivo_nuevo.close()
    print("-------------------------------------END TRANSPOSE MATRIX FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def K_L_plots(label1,plot_out, data_in_1,data_in_2):

    """ This function obtain Koutecký–Levich plots and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """

    imput_1 = np.genfromtxt(data_in_1, delimiter=" ")

    t=Table(imput_1)
    #print(t)
    """
    dat_col1 = t['col0'] #valores interpolados a -0.200 V
    dat_col2 = t['col1'] #valores interpolados a -0.225 V
    dat_col3 = t['col2'] #valores interpolados a -0.250 V
    dat_col4 = t['col3'] #valores interpolados a -0.275 V
    dat_col5 = t['col4'] #valores interpolados a -0.300 V
    dat_col6 = t['col5'] #valores interpolados a -0.350 V
    dat_col7 = t['col6'] #valores interpolados a -0.400 V
    dat_col8 = t['col7'] #valores interpolados a -0.450 V
    dat_col9 = t['col8'] #valores interpolados a -0.500 V
    dat_col10 = t['col9'] #valores interpolados a -0.600 V
    dat_col11 = t['col10'] #valores interpolados a -0.700 V
    dat_col12 = t['col11'] #valores interpolados a -0.800 V
    """

    #---------------------------------------------------------------------------------------
    imput_2 = np.genfromtxt(data_in_2, delimiter=" ", skip_header=0)

    col_1=0 #rpms
    col_2=1 #velocidad angular (w)

    rpm = imput_2[:, col_1] #rpms
    w = imput_2[:, col_2] #velocidad angular (w)

    n=0 #counter

    fig = plt.figure(constrained_layout=True)

    gs=gridspec.GridSpec(4,3, figure=fig) #filas -columnas

    for counter,colname in zip(gs,t.colnames):

        ax=plt.subplot(counter) ##constrained_layout is meant to be used with subplots() or GridSpec() and add_subplot(). --> constrained_layout=True ;   figsize=(3, 3) 

        col = t[colname]
        ax.plot(w, col,".")  #,label= label1[n]
        plt.xlabel( r"1/$w^\frac{1}{2}$ (rad/s) ")
        plt.ylabel(' 1/J ')
        #plt.title( " \n Koutecký–Levich plot " + str(n))
        ax.legend(loc='upper right', prop={'size':5})
        plt.xlim(0.05,0.3)  
        #plt.ylim(0,1)  
        plt.grid()
        
        n=n+1
        #plt.savefig(fname_output, format=format_plot,overwrite=True)

    #plt.subplots(constrained_layout=True)
    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    plt.clf()
    shutil.move(plot_out,  "figures")
    print("-------------------------------------END PLOTTING KOUTECKY-LEVICH CURVES FUNCTION---------------------------------------------------")
#---------------------------------------------------------------------------------------
def linealice(label1,plot_out,data_out,data_in_1,data_in_2):

    """ This function linealice Koutecký–Levich plots and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """

    parameters_list=[]

    imput_1 = np.genfromtxt(data_in_1, delimiter=" ")

    t=Table(imput_1)

    lista=[]
    n=0
    for colname in t.colnames[4:]:
        columnssss=t[colname]
        lista.append(columnssss)
        n=n+1
    #print(lista)
  
    #---------------------------------------------------------------------------------------
    imput_2 = np.genfromtxt(data_in_2, delimiter=" ", skip_header=0)

    col_1=0 #rpms
    col_2=1 #velocidad angular (w)
    rpm = imput_2[:, col_1] #rpms
    w = imput_2[:, col_2] #angular speed (w)

    n=0 #counter

    fig = plt.figure(constrained_layout=True)


    gs=gridspec.GridSpec(3,2, figure=fig) #filas -columnas

    for counter,column in zip(gs,lista):
        ax=plt.subplot(counter) #posicion
        #------------------
        #regression interval
        #------------------
        #print(col)
        w1=0 #start value of range
        w2=0.2 #end value of range
        i_interval = np.where( (w < w2) & (w > w1) )[0] #range of regresion
        x_interval = w[i_interval] #find in X axis the range of regresion
        y_interval = column[i_interval] #find in Y axis the range of regresion
        print("\n")
        #print("Estp es el intervalo de y " +str(y_interval))
        #print("Estp es el intervalo de x " +str(x_interval))
        #------------------
        #Linear regression
        #------------------
        adjust = np.polyfit(x_interval, y_interval, deg=1)  #x_interval= x values ; y_interval= y values with same X value ; deg = polynomial grad
        a = adjust[0] #pendiente
        b = adjust[1] #termino indep.
        #y_adjust = adjust[0]*x_interval + adjust[1]
        #y_adjust = adjust[0]*(x_interval ** 3) + adjust[1]*(x_interval **2) + adjust[2]*(x_interval) + adjust[3]
        y_adjust = np.polyval(adjust, x_interval) # adjust = polinomio ;  x_interval= número o  matriz de números en la que evaluar p .
        print("The slope of our linear system is    "+  str(a)+ "     and y-intercept is    "  + str(b))
        graph_parameters=(a,b)
        parameters_list.append(graph_parameters)
        plt.plot(x_interval, y_adjust,'k',linestyle='-') 
        #------------------
        #Regression coeficient
        #------------------
        x=w
        y =column
        slope, intercept = np.polyfit(x, y, 1)
        r_squared = 1 - (sum((y - (slope * x + intercept))**2) / ((len(y) - 1) * np.var(y, ddof=1)))
        print("Regression coeficient is:     "+  str(r_squared))
        #------------------

        ax.plot(w,column,".",label=label1[n])
        plt.xlabel( r"1/$w^\frac{1}{2}$  (rad/s) ")
        plt.ylabel(' 1/J ')
        #plt.title( " \n Koutecký–Levich plot " + str(n))
        plt.legend(loc='upper right', prop={'size':10})
        plt.xlim(0.05,0.3)  
        #plt.ylim(0,1)  
        plt.grid()
        n=n+1 #counter + 1


    #plt.show()
    plt.savefig(plot_out, format="png",overwrite=True)
    plt.clf()
    shutil.move(plot_out,  "figures")
    a=np.savetxt(data_out,  parameters_list)
    #archivo_nuevo.close()
    print("-------------------------------------END LINEALICE KOUTECKY-LEVICH PLOTS FUNCTION---------------------------------------------------")
    print("\n")
#---------------------------------------------------------------------------------------
def electrons(data_in):

    """ This function obtain numer of electrons from slope of linealiced Koutecký–Levich plots and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """


    graph_parameters= np.genfromtxt(data_in, delimiter=" ")
    slope = graph_parameters[:, 0] #slope
    print("slope list is: " +str(slope))
    constant=((0.01)**(1/6))/(0.62*96485*(0.00139)*((0.000019)**(2/3)))
    print("Constant we use is : " +str (constant))
    counter=0
    electron_list=[]


    for value in graph_parameters:
        electrons=constant/value
        #print(electrons)
        electron_list.append(electrons)
        counter=counter+1
    
    col_electrons= np.array(electron_list)
    array_out= np.concatenate((col_electrons,graph_parameters), axis=1) #genera un nuevo array concatenando la nueva columna en posicion 1

    t = Table(array_out,names=('electrons', 'constant/y-intercept', 'slope', ' y-intercept'))
    print("\n")
    print(t)

    print("-------------------------------------END OBTAIN ELECTRONS FUNCTION---------------------------------------------------")
    print("\n")
#---------------------------------------------------------------------------------------
def move_data():

    """ This function move every data file .txt to folder data and
    has been created by Gaspar, gasparcarrascohuertas@gmail.com for contact
    """

    files = glob.glob(path+ "/data*.txt")
    print("Files in moved to directories are: "+str(files))
    for f in files:
     shutil.move(f, "data")
    print("-------------------------------------END MOVING DATA .TXT  FUNCTION---------------------------------------------------")



new_directories("figures", "data")
removing_files_in_folder("figures","data")
O2_file_change_name(files_O2)
electrochemical_parameteres(files_N2)
#replace_dots_commas(files_2, "\t", ";")
#replace_dots_commas(files_O2, "\t", ";")
plot_LSV(files_N2,color_list_N2, label_list_N2, "figure_1_nitrogen.png")
plot_LSV(files_O2_ordered,color_list_O2, label_list_O2, "figure_2_oxygen.png")
plot_EIS_Nyquist_N2(files_N2,color_list_N2, label_list_N2,"Nitrogen", "figure_11_nitrogen_EIS.png")
plot_EIS_Nyquist_O2(files_O2,"Oxygen", "figure_12_oxygen_EIS.png")
plot_EIS_Bode_phase_modulus_N2(files_N2,color_list_N2, label_list_N2, "Nitrogen","figure_11_nitrogen_EIS_bode.png")
plot_EIS_Bode_phase_modulus_O2(files_O2,"Oxygen", "figure_12_oxygen_EIS_bode.png")
subtract(files_O2_ordered,"figure_3_substracted_oxygen_nitrogen.png","data_1_substract_oxygen_nitrogen.txt")
matriz_substract_ordered("data_1_substract_oxygen_nitrogen.txt")
interpolate_points("data_1_substract_oxygen_nitrogen_ordered.txt","figure_4_interpolated_graph.png","data_2_interpolation.txt")
Redox_peak("data_1_substract_oxygen_nitrogen_ordered.txt")
Add_index_data1("data_1_substract_oxygen_nitrogen_ordered.txt")
Halfwave_potential_reduction_branch("data_1_substract_oxygen_nitrogen_ordered.txt")
Limiting_current_E_onset("data_1_substract_oxygen_nitrogen_ordered.txt")


radians("data_3_revolutions.txt")
table_operation('data_2_interpolation.txt',"data_4_operation.txt")
transpose("data_4_operation.txt","data_5_operation_transpose.txt")
K_L_plots(x_new_RHE,"figure_5_K_L_plots.png","data_5_operation_transpose.txt","data_3_revolutions.txt")
linealice(x_new_RHE,"figure_6_linealiced_K_L_plots.png","data_6_K_L_plots_parameters.txt","data_5_operation_transpose.txt","data_3_revolutions.txt")
electrons("data_6_K_L_plots_parameters.txt")
move_data() 