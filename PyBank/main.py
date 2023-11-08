import csv


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

    # set this so it skips the first line
    prev_line = False

    # set to 0 so we can add to it
    greatest_increase = 0

    # set to 0 so we can add to it
    greatest_decrease = 0

    # set to blank string so we can add to it
    greatest_increase_month = ""

    # set to blank string so we can add to it
    greatest_decrease_month = ""

    # loop through the csvfile
    for line in csv_reader:
        # variable for the different months
        months = line[0]
        # variable for the different profit/loss
        profit_loss = line[1]
        # add profit/loss to list as int
        list_profit_loss.append(int(profit_loss))
        # add months to list
        list_months.append(months)
        # loop thorugh prev_line (1st loop set to false so it skips)
        if prev_line:
            # equation to get the current line and previous line to find the differece
            monthly_change = int(line[1]) - int(prev_line[1])
            # append those to list_sum_profit_loss
            list_sum_profit_loss.append(monthly_change)
            # finding the greast incresase by looping through as well as finding the month associated to the greatest increase
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = months
            # finding the greast decrease by looping through as well as finding the month associated to the greatest decrease
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = months
        # set prev_line to line so the loop can work the second time it goes through
        prev_line = line
    # all the results in the format
    results = (
        f"Financial Analysis\n"
        f"---------------------------------------\n"
        f"Total Months: {len(list_months)}\n"
        f"Total: ${sum(list_profit_loss)}\n"
        # Average change formula = y1-y2/x2-x1
        # Reference list profit loss find the length to get the last number and -1 to fix 0 index, then subtract number in 0 index/length of list - 1 to fix 0 index and round the number to 2 decmial plaecs
        f"Average Change: ${round(((list_profit_loss[len(list_profit_loss) - 1]) - (list_profit_loss[0]))/ (len(list_profit_loss) - 1), 2)}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )
    # print the results
    print(results)
    # create a new txt file with results
with open("PyBank_Results.txt", "w") as textfile:
    textfile.write(results)
