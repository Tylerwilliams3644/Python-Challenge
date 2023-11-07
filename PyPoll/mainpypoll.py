import csv

with open("election_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    total_votes = 0

    max_votes = 0

    canidates_names = []

    canidates_votes = []

    canidates_dict = {}

    winner_dict = {}

    header = next(csv_reader)

    for line in csv_reader:
        total_votes += 1
        if line[2] in canidates_dict.keys():
            canidates_dict[line[2]] += 1
        else:
            canidates_dict[line[2]] = 1

        Ballot_ID = line[0]
        County = line[1]
        canidates = line[2]

        if canidates not in canidates_names:
            canidates_names.append(canidates)

    for key, value in canidates_dict.items():
        print(f"{key}: {round(value/total_votes *100, 3)}% ({value})")

        if value > max_votes:
            winner = key
            max_votes = value

    print(f"Winner: {winner}")

    # if line[2] == "Charles Casper Stockham":
    #    charles_votes += 1
    # if line[2] == "Diana DeGette":
    #    diana_votes += 1
    # if line[2] == "Raymon Anthony Doane":
    #    raymon_votes += 1
    # charles_percentage = round(int(charles_votes) / int(total_votes) * 100, 3)
    # diana_percentage = round(int(diana_votes) / int(total_votes) * 100, 3)
    # raymon_percentage = round(int(raymon_votes) / int(total_votes) * 100, 3)

    # pypoll_results = (
    # f"Election Results\n"
    # f"------------------------\n"
    # f"Total Votes: {total_votes}\n"
    # f"------------------------\n"
    # f"Charles Casper Stockham: {charles_percentage}% ({charles_votes})\n"
    # f"Diana DeGette: {diana_percentage}% ({diana_votes})\n"
    # f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_votes})\n"
    # f"------------------------\n"
    ######## need to find a way to make the winner and automated process
    ## f"Winner: {winner}\n"
    # f"------------------------\n"
    # )
    # print(pypoll_results)
    print(canidates_dict)
    print(total_votes)
