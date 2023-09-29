#Part 1: Carbonate in the Limestone, Sample 1
MassOfLimestone =2
MassOfContainerandHCL=144
FinalMassofContainerPlusContent=145.2
MassofCo2Released = MassOfContainerandHCL + MassOfLimestone - FinalMassofContainerPlusContent
# Moles = Mass/MolarMass, Co2 12 + (16x2) = 44
MolesOfC02Released = MassofCo2Released / 44
MolesCaCo3inLimestone = MolesOfC02Released * 100
PercentageCaCo3inLimestone = (MolesCaCo3inLimestone / MassOfLimestone)*100
print (MassofCo2Released)
print (MolesOfC02Released)
print (MolesCaCo3inLimestone)
print (PercentageCaCo3inLimestone)
print('#####################################################################################################################################################################')

##Part 2: Unknown Diprotic Acid
MassOfUnknown =0.406
InitVolumeOfNaOH = 0
FinalVolumeOfNaOH = 18
VolumeOfNaOHdispensed = (FinalVolumeOfNaOH - InitVolumeOfNaOH) / 1000
#Moles=Molarity(0.25 M Na0H) x Liter (volume)
MolesOfNaOHaddedatendpoint = 0.25 * VolumeOfNaOHdispensed
# 1 H2A (aq) + 2 NaH (aq) ->> 1 Na2A (aq) + 2 H20 (1) , 2 NaOH = 1 H2A
# 1:2 Ratio of Unknown Diprotic acid (H2A) : NaOH
MolesofH2A = MolesOfNaOHaddedatendpoint / 2
MolarMassofH2A = MassOfUnknown/ MolesofH2A
print (VolumeOfNaOHdispensed)
print (MolesOfNaOHaddedatendpoint)
print (MolesofH2A)
print (MolarMassofH2A)
print('#####################################################################################################################################################################')

## DIPROTIC ACID 

MassofKHPingrams = 1.007
#mass/molarmass=mole, molar mass of KPH = 204.22 g/mol
MoleofKPH = MassofKHPingrams/204.22
#Molarity, M of Na0H = 0.25, Molarity=Mole/liter, liter=Mole/Molarity, Volume=liter
# 1:1 ratio 1 KHC8H404 (ag) + 1 Na0H (ag) ->> 1 KNaC8H404 (ag) + 1 H20 (1)
MoleofNaOH = MoleofKPH
VolumeofNaOH = MoleofNaOH / 0.25
VolumeofNaOHinliter = VolumeofNaOH * 1000 # Liters to MilliLiters
InitVolumeNaOH = 0
FinalVolumeNaOH = 13.5 # in MilliLiters
VolumeofNaOHdispensed = FinalVolumeNaOH - InitVolumeNaOH
VolumeofNaOHdispensedinLiter = VolumeofNaOHdispensed / 1000
MolarityofNaOH = MoleofNaOH / VolumeofNaOHdispensedinLiter #Molarity, M=Mole/liter
print (MoleofKPH)
print (MoleofNaOH)
print (VolumeofNaOH)
print (VolumeofNaOHinliter)
print (VolumeofNaOHdispensed)
print (VolumeofNaOHdispensedinLiter)
print (MolarityofNaOH)
print('#####################################################################################################################################################################')


## Part 3: GAS LAWS
MassofZn = 0.21
VolumeofH2gasinMilliliters = 8
VolumeofH2gasinLiters = VolumeofH2gasinMilliliters / 1000 #1ML=0.001L
AtmosphericPressure = 0.977 #atm
WaterTemperatureinKelvin = 293 #13celsius + 217.15 kelvin
MolesofZnmetal = MassofZn / 65.38 #periodic table molar mass value
MolesofH2produced = MolesofZnmetal # 1 n(s)+2HCl(aq)-->> 1 H2+1ZnCl(aq) ,1 : 1 SIMILAR RATIO
PartialPressureofWater = 17.546/ 760 # 20 celsius=17.546 table in page 163, 1 atm=760 mmhg
PressureofH2gas = AtmosphericPressure - PartialPressureofWater # Patm - Pwater
ExperimentalR = (PressureofH2gas * VolumeofH2gasinLiters) / (MolesofZnmetal * WaterTemperatureinKelvin)
PercentageError= ((ExperimentalR - 0.0821) / 0.0821 )* 100 #0.08206 L.atm/Mol.K in Page 155
print(VolumeofH2gasinLiters)
print(MolesofZnmetal)
print(PartialPressureofWater)
print(PressureofH2gas)
print(ExperimentalR)
print(PercentageError)
print('#####################################################################################################################################################################')


## Part 4: Automobile Airbag
# PVT=RT, n=PV/RT, T=Temperature in Kelvin + 273.15
#P=Pressure, V=Volume, n=no. of moles, R= 0.0821 L.atm/mol.K ideal gas constant from last lab
P = 1 #atm, atmospheric pressure of the day in atm unit not mmHg
V = 3.78 # 1 LITER = 1000 MILLILITERS, VOLUME OF ZIPLOC BAG IN LITERS
R = 0.0821 #unit = L.atm/mol.K
T = 293.15 #Room temperature of the day from the Thermometer 20C + 273
n = (P * V) / (R * T) #n = no. of Moles of CO2
# 1 NaHC03 (s) + 1 HC2H302 (aq) = 1 NaC2H302 (aq) + 1 C02 (g) + 1 H20(1) ALL IN 1:1 RATIO
#MolesofC02 = MolesofBakingSoda = MolesofAceticAcid = MolesofWater
Moles = n
MolarMass = 84
Mass = Moles * MolarMass #Molar Mass of NaHC03 (s) = 84 g/mol, Moles = Mass/MolarMass
Molarity = 6 # 6M Acetic Acid
Volume = Moles / Molarity
print (n, 'Moles of C02,NaHC03 (s), HC2H302 (aq) , NaC2H302 (aq) ,H20(1) 1 to 1 ratio')
print (Mass, 'grams')
print (Volume,'Litres')
# * MEANS MULTIPLICATION, / MEANS DIVISION