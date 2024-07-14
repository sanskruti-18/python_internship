def find_winner(votes):
    vote_count = {}
    for candidate in votes:
        if candidate in vote_count:
            vote_count[candidate] += 1
        else:
            vote_count[candidate] = 1
    max_votes = 0
    for candiate, count in vote_count.items():
        if count>max_votes:
            max_votes = count
            winner = candiate
    return winner

votes = ['a', 'b', 'a', 'c', 'a']

print(f"The Winner candidate is {find_winner(votes)}")