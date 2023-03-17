sentences_list = [
    ["Next", "big", "feat?"],
    ["Get", "over", "it"],
    ["Grace", "under", "pressure"],
    ["Go", "for", "it"],
    ["Handle", "breakdowns", "immediately"],
    ["Happiness", "is", "Choice"],
    ["Health", "is", "wealth"],
    ["Hope", "trumps", "all"],
    ["Identify", "key", "milestones"],
    ["It", "is", "possible"],
    ["Judgement", "free", "zone"],
    ["Just", "be", "awesome"],
    ["Keep", "it", "cool"],
    ["Keep", "information", "flowing"],
    ["Keep", "it", "simple"],
    ["Keep", "morale", "high"],
    ["Knowledge", "is", "power"],
    ["Laughter", "is", "best"],
    ["Leaders", "are", "early"],
    ["Learn", "from", "yesterday"],
    ["Let", "it", "go"],
    ["Laughter", "is", "medicine"],
    ["Life", "is", "awesome"],
    ["Life", "is", "beautiful"],
    ["Life", "won’t", "wait"],
    ["Live", "life", "daily"],
    ["Live,", "love,", "laugh"],
    ["Live", "your", "potential"],
    ["Love", "endures", "delay"],
    ["Love", "is", "everything"],
    ["Manage", "your", "reputation"],
    ["Manage", "your", "resistance"],
    ["Manage", "resources", "effectively"],
    ["Massive", "motions", "mesmerize"],
    ["Mastery", "abhors", "mediocrity"],
    ["Model", "the", "masters"],
    ["Money", "amplifies", "emotions"],
    ["Monitor", "budgets", "regularly"],
    ["Never", "give", "up"],
    ["Never", "look", "back"],
    ["Nothing", "is", "Impossible"],
    ["Nurture", "your", "best"]
]

def is_sentence(sentence: list | None = None):
    """
    Verify if the list i a valid sentences who build from words
    :param sentence:
    :return: True\False
    """
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
def is_char(char: str | None = None):
    return type(char) == str and len(char) == 1 and char.isalpha()
def sentence_len(sentence: list | None = None):
    if is_sentence(sentence):
        return len("".join(sentence))

def hide_chars(sentence: list | None = None):
    # Verify if the sent sentence is a valid
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

def index_char_in_sentence(sentence: list | None = None, char: str | None = None):
    if not is_sentence(sentence) or not is_char(char):
        return None

    indexes = []
    s = " ".join(sentence)
    for i in range(len(s)):
        if s[i].lower() == char:
            indexes.append(i)
    return indexes

def update_hidden_sentence(sentence: list = [], indexes: list = [], char:str=""):
    if len(sentence) == 0 or len(indexes) == 0 or not is_char(char):
        return None

    s = " ".join(sentence)
    for index in indexes:
        s = s[0:index] + char + s[index+1:]

    return s.split(" ")

def game_round(sentence: list | None = None):
    if not is_sentence(sentence):
        return None

    hide_sentence = hide_chars(sentence)
    word_left = sentence_len(sentence) - 1
    print(f"Let's start the Game! the is the sentence you need to guess: {hide_sentence}")

    while word_left:
        guess = input(f"Please enter your guess: ")
        indexes = index_char_in_sentence(sentence, guess)
        if indexes == None:
            print("Invalid guess, please try again")
            continue

        s = update_hidden_sentence(hide_sentence, indexes, guess)
        if s:
            hide_sentence = s
            word_left -= len(indexes)

        print(hide_sentence)

    print("Congrats!!! you succeed to solve this!")