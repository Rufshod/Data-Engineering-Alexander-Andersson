from print_joke import get_random_reaction



def test_get_random_reaction_type():
    reaction = get_random_reaction()
    assert reaction == str(reaction)

def test_get_random_reaction_repeats():
    # Write a test that checks that multiple calls to get_random_reaction() doesn't give you the same reaction every time
    reaction1 = get_random_reaction()
    reaction2 = get_random_reaction()
    assert reaction1 != reaction2


# Come up with a test of your own and implement it here.
