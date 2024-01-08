import matplotlib.pyplot as plt
# Shawdi Keshavarz
def compounding_accumulation(k,nom_rate,t,m):
    i = nom_rate/m
    return round((k*((1+i)**t)),2)

print(compounding_accumulation(50000,.0675,5,1)) # number 1.C on problem set
print(compounding_accumulation(10000,.08,(78/6),2)) # number 3 on problem set

# Shawdi Keshavarz
y1_ticks= []
y1_tick = 1000
for x in range(24):
    y1_ticks.append(y1_tick)
    y1_tick += 100
    
# part a
x1=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028]
y1=[]
for year in x1:
    pres = 3500*((1-.0575)**(2029-year))
    pres = round(pres,2)
    y1.append(pres)
plt.xticks(x1,rotation="vertical")
plt.yticks(y1_ticks)
plt.scatter(x1,y1,color='red')
plt.show()

# part b monthly
x2 = list(reversed(range(1,252)))
y2=[]
i=.0575/(1-.0575)
for month in x2:
    pres = 3500*((1+i/12)**(-month*12))
    y2[:0]= [pres]
plt.scatter(x2,y2,color='blue')
plt.show()

# part b quarterly
x3 = list(reversed(range(1,84)))
y3=[]
i=.0575/(1-.0575)
for month in x3:
    pres = 3500*((1+i/4)**(-month*4))
    y3[:0]= [pres]
plt.scatter(x3,y3,color='yellow')
plt.show()