import csv


# def average_change(list_to_average):
# return sum(list_to_average) / len(list_to_average)


# reading csv file
with open("budget_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # skips the headers and goes to the first value in the set
    next(csv_reader)

    # create empty list to store values for profit loss
    list_profit_loss = []
    # create empty list to store total months
    list_months = []
    # new list for
    list_sum_profit_loss = []

    prev_line = False

    greatest_increase = 0

    greatest_decrease = 0

    greatest_increase_month = ""

    greatest_decrease_month = ""

    # loop through the csvfile
    for line in csv_reader:
        # variabl for the different months
        months = line[0]
        # variable for the different profit/loss
        profit_loss = line[1]
        # add profit/loss to list as int
        list_profit_loss.append(int(profit_loss))
        # add months to list
        list_months.append(months)
        # add profit_loss columns together and find max
        if prev_line:
            monthly_change = int(line[1]) - int(prev_line[1])
            list_sum_profit_loss.append(monthly_change)
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = months
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = months
        prev_line = line

    results = (
        f"Financial Analysis\n"
        f"---------------------------------------\n"
        f"Total Months: {len(list_months)}\n"
        f"Total: ${sum(list_profit_loss)}\n"
        # Average change formula = y1-y2/x2-x1
        # Reference list profit loss find the length to get the last number and -1 to fix 0 index, then subtract number in 0 index/length of list - 1 to fix 0 index and round the number to 2 decmial plaecs
        f"Average Change: ${round(((list_profit_loss[len(list_profit_loss) - 1]) - (list_profit_loss[0]))/ (len(list_profit_loss) - 1), 2)}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease})\n"
    )
    print(results)
with open("PyBank_Results.txt", "w") as textfile:
    textfile.write(results)
