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

    print("Financial Analysis")
    print("---------------------------------------")
    print("Total Months: ", len(list_months))
    print(f"Total: ${sum(list_profit_loss)}")
    # Average change formula = y1-y2/x2-x1
    # Reference list profit loss find the length to get the last number and -1 to fix 0 index, then subtract number in 0 index/length of list - 1 to fix 0 index and round the number to 2 decmial plaecs
    print(
        f"Average Change: ${round(((list_profit_loss[len(list_profit_loss) - 1]) - (list_profit_loss[0]))/ (len(list_profit_loss) - 1), 2)}"
    )
    print(max(list_profit_loss))
