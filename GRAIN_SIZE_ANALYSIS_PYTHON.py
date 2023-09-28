
def Grain_analysis_algorithm(Weight_in_grams ):
    print("MONAHANS SAND ANALYSIS")
   
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
              
                          

Weight_in_grams = [ [7,3,6,9,175,261,3,7,4,3,5,5,7,4 ],  # MONAHANS SAMPLE A
                    [1,3,2,8,198,258,10,6,2,3,2,1,2,1],  # MONAHANS SAMPLE B
                    [3,2,3,14,190,253,4,5,4,5,3,4,3,3]] # MONAHANS SAMPLE C
              #     -1|0|1|1.25|2|2.5|2.75|3|3.25|3.5|3.75|4|4.5 : phi(Φ) scale size 
Grain_analysis_algorithm(Weight_in_grams )

  
