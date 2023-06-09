from os import path

POINTS_PER_GUESS = 5


def load_sentences() -> list:
    """ Read sentences from file """
    returned_array = []
    with open(f"{path.dirname(__file__)}\\sentences.txt", "r+") as sentences:
        for sentence in sentences:
            returned_array.append(sentence.strip().split(' '))

    return returned_array


def is_sentence(sentence: list | None = None) -> bool:
    """ Verify if the list is a valid sentences who build from words """
    if type(sentence) != list:
        return False

    for word in sentence:
        if type(word) != str:
            return False

    s = " ".join(sentence)
    for char in s:
        if char.isdigit():
            return False

    return True


def is_char(char: str | None = None) -> bool:
    """ Validate that given string is 1 alphanumeric character """
    return type(char) == str and len(char) == 1 and char.isalpha()


def sentence_len(sentence: list | None = None) -> int:
    """ Return the length of a given sentence """
    if is_sentence(sentence):
        return len("".join(sentence))
    return 0


def hide_chars(sentence: list | None = None) -> list | None:
    """ Return the given sentences with hidden characters """

    # Verify if the sentence is a valid
    if not is_sentence(sentence):
        return None

    hidden_sentence = ""
    s = " ".join(sentence)
    for char in s:
        if char.isalpha():
            hidden_sentence += "_"
        else:
            hidden_sentence += char

    return hidden_sentence.split(" ")


def index_char_in_sentence(sentence: list | None = None, char: str | None = None) -> list | None:
    """ This function responsible for find the indexes of given char in a given sentence """
    if not is_sentence(sentence) or not is_char(char):
        return None

    indexes = []
    s = " ".join(sentence)
    for index, _char in enumerate(s):
        if _char.lower() == char.lower():
            indexes.append(index)
    return indexes


def update_hidden_sentence(sentence=None, indexes=None, char: str = "") -> list[str] | None:
    """ Responsible for receive hidden sentence, list of indexes and a char, and locate the char
        in the sentence based on the indexes """
    if indexes is None:
        indexes = []
    if sentence is None:
        sentence = []
    if len(sentence) == 0 or len(indexes) == 0 or not is_char(char):
        return None

    s = " ".join(sentence)
    for index in indexes:
        s = s[0:index] + char + s[index + 1:]

    return s.split(" ")


def game_round(sentence: list | None = None) -> int | None:
    """ Responsible for one game logic """
    if not is_sentence(sentence):
        return None

    hide_sentence = hide_chars(sentence)
    word_left = sentence_len(sentence)
    score = 0
    print(f"Let's start the Game! the is the sentence you need to guess: {' '.join(hide_sentence)}")

    while word_left > 0:
        guess = input(f"Please enter your guess: ").lower()
        indexes = index_char_in_sentence(sentence, guess)
        if indexes is None:
            print("Invalid guess, please try again")
        elif guess in "".join(hide_sentence):
            print("Char already been guessed")
        else:
            s = update_hidden_sentence(hide_sentence, indexes, guess)
            if s:
                hide_sentence = s
                successful_guesses = len(indexes)
                word_left -= successful_guesses
                if successful_guesses:
                    score += successful_guesses * POINTS_PER_GUESS
                else:
                    score -= 1

        print(f"Try again! You left {word_left} characters to guess: {' '.join(hide_sentence)}")

    print("Congrats!!! you succeed to solve this!")
    return score
