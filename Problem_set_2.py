import pandas as pd
import numpy as np

# Shawdi Keshavarz
print("\nQuestion 1")
def find_interest(x: int, t:int):
    return round(((x**(1/t))-1),4)
# Class activity 4 problem 4: Find i, the annual rate of interest, such that an amount of money will triple itself over 16 years.
print("Is i for tripling itself after 16 years .0711?: " + str(find_interest(3,16)==.0711))
print("\n\n")
print("Question2")
data={'1/1':[200000, 0],
           '2/1':[195000, 3000],
           '5/1':[224000+2000, (-2000)],
           '6/1':[224500+1000, (-1000)],
           '8/1':[224000-4000, 4000],
           '10/1':[229500, 2500],
           '11/1':[233500+1500, (-1500)],
           '12/1':[238000, 0]}

df=pd.DataFrame(data, index=['Bt', 'Wt'])
print(df)

# Shawdi Keshavarz
col=1
i:int=1
while col < len(df.columns):
    sum = (df.iloc[:,(col-1)]).sum()
    b0 = df.iat[0,col]
    it = b0/sum
    i=i*it
    col += 1
    
print("time-weighted rate of return for 2022: " + str(round((i-1),4)))

# Shawdi Keshavarz
print("\nQuestion 3")
s1 = (650*(1.115**(2024-2018)))+(450*(1.115**(2024-2019)))+250

a = [[(14*(1.115**(2024-2019))), (35*(1.115**(2024-2022)))], [(21*(1.115**(2024-2023))), (29*(1.115**(2024-2020)))]]
b = [s1,s1]
answer= np.linalg.solve(a,b)
print("Matrix")

fullmatrix = np.c_[a,b]

print(np.matrix(fullmatrix))
print("[x,y] = " + str(answer))
print("x = " + str(round(answer[0],2)) + ", y = " + str(round(answer[1],2)))