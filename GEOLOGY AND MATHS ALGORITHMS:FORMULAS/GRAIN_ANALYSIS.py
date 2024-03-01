# Round x down to the nearest integer
def floor(x):
  rounded_down = x // 1
  return rounded_down 

# Round x up to the nearest integer      
def ceil(x):
  rounded_down = x // 1 + 1
  return rounded_down 
 
def percentile(N, percent, key=lambda x:x):
  percent = percent/100
  """
  Find the percentile of a list of values.

  @parameter N - is a list of values. Note N MUST BE already sorted.
  @parameter percent - a float value from 0.0 to 1.0.
  @parameter key - optional key function to compute value from each element of N.  

  @return - the percentile of the values
  """
  if not N:
    return None
  k = (len(N)-1) * percent
  f = floor(k)
  c = ceil(k)
  if f == c:
    return key(N[int(k)])
  d0 = key(N[int(f)]) * (c-k)
  d1 = key(N[int(c)]) * (k-f)
  return d0+d1

def Grain_analysis_algorithm(Weight_in_grams ):
    print("MONAHANS SAND ANALYSIS")
    TEMPE =  [[0] * len(Weight_in_grams[0])  for i in range( len(Weight_in_grams)  )    ]
   
    for y in range(len(Weight_in_grams)):
        print("\n")
        SAND5 = ["A:","B:","C:"]
        print("SAND", SAND5[y])
        print("\n")
        cumulative_sum = 0
        cummulative_percent_retained=0
        Finess_Modulus =0
        for x in range(len(Weight_in_grams[0])): 
            percent_retained = 0
            total_sum = 0
            for xx in range(len(Weight_in_grams[0])) : 
                total_sum += Weight_in_grams[y][xx] 
            for yy in range(y, y+1):       
                percent_retained +=  Weight_in_grams[yy][x]/total_sum * 100
                temp1 = [[0] * len(Weight_in_grams[0]) for _ in range(len(Weight_in_grams))]
            
                temp1[y][x] = percent_retained
                cumulative_sum += Weight_in_grams[yy][x]
                cummulative_percent_retained +=  temp1[yy][x]
                
                TEMPE[y][x] = cummulative_percent_retained
                
                temp2 = [[0] * len(Weight_in_grams[0]) for _ in range(len(Weight_in_grams))]
                temp2[y][x] = cummulative_percent_retained
                
                print(Weight_in_grams[y][x],"|",cumulative_sum,"CUMULATIVE SUM|",percent_retained,"% RETAINED |" , cummulative_percent_retained , "  CUMULATIVE % RETAINED |", 100 - cummulative_percent_retained , " %   FINER "," | FINESS MODULUS: ", Finess_Modulus)
              
            if (x<13 and y==yy):
                Finess_Modulus += temp2[y][x] /100.00
            if(x==13 and  y==yy and  Finess_Modulus <=2.2 ) :
                print("Very Fine Sand")
            if(x==13 and  y==yy and  Finess_Modulus >=2.2 and  Finess_Modulus <=2.6):
                print("Fine Sand")
            if(x==13 and  y==yy and  Finess_Modulus >=2.6 and  Finess_Modulus <=2.9):
                print("Medium Sand")
            if(x==13 and  y==yy and  Finess_Modulus >=2.9 and  Finess_Modulus <=3.2):
                print("Coarse Sand")
            if(x==13 and  y==yy and  Finess_Modulus >=6 and  Finess_Modulus <=6.9):
                print("20mm size of coarse aggregate")
            if(x==13 and  y==yy and  Finess_Modulus >=6.9 and  Finess_Modulus <=7.5):
                print("40mm size of coarse aggregate")
            if(x==13 and  y==yy and Finess_Modulus >=7.5 and  Finess_Modulus <=8):
                print("75mm size of coarse aggregate")
            if(x==13 and  y==yy and Finess_Modulus >=8 and  Finess_Modulus <=8.5):
                print("150mm size of coarse aggregate")
              
              #print(TEMPE)
    print()
    
    
    
    SANDZ = ['A','B','C']
    cnt = -1
    for rw in TEMPE:
      cnt +=1
    
      Graphic_Mean_a = ( percentile(rw, 16, key=lambda x:x)  + percentile(rw, 50, key=lambda x:x)  + percentile(rw, 84, key=lambda x:x) ) / 3
      
      #Graphic_Mean_a = ( np.percentile(a, 16) + np.percentile(a, 50) + np.percentile(a, 84)  )/ 3
      
      Inclusive_Graphic_Mean_a = (( percentile(rw, 84, key=lambda x:x) - percentile(rw, 16, key=lambda x:x)   )    / 4 )   +  (    ( percentile(rw, 95, key=lambda x:x) - percentile(rw, 5, key=lambda x:x)   )  / 6.6 ) 
      
      #Inclusive_Graphic_Mean_a = ( (np.percentile(a, 84) - np.percentile(a, 16))/ 4 )   +  ( (np.percentile(a, 95) - np.percentile(a, 5))/ 6.6 ) 
      
      Simple_Sorting_a = 0.5 *  ( percentile(rw, 95, key=lambda x:x) - percentile(rw, 5, key=lambda x:x) )
      #Simple_Sorting_a = 0.5 *  (np.percentile(a, 95) - np.percentile(a, 5))
      
      
      
      
      
      Inclusive_Sorting_Skewness_a = (       (percentile(rw, 84, key=lambda x:x) + percentile(rw, 16, key=lambda x:x) - (2 * percentile(rw, 50, key=lambda x:x) )       )  / (2 *(percentile(rw, 84, key=lambda x:x) - percentile(rw, 16, key=lambda x:x))      ) +   (       (percentile(rw, 95, key=lambda x:x) + percentile(rw, 5, key=lambda x:x) - (2 * percentile(rw, 50, key=lambda x:x) ))  / (2 *  (percentile(rw, 95, key=lambda x:x) - percentile(rw, 5, key=lambda x:x))))  )
      
      
      #Inclusive_Sorting_Skewness_a = (       (np.percentile(a, 84) + np.percentile(a, 16) - (2 * np.percentile(a, 50) )       )  / (2 *(np.percentile(a, 84) - np.percentile(a, 16))      ) +   (       (np.percentile(a, 95) + np.percentile(a, 5) - (2 * np.percentile(a, 50) ))  / (2 *  (np.percentile(a, 95) - np.percentile(a, 5))))  )
      
      Simple_Skewness_Measure_a = (percentile(rw, 95, key=lambda x:x) + percentile(rw, 5, key=lambda x:x) )  - (2 * percentile(rw, 50, key=lambda x:x))
      #Simple_Skewness_Measure_a = (np.percentile(a, 95) + np.percentile(a, 5) )  - (2 * np.percentile(a, 50))
      
      
      Graphic_Kurtosis_a = ( percentile(rw, 95, key=lambda x:x) - percentile(rw, 5, key=lambda x:x) ) /  (2.44 *  (percentile(rw, 75, key=lambda x:x) - percentile(rw, 25, key=lambda x:x)) )
      #Graphic_Kurtosis_a = ( np.percentile(a, 95) - np.percentile(a, 5) ) /  (2.44 *  (np.percentile(a, 75) - np.percentile(a, 25)) )
      
      
      print("MONAHANS SAND",SANDZ[cnt],":",end='\n')
      print("Graphic Mean:",Graphic_Mean_a,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_a,"||  Simple Sorting:",Simple_Sorting_a,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_a, "||   Simple Skewness Measure:",Simple_Skewness_Measure_a,"||  Graphic Kurtosis:",Graphic_Kurtosis_a)
      print(end='\n')
      
                          

Weight_in_grams = [ [7,3,6,9,175,261,3,7,4,3,5,5,7,4 ],  # MONAHANS SAMPLE A
                    [1,3,2,8,198,258,10,6,2,3,2,1,2,1],  # MONAHANS SAMPLE B
                    [3,2,3,14,190,253,4,5,4,5,3,4,3,3]] # MONAHANS SAMPLE C
              #     -1|0|1|1.25|2|2.5|2.75|3|3.25|3.5|3.75|4|4.5 : phi(Φ) scale size 
Grain_analysis_algorithm(Weight_in_grams )


"""
  MONAHANS SAND A:
  Graphic Mean: 64.91783567077333 ||  Inclusive Graphic Mean: 38.39199611239121 ||  Simple Sorting: 48.842685369625 ||  Inclusive Sorting Skewness: -0.8980258332837834 ||   Simple Skewness Measure: -86.10220441225002 ||  Graphic Kurtosis: 0.48371571468400776
  
  MONAHANS SAND B:
  Graphic Mean: 65.96646545918667 ||  Inclusive Graphic Mean: 39.55283214485091 ||  Simple Sorting: 49.637826962925 ||  Inclusive Sorting Skewness: -0.9505327322194678 ||   Simple Skewness Measure: -93.90342051785 ||  Graphic Kurtosis: 0.4713592418383512
  
  MONAHANS SAND C:
  Graphic Mean: 65.20833333293332 ||  Inclusive Graphic Mean: 39.182368035006064 ||  Simple Sorting: 49.3699596773 ||  Inclusive Sorting Skewness: -0.9161252360452901 ||   Simple Skewness Measure: -89.6471774176 ||  Graphic Kurtosis: 0.4827834350133382


"""