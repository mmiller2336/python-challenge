#import os module and csv reading file
import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')

# total nbr of months in dataset

month_total = 0
amount_net = 0
amount = []
months = []




with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    next(csvreader)

    
    for row in csvreader:
        month_total += 1
        amount_net = amount_net + int(row[1])
        months.append(row[0])
        amount.append(row[1])

        average = amount_net/month_total

        greatInc = max(amount)
        greatDec = min(amount)

        greatInc_index = amount.index(greatInc)
        greatDec_index = amount.index(greatDec)

        print (f"no of {month_total} months")
        print (f"net amount {amount_net}")
        print (f" average change was {average} per month")
        print (f"greatest increase was {greatInc} and it happened at {months[greatInc_index]}")
        print(f" greatest decrease was {greatDec} and it happened at {months[greatDec_index]}")


        month_highest = str(greatInc+ " " +months[greatInc_index])
        month_lowest = str(greatDec+ " " +months[greatDec_index])


        #write output to text file

        f = open("pybank_output.txt", "w")

        f.write("There are" +str(month_total) +"months\n")
        f.write("There was" +str(amount_net) +"months\n")
        f.write("The Average net change was" +str(average) +" Dollar Average per month\n")
        f.write("the greatest increase was " +str(greatInc) +" and it happened at " +str(months[greatInc_index]) +"\n")
        f.write("the greatest decrease was " +str(greatDec) +" and it happened at " +str(months[greatDec_index]) +"\n")
        f.close()

        



