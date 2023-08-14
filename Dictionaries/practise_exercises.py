def display_facts(facts):
    """Displays facts"""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()


facts = {
    'Jeff': 'Is afraid of clowns',
    'David': 'Plays the piano',
    'Jason': 'Can fly an airplane',
}


# Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and their interesting fact to the screen.

display_facts(facts)


# Next, change a fact about one of
# the people. Also add an additional person and corresponding fact. Display the new list of people
# and facts. Run the program multiple times and notice if the order changes

facts['Jill'] = 'Can hula dance'
facts['Jeff'] = 'Is afraid of heights'

display_facts(facts)
