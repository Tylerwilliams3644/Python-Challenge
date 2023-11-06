import csv

with open("election_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    total_votes = 0

    charles_votes = 0

    diana_votes = 0

    raymon_votes = 0

    canidates_names = []

    canidates_votes = []

    canidates_dict = {}

    next(csv_reader)

    for line in csv_reader:
        total_votes += 1
        canidates = line[2]
        if line[2] == "Charles Casper Stockham":
            charles_votes += 1
        if line[2] == "Diana DeGette":
            diana_votes += 1
        if line[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        charles_percentage = round(int(charles_votes) / int(total_votes) * 100, 3)
        diana_percentage = round(int(diana_votes) / int(total_votes) * 100, 3)
        raymon_percentage = round(int(raymon_votes) / int(total_votes) * 100, 3)
        if canidates not in canidates_names:
            canidates_names.append(canidates)

    for key, value in zip(canidates_names, canidates_votes):
        canidates_dict[key] = value

    pypoll_results = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n"
        f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n"
        f"Diana DeGette: {diana_percentage}% ({diana_votes})\n"
        f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n"
        f"------------------------\n"
        ####### need to find a way to make the winner and automated process
        # f"Winner: {winner}\n"
        f"------------------------\n"
    )
    print(pypoll_results)
    print(canidates_dict)
