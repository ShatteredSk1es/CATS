"""Typing test implementation"""

import string
from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1

    if len(paragraphs) <= k:
        return ""
    index=0
    for para in paragraphs:
        if select(para) == True and index == k:
            return para
        elif select(para):
            index += 1
    return ''




    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2

    def contain(paragraph):
        string = split(remove_punctuation(lower(paragraph)))
        i=0
        bool = False
        while i <= (len(topic)-1):
                if topic[i] in string[:]:
                    i +=1
                    bool = True
                else:
                    i +=1
        return bool
    return contain

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3





    ####
    i=0
    correct = 0
    if typed == "" and reference == "":
        return 100.0
    elif typed == "":
        return 0.0
    elif reference == False:
        return 0.0
    else:
        while i <= min(len(reference_words) -1, len(typed_words) -1):
            if typed_words[i] == reference_words[i]:
                correct = correct + 1
            i +=1 
        return (correct/len(typed_words)) *100
    ####




    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4

    if typed == "":
        return 0.0
    else:
        return (len(typed)/5)*(60/elapsed)


    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    if typed_word in word_list:
        return typed_word
    else: 
        diffwordlist = [diff_function(typed_word, word, limit) for word in word_list]
        index = diffwordlist.index(min(diffwordlist))
        if limit < min(diffwordlist):
            return typed_word
        return word_list[index]
    # END PROBLEM 5


def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6

    index = 0
    def helperfunc(start, goal, index):
        absdiff = abs(len(start) - len(goal))
        minlen = min(len(start), len(goal))
        startaltered = start[0:minlen]
        goalaltered = goal[0:minlen]
        
        if start == goal:
            return 0
        elif limit < 0:
            return 0
        elif startaltered[0] == goalaltered[0] and index <= limit+3:
            total = helperfunc(startaltered[1:], goalaltered[1:], index+1)
            return total + absdiff
        elif startaltered[0] != goalaltered[0] and index <= limit+3:
            total = 1 + helperfunc(startaltered[1:], goalaltered[1:], index+1)
            return total + absdiff
        else:
            return (limit + 1)
    return helperfunc(start, goal, index)

    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    
    
    
    if start == '' or goal == '':  # Fill in the condition
        return abs(len(start) - len(goal))
    
    elif limit < 0 :  # Feel free to remove or add additional cases
        return limit + 1
    
    elif start[0] == goal[0]:
        first_letter_same = minimum_mewtations(start[1:], goal[1:], limit)
        return first_letter_same
    
    else:
        add = 1 + minimum_mewtations(start[:], goal[1:], limit - 1) 
        remove = 1 + minimum_mewtations(start[1:], goal[:], limit - 1)
        substitute = 1 + minimum_mewtations(start[1:], goal[1:], limit - 1)

        return min(add, remove, substitute)



def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8


    index = 0
    count = 0
    for word in sofar:
        if sofar[index] == prompt[index]:
            count += 1 
            index += 1
        else:
            progress_val = count/len(prompt)
            answer = {'id': user_id, "progress": progress_val}
            upload(answer)
            return progress_val
        
    progress_val = count/len(prompt)
    answer = {'id': user_id, "progress": progress_val}
    upload(answer)
    return progress_val
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9

    i = 0
    ind = 0
    index = 0
    
    player1times = []
    player2times = []
    player3times = []
    noofplayers = len(times_per_player)

    if noofplayers == 1:
        while ind < len(times_per_player[0]) -1 :
            player1times = player1times + [(times_per_player[0][ind+1] - times_per_player[0][ind])]
            ind += 1
            print("DEBUG", player1times)
        time = [player1times]
    elif noofplayers == 2:
        while i < len(times_per_player[0]) -1 :
            player1times = player1times + [(times_per_player[0][i+1] - times_per_player[0][i])]
            player2times = player2times + [(times_per_player[1][i+1] - times_per_player[1][i])]
            i += 1
            print("DEBUG", player1times)
            print("DEBUG", player2times)
        time = [player1times, player2times]
    elif noofplayers ==3:
        while index < len(times_per_player[2]) -1 :
            player1times = player1times + [(times_per_player[0][index+1] - times_per_player[0][index])]
            player2times = player2times + [(times_per_player[1][index+1] - times_per_player[1][index])]
            player3times = player3times + [(times_per_player[2][index+1] - times_per_player[2][index])]
            index += 1
        time = [player1times, player2times, player3times]
    return match(words, time)
    
    
    """
    player0times = []
    for firsttimesforplayer0 in times_per_player[0][:-1]:
        for secondtimesforplayer0 in times_per_player[0][1:]:
            player0times += [secondtimesforplayer0-firsttimesforplayer0]
            print("DEBUG", player0times)
    
    player1times = []
    for firsttimesforplayer1 in times_per_player[1][:-1]:
        for secondtimesforplayer1 in times_per_player[1][1:]:
            player1times += [secondtimesforplayer1-firsttimesforplayer1]

    time = [player0times, player1times]
    return match(words, time)"""


    """index = 0
    index1 = 0
    player0times = []
    times_per_player_sliced_player0 = times_per_player[0][1:]
    while index < len(times_per_player_sliced_player0):
        player0times = player0times + [(times_per_player_sliced_player0[index] - times_per_player[0][index])]
        index += 1
        print("DEBUG", player0times)

        
    player0times = player0times[:-1]

    player1times = []
    times_per_player_sliced_player1 = times_per_player[1][1:]
    while index < len(times_per_player_sliced_player1):
        player1times = player1times + [(times_per_player_sliced_player1[index] - times_per_player[1][index])]
        index1 += 1
    player1times = player1times[:-1]
    print("DEBUG", player1times)
    time = [player0times, player1times] """




    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(match["times"]))  # contains an *index* for each player
    word_indices = range(len(match["words"]))    # contains an *index* for each word
    # BEGIN PROBLEM 10


    final_list = [[] for playernum in player_indices]
    for word_index in word_indices:
        mintime = 100 #Just a high initial value
        player = 0
        for playernum in player_indices:
            if time(match, playernum, word_index) < mintime:
                mintime = time(match, playernum, word_index)
                player = playernum
        final_list[player] = final_list[player] + [(word_at(match, word_index))]
    return final_list


    # END PROBLEM 10


def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def word_at(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
