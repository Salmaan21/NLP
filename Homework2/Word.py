import sys
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import random
def main():

    if len(sys.argv) != 2:
        print("error need to specify path to input file")
        exit(-1)

    sentence = ""
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f:
            sentence += line

    tokens = word_tokenize(sentence)
    print("lexical diversity: %.2f" % (len(set(tokens))/len(tokens)))
    tokens, nouns = tokenize_words(tokens)
    most_commonwords = {}
    for word in nouns:
        most_commonwords[word] = tokens.count(word)
    most_commonwords = dict(reversed(sorted(most_commonwords.items(), key=lambda item:item[1])))
    count = 0
    game_words = []
    for i in most_commonwords:
        print(i,most_commonwords[i], end=" ")
        game_words.append(i)
        count += 1
        if count == 50:
            break
    print()
    gameshow(game_words)

def tokenize_words(tokens):
    tokens = [t.lower() for t in tokens if len(t) > 5 and t.lower() not in stopwords.words("english") and t.isalpha()]
    setOfTokens = set(tokens)
    partsOfSpeech = pos_tag(setOfTokens)
    print("First 20 tagged items", partsOfSpeech[:20])
    nouns = [word for word, pos in partsOfSpeech if pos.startswith("N")]
    print(len(tokens),len(nouns))
    return tokens, nouns

def gameshow(words):
    print("Let's play a word guessing game!", end="\n")
    points = 5
    gameover = False
    while points >= 0 and not gameover:
        if len(words) == 0:
            break
        word = random.choice(words)
        words.remove(word)
        guessed = ["_"] * len(word)
        while points >= 0:
            for letters in guessed:
                print(letters, end = " ")
            print()
            guess = ""
            while(len(guess) != 1):
                guess = (input("Guess a letter:")).lower()
            if guess == "!":
                gameover = True
                break
            if guess in word and guess not in guessed:
                points += 1
                print("Right! Score is " + str(points))
                for i in range(len(word)):
                    if word[i] == guess:
                        guessed[i] = guess
            else:
                points -= 1
                print("Sorry, guess again. Score is " + str(points))
            if "_" not in guessed:
                print("You solved it!")
                break
        print()
        if points >= 0 and not gameover:
            print("Current Score: " + str(points))
        else:
            print("Game Over! Total Score: " + str(points))




if __name__=="__main__":
    main()