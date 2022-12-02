'''
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
'''


from part_1 import play

def choose(outcome, elf):
    # X = lose, Y = draw, Z = win
    # X = Rock, Y = Paper, Z = Scissors
    # A = Rock, B = Paper, C = Scissors

    # Lose
    if outcome == 'X':
        if elf == 'A':
            return 'Z'
        elif elf == 'B':
            return 'X'
        elif elf == 'C':
            return 'Y'
    # Draw
    elif outcome == 'Y':
        if elf == 'A':
            return 'X'
        elif elf == 'B':
            return 'Y'
        elif elf == 'C':
            return 'Z'
    # Win
    elif outcome == 'Z':
        if elf == 'A':
            return 'Y'
        elif elf == 'B':
            return 'Z'
        elif elf == 'C':
            return 'X'


if __name__ == "__main__":
    # Read the input file and store as list of tuples
    with open("input.txt", "r") as f:
        strategy = [tuple(line.strip().split()) for line in f]

    scores = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0
    
    # Loop through the strategy and play the game
    for elf, outcome in strategy:
        player_choice = choose(outcome, elf)
        total_score += play(player_choice, elf)
        total_score += scores[player_choice]

    print(total_score)
