# Import csv
import csv

# Open csv file as read
with open("election_data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # set total votes to 0 to be able to itterate for loop
    total_votes = 0

    # set total votes to 0 to be able to itterate for loop
    max_votes = 0

    # blank dict to add can candidates name as key and votes as value
    candidates_dict = {}

    # skip the first line and set the first line to the variable header
    header = next(csv_reader)

    # set winner variable to none to set it as a variable to call it later
    winner = None

    # blank list to display the output of the key, value loop so we can call it outside of the loop
    output_list = []

    # loop through all the lines
    for line in csv_reader:
        # add one to total votes for each line
        total_votes += 1
        # if the name is in the candidates dict add one to the key(votes)
        if line[2] in candidates_dict.keys():
            candidates_dict[line[2]] += 1
        # if it is not in the dict it is equal to one to start the key(votes) at one and keep adding to it
        else:
            candidates_dict[line[2]] = 1
        # the 0 index is all of the ballot ids
        Ballot_ID = line[0]
        # the 1st index is the counties
        County = line[1]
        # the 2nd index is all of the candidates names
        candidates = line[2]
    # looking thought the candidates dict items with key, value
    for key, value in candidates_dict.items():
        # outputting the name(key), math equation for votes they received rounded 3 places and set to percent, value is the # of votes in ()
        output = f"{key}: {round(value/total_votes *100, 3)}% ({value})"
        # append each printed item to the blank output list so it can be called outside of loop easy
        output_list.append(output)

        # if the votes is bigger the 0(what we set max votes to)
        if value > max_votes:
            # the winner is the person with the max votes
            winner = key
            # loops through  to find the value with the max votes
            max_votes = value

    # varaible to call to for the intended out put of the candidates names and votes
    name_vote_results = f"{output_list[0]}\n" f"{output_list[1]}\n" f"{output_list[2]}"

    # format the results
    all_results = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n"
        f"{name_vote_results}\n"
        f"------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------"
    )
    # print results
    print(all_results)

    # make a new text file with intended results
    with open("PyPoll_Results.txt", "w") as textfile:
        textfile.write(all_results)
