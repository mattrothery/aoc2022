'''
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

def main():
    # Read the input file
    with open('input.txt', 'r') as f:
        input = f.read()

    # Split the input into a list of lists
    input = input.split('\n\n')
    input = [x.split('\n') for x in input]

    # Remove the empty list at the end
    input.pop()

    # Create a list to store the total calories for each elf
    calories = []

    # Loop through each elf's inventory
    for elf in input:
        # Create a variable to store the total calories for this elf
        total = 0

        # Loop through each item
        for item in elf:
            # Add the calories for this item to the total
            total += int(item)

        # Add the total calories for this elf to the list
        calories.append(total)
    
    # Sort the list of calories from highest to lowest
    calories.sort(reverse=True)

    # Find the top three elves
    top_three = calories[:3]

    # Find the total calories for the top three elves
    total_calories = sum(top_three)

    # Print the answer
    print(total_calories)

if __name__ == '__main__':
    main()