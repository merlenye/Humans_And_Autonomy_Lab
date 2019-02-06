import os 
import csv


print(os.getcwd())

filenames = os.listdir(os.getcwd())
print(filenames)

for filename in filenames:

    if filename.endswith('.csv'):
        print("got it")
        r=csv.reader(open(filename))
        new_data = []
        small = float(1000000000000000)
        for row in r:
            print(row)
            if row[0].startswith("1"):
                n = float(row[0])
                print(n)
                if n < small:
                    small = float(row[0])
                    print(small)
                q = float(row[0])-small
                print(row[0])
                row[0] = q
                new_data.append(row)
        newfilename = "".join(filename.split(".csv")) + "_absolutetime.csv"
        with open(newfilename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(new_data)
        

