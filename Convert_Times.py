import pandas
df = pandas.read_csv('Data_Frequency_Cleaned.csv')
for i in range(0,42):
    print(i)
    for m in range(0,6):
        newval = (df.iloc[i, m])
        if type(newval) != float and newval != '-': 
            newval = newval.split(":")
            print(newval)
            min = int(newval[0])
            min = min*60
            sec = int(newval[1])
            newval = min + sec
            df.set_value(i, m, newval)
            
df.to_csv('time_in_seconds.csv')
        
        
        
