import os
import csv
election_data = os.path.join('Resources', 'election_data.csv')
election_data_txt = os.path.join('Resources', 'election_data.txt')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(election_data) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes [candidate_name] + 1

with open (election_data_txt, 'w') as text_file:
    election_results = (
    f"Election Results\n"
	f"-------------------------\n"
	f"Total Votes: {total_votes}\n"
	f"-------------------------\n"

    )
    text_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)

        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = (
            f"{candidate}: {vote_percentage}\n"
        )
        text_file.write(voter_output)

    winning_candidate_summary = (
        f"-------------------------\n"
        f"winner: {winning_candidate}\n"
    )
    text_file.write(winning_candidate_summary)


