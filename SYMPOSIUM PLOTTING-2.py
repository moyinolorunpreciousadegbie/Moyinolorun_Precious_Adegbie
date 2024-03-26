#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'sales': [14, 16, 19, 22, 24, 25, 24, 24, 27, 30]})

df2 = pd.DataFrame({'year': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    'leads': [4, 4, 4, 5, 4, 5, 7, 8, 5, 3]})

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.year, df1.sales,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Year', fontsize=14)






#add y-axis label
ax.set_ylabel('Sales', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.year, df2.leads, marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Leads', color=col2, fontsize=16)


lis = list( range(10,110,10) )
ax2.set_xticks(df1.year)
ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])





plt.grid()


# In[ ]:


lis = list( range(10,110,10) )

#print( lis )






# # #################################################################

# # #################################################################

# 

# In[ ]:





# # QUATERNARY TO EARLY DEVONIAN

# In[44]:


TEMP =  [ 0, -0.05, -0.11, -0.16, -0.21, -0.27, -0.32, -0.37, -0.43, -0.48, -0.53, -0.59, -0.66, -0.73, -0.86, -1, -1.1, -1.2, -1.3, -1.42, -1.48, -1.52, -1.55, -1.58, -1.62, -1.64, -1.64, -1.64, -1.65, -1.66, -1.66, -1.53, -1.39, -1.29, -1.19, -1.07, -0.93, -0.8, -0.71, -0.59, -0.44, -0.32, -0.22, -0.12, -0.02, 0.09, 0.22, 0.32, 0.42, 0.52, 0.56, 0.59, 0.6, 0.6, 0.59, 0.57, 0.55, 0.53, 0.51, 0.5, 0.48, 0.44, 0.4, 0.35, 0.31, 0.26, 0.22, 0.15, 0.11, 0.08, 0.2, 0.54, 0.96, 1.41, 1.88, 2.31, 2.75, 3.21, 3.65, 4.1, 4.4, 4.43, 4.24, 4.04, 3.84,  3.64, 3.49, 3.25, 2.99, 2.84, 2.73, 2.54, 2.29, 2.04, 1.84, 1.6, 1.34, 1.1, 0.77, 0.65, 0.41, 0.37, 0.38, 0.39, 0.41, 0.42, 0.44, 0.45, 0.46, 0.48, 0.49, 0.47, 0.31, 0.18, 0.04, -0.12, -0.29, -0.43, -0.56, -0.76, -0.93, -1.05, -1.15, -1.23, -1.32, -1.44, -1.51, -1.62, -1.75, -1.88, -1.91, -1.91, -1.85, -1.73, -1.68, -1.57, -1.48, -1.4, -1.33, -1.27, -1.17, -1.12, -1.18, -1.22, -1.26, -1.3, -1.35, -1.39, -1.43, -1.47, -1.51, -1.57, -1.64, -1.7, -1.77, -1.84, -1.9, -1.98, -2.06, -2.13, -2.17, -2.24, -2.34, -2.41, -2.5, -2.6, -2.68, -2.74, -2.83, -2.89, -2.92, -2.77, -2.62, -2.4, -2.13, -1.9, -1.69, -1.43, -1.23, -0.99, -0.83, -0.81, -0.87, -0.93, -1, -1.07, -1.13, -1.19, -1.24, -1.29, -1.34, -1.39, -1.44, -1.49, -1.52, -1.56, -1.59, -1.62, -1.66, -1.68, -1.71, -1.73, -1.7, -1.67, -1.64, -1.6, -1.52, -1.44, -1.35, -1.26, -1.17, -1.08, -0.99, -0.9, -0.81, -0.72, -0.64, -0.55, -0.46, -0.37, -0.28, -0.19, -0.1, -0.01, 0.08, 0.18, 0.33, 0.4, 0.5, 0.6, 0.7, 0.8, 0.93, 1.04, 1.14, 1.24, 1.37, 1.51, 1.62, 1.74, 1.81, 1.87, 1.92, 1.97, 2.03, 2.08, 2.13, 2.17, 2.22, 2.26, 2.3, 2.32, 2.34, 2.36, 2.38, 2.4, 2.42, 2.44, 2.46, 2.47, 2.5, 2.9, 3.27, 3.67, 4.07, 4.47, 4.77, 5.15, 5.54, 5.94, 6.22, 6.08, 5.46, 4.67, 3.91, 3.18, 2.45, 1.68, 0.91, 0.15, -0.65, -1.15, -1.39, -1.56, -1.7, -1.85, -2.04, -2.19, -2.32, -2.47, -2.61, -2.76, -2.79, -2.83, -2.85, -2.87, -2.89, -2.93, -2.95, -2.97, -2.98, -2.9, -2.81, -2.73, -2.65, -2.54, -2.4, -2.28, -2.18, -2.08, -1.98, -1.88, -1.78, -1.65, -1.54, -1.44, -1.34, -1.24, -1.14, -1.06, -0.99, -1, -1.03, -1.08, -1.13, -1.18, -1.23, -1.3, -1.31, -1.32, -1.33, -1.34, -1.35, -1.37, -1.35, -1.3, -1.26, -1.22, -1.18, -1.15, -1.12, -1.14, -1.2, -1.28, -1.37, -1.46, -1.56, -1.66, -1.76, -1.86, -1.94, -1.9, -1.79, -1.66, -1.51, -1.37, -1.24, -1.14, -0.97, -0.87, -0.71, -0.63, -0.48, -0.31, -0.15, 0, 0.11, 0.21, 0.36, 0.53, 0.64, 0.67, 0.61, 0.58, 0.54, 0.49, 0.44, 0.43, 0.41, 0.4, 0.38, 0.37, 0.35, 0.34, 0.32, 0.31, 0.29, 0.28, 0.26, 0.24, 0.23, 0.21, 0.19, 0.13, 0.03, -0.01, -0.05, -0.11, -0.18, -0.25, -0.31]


print(len(TEMP))



# In[45]:


CO2 = [ 382.67, 368.86, 355.2, 340.43, 325.93,   314.2, 297.11, 277.02, 261.38, 246.77, 231.87, 223.25, 218.98, 228.32, 230.62, 234.09, 225.27, 224.14, 222.95, 230.86, 249.99, 271.65, 291.41, 278.56, 299.14, 338.87, 398.51, 459.77, 505.81, 579.65, 642.38, 689.87, 740.64, 792.39, 838.87, 863.49, 904.33, 938.16, 955.99, 959.43, 947.36, 924.89, 946.34, 953.23, 963.59, 955.61, 916.76, 892.44, 820.01, 762.5, 709.63, 645.43, 612.99, 570.28, 559.93, 530.88, 501.8, 472.14, 447.51, 428.41, 408.3, 389, 373.24, 319.07, 280.08, 251.39, 204.74, 240.95, 285.96, 335.83, 409.39, 478.89, 533.88, 578.83, 611.85, 634.92, 654.58, 663.22, 657.07, 641.95, 618.71, 586.24, 586.64, 591.23, 616.74, 658.46, 713.82, 735.84, 748.34, 750.07, 736.88, 724.33, 723.87, 715.58, 705.14, 717.01, 743.88, 779.34, 803.99, 821.98, 845.18, 867.78, 873.95, 858.03, 872.24, 827.89, 770.18, 731.01, 709.41, 709.96, 713.55, 704.15, 671.05, 689.97, 727.31, 761.73, 783.28, 805.12, 825.53, 838.02, 843.01, 820.09, 776.34, 713.58, 652.7, 637.69, 662.85, 673.71, 662.16, 640.9, 615.71, 647.46, 687.05, 753.32, 837.97, 901.6, 946.59, 989.81, 1015.55, 1013.48, 992.31, 959.51, 935.17, 927.11, 919.93, 907.15, 896.11, 888.65, 887.23, 894.96, 915.57, 953.44, 965.79, 945.58, 926.67, 918.02, 906.94, 892.8, 874.19, 887.91, 896.01, 930.89, 968.52, 1040.22, 1081.48, 1140.88, 1180.22, 1199.61, 1198.85, 1177.38, 1134.35, 1082.74, 1027.49, 973.81, 955.27, 927.83, 902.28, 889.39, 864.46, 867.36, 835.02, 815.42, 793.22, 831.87, 877.38, 943.09, 1020.58, 1102.36, 1181.92, 1224.32, 1230.65, 1295.63, 1343.96, 1333.73, 1293.89, 1242.2, 1200.63, 1191.52, 1128.6, 1018.63, 942.28, 914.03, 899.45, 893.09, 888.75, 879.55, 857.89, 815.46, 785.27, 824.33, 810.56, 796.26, 785.07, 795.98, 854.52, 893.98, 851.26, 785.06, 756.75, 736.17, 722.15, 713.48, 708.96, 707.37, 707.45, 707.95, 707.59, 718.46, 715.51, 713.23, 713.48, 734.48, 753.84, 726.92, 687.57, 640.89, 592.31, 547.65, 502.22, 457.6, 415.25, 376.5, 342.56, 314.51, 293.34, 279.88, 274.87, 278.9, 293.26, 318.67, 328.42, 335.58, 343.99, 352.87, 361.52, 369.36, 375.88, 380.65, 383.37, 383.84, 382.85, 379.74, 365.41, 333.09, 294.73, 260.93, 259.29, 286.29, 338.44, 434.02, 524.74, 637.83, 745.97, 833.22, 962.86, 1037.9, 1071.04, 1084.03, 1072.17, 1029.44, 950.99, 846.71, 739.34, 640.62, 560.66, 485.67, 415.68, 360.45, 273.07, 227.21, 169.76, 129.25, 144.24, 120.7, 127.94, 165.1, 213.19, 268.63, 327.6, 386.06, 439.68, 483.02, 510.84, 524.68, 520.59, 499.25, 459.03, 427.84, 382.62, 351.06, 335.72, 323.9, 318.97, 317.19, 316.19, 315.82, 315.9, 316.19, 316.4, 316.17, 315.11, 312.76, 306.5, 294.81, 281.69, 267.91, 254.33, 241.93, 227.24, 214.27, 206.76, 201.16, 197.54, 200.18, 210.27, 233.56, 267.45, 309.41, 356.92, 407.49, 458.66, 508, 553.1, 591.62, 621.19, 639.52, 644.31, 641.01, 630.86, 615.5, 596.92, 577.47, 559.86, 547.18, 534.5, 521.82, 509.14, 489.53, 467.32, 420.02, 396.25, 395.3, 420.55, 467.84, 533.04, 612, 700.57, 794.63, 890.04, 982.7, 1068.47, 1143.26, 1199.18, 1234.49, 1247.19, 1235.01, 1207.15, 1166.15, 1159.46, 1161.37, 1175.07, 1227.35, 1298.63, 1336.76, 1347.81, 1337.29, 1310.21, 1271.02, 1223.63, 1171.44, 1117.29, 1069.93, 1034.05, 1041.11, 1011.94, 1032.95, 1082.09, 1163.89, 1282.45, 1441.45, 1591.32         
      ]


print(len(CO2))


# In[46]:


AGE = list(   range(401)   )

#print( AGE )


# In[48]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE,
                    'CO2': TEMP })  ####

df2 = pd.DataFrame({'age': AGE ,
                    'temperature': CO2 }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('QUATERNARY TO EARLY DEVONIAN')


plt.grid()


# # NEOGENE

# In[51]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[2:23],
                    'CO2': TEMP[2:23] })  ####

df2 = pd.DataFrame({'age': AGE[2:23] ,
                    'temperature': CO2[2:23] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('NEOGENE')


plt.grid()


# # PALEOGENE

# In[53]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[24:66],
                    'CO2': TEMP[24:66] })  ####

df2 = pd.DataFrame({'age': AGE[24:66] ,
                    'temperature': CO2[24:66] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('PALEOGENE')


plt.grid()


# # CRETACEOUS 

# In[55]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[66:145],
                    'CO2': TEMP[66:145] })  ####

df2 = pd.DataFrame({'age': AGE[66:145] ,
                    'temperature': CO2[66:145] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('CRETACEOUS')


plt.grid()


# # JURASSIC

# In[57]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[145:199],
                    'CO2': TEMP[145:199] })  ####

df2 = pd.DataFrame({'age': AGE[145:199] ,
                    'temperature': CO2[145:199] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('JURASSIC')


plt.grid()


# # TRIASSIC

# In[62]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[199:250],
                    'CO2': TEMP[199:250] })  ####

df2 = pd.DataFrame({'age': AGE[199:250] ,
                    'temperature': CO2[199:250] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('TRIASSIC')


plt.grid()


# # PERMIAN

# In[61]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[250:298],
                    'CO2': TEMP[250:298] })  ####

df2 = pd.DataFrame({'age': AGE[250:298] ,
                    'temperature': CO2[250:298] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('PERMIAN')


plt.grid()


# # CARBONIFEROUS - PENNSYLVANIAN 

# In[60]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[298:318],
                    'CO2': TEMP[298:318] })  ####

df2 = pd.DataFrame({'age': AGE[298:318] ,
                    'temperature': CO2[298:318] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('CARBONIFEROUS - PENNSYLVANIAN')


plt.grid()


# # CARBONIFEROUS - MISSISSIPIAN

# In[64]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[318:359],
                    'CO2': TEMP[318:359] })  ####

df2 = pd.DataFrame({'age': AGE[318:359] ,
                    'temperature': CO2[318:359] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('CARBONIFEROUS - MISSISSIPIAN')


plt.grid()


# # DEVONIAN 

# In[66]:


import pandas as pd

#create DataFrames
df1 = pd.DataFrame({'age': AGE[359:401],
                    'CO2': TEMP[359:401] })  ####

df2 = pd.DataFrame({'age': AGE[359:401] ,
                    'temperature': CO2[359:401] }) ####

import matplotlib.pyplot as plt

#define colors to use
col1 = 'steelblue'
col2 = 'red'

#define subplots
fig,ax = plt.subplots()

#add first line to plot
ax.plot(df1.age, df1.CO2,marker='o',  color=col1)

#add x-axis label
ax.set_xlabel('Age [Ma]', fontsize=14)






#add y-axis label
ax.set_ylabel('Mean Termperature Anomaly [°C]', color=col1, fontsize=16)

#define second y-axis that shares x-axis with current plot
ax2 = ax.twinx()

#add second line to plot
ax2.plot(df2.age, df2.temperature , marker='x', color=col2)

#add second y-axis label
ax2.set_ylabel('Atmospheric CO2 [ppm]', color=col2, fontsize=16)


#lis = list( range(10,110,10) )

#lis


#ax2.set_xticks(df1.age)
#ax2.set_xticklabels(  lis )

#plt.legend(df2.leads, df1.sales, ["Leads", "Sales"])


plt.title('DEVONIAN')


plt.grid()


# In[ ]:




