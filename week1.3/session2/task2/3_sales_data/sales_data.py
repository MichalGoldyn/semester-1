# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

with open('week1.3/session2/task2/3_sales_data/sales.csv', 'r') as sales:
    salesData = [x.rstrip('\n').split(',') for x in sales]

    largestSaleDay = 0
    totalDays = len(salesData) - 1
    totalsales = 0
    for x in salesData:
        if x[2] == "Sales_Amount":
            continue
        elif int(x[2]) > largestSaleDay:
            largestSaleDay = int(x[2])
            totalsales += int(x[2]) * int(x[3])
        else:
            totalsales += int(x[2]) * int(x[3])
    


print(totalsales/totalDays)
print(largestSaleDay)
products=["Widget A", "Widget B", "Widget C", "Widget D"]
counts = [0, 0, 0, 0]
for i in salesData:
    tmp = i[1]
    if tmp == "Widget A":
        counts[0] += int(i[3])
    elif tmp == "Widget B":
            counts[1] += int(i[3])
    elif tmp == "Widget C":
                counts[2] += int(i[3])
    elif tmp == "Widget D":
                counts[3] += int(i[3])

print(products[counts.index(max(counts))])


# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget

# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows