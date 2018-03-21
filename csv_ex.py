import csv
try:
    
    with open('eggs.csv', newline='') as csvfile:
         spamreader = csv.reader(csvfile, dialect='excel', delimiter=' ', quotechar='|')
         for row in spamreader:
             print(', '.join(row))
except IOError:
    print("No such file present")
finally:
    print("Have a good day ")
