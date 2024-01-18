import re
import random
from enum import Enum

# TODO: README
# TODO: front-end with hiragana keyboard

class Type(Enum):
  U_VERB = 1
  RU_VERB = 2
  NA_ADJECTIVE = 3
  I_ADJECTIVE = 4
  ANIMATE_NOUN = 5
  INANIMATE_NOUN = 6

class Word:
    def __init__(self, japanese, english, type):
        self.japanese = japanese
        self.english = english
        self.type = type

adjectives = [
  Word("しずか", "quiet", Type.NA_ADJECTIVE),
  Word("たかい", "tall/expensive", Type.I_ADJECTIVE),
  Word("きれい", "clean/beautiful", Type.I_ADJECTIVE),
  Word("きらい", "hateful", Type.I_ADJECTIVE),
  Word("しんせつ", "thoughtful", Type.NA_ADJECTIVE),
  Word("すき", "liked", Type.NA_ADJECTIVE),
  Word("おいしい", "tasty", Type.I_ADJECTIVE),
  Word("いい", "good", Type.I_ADJECTIVE),
  Word("かっこいい", "cool", Type.I_ADJECTIVE),
]

verbs = [
  Word("たべる", "eat", Type.RU_VERB),
  Word("わかる", "understand", Type.U_VERB),
  Word("みる", "see", Type.RU_VERB),
  Word("ねる", "sleep", Type.RU_VERB),
  Word("かんがえる", "think", Type.RU_VERB),
  Word("おしえる", "teach/inform", Type.RU_VERB),
  Word("でる", "exit", Type.RU_VERB),
  Word("きる", "wear", Type.RU_VERB),
  Word("きる", "cut", Type.U_VERB),
  Word("はしる", "run", Type.RU_VERB),
  Word("きく", "ask/listen", Type.U_VERB),
  Word("あそぶ", "play", Type.U_VERB),
  Word("まつ", "wait", Type.U_VERB),
  Word("しぬ", "die", Type.U_VERB),
  Word("のむ", "drink", Type.U_VERB),
  Word("かう", "buy", Type.U_VERB),
  Word("かく", "write", Type.U_VERB),
  Word("もつ", "hold", Type.U_VERB),
  Word("すてる", "throw away", Type.RU_VERB),
  Word("よむ", "read", Type.U_VERB),
  Word("くる", "come", Type.RU_VERB), #exception 
  Word("する", "do", Type.RU_VERB), # exception
  Word("いる", "exist(animate)", Type.RU_VERB),
  Word("ある", "exist(inanimate)", Type.RU_VERB),
  Word("いく", "go", Type.U_VERB),
]

nouns = [
  Word("ひと", "person", Type.ANIMATE_NOUN),
  Word("ともだち", "friend", Type.ANIMATE_NOUN),
  Word("わたし", "I", Type.ANIMATE_NOUN),
  Word("ねこ", "cat", Type.ANIMATE_NOUN),
  Word("さかな", "fish", Type.ANIMATE_NOUN),
  Word("にく", "meat", Type.INANIMATE_NOUN),
  Word("やさい", "vegetable", Type.INANIMATE_NOUN),
  Word("たべもの", "food", Type.INANIMATE_NOUN),
  Word("ビル", "building", Type.INANIMATE_NOUN),
  Word("ねだん", "price", Type.INANIMATE_NOUN),
  Word("おかね", "money", Type.INANIMATE_NOUN),
  Word("えいが", "movie", Type.INANIMATE_NOUN),
  Word("ごはん", "rice", Type.INANIMATE_NOUN),
]

def getNoun():
    return nouns[random.randint(0, len(nouns) - 1)]

def getAdjective():
    return adjectives[random.randint(0, len(adjectives) - 1)]

def getVerb():
    return verbs[random.randint(0, len(verbs) - 1)]

def convertAdjective(adjective, adjectiveType, adjectiveIsPositive, adjectiveInPresentTense):
    if adjective == "いい" or adjective == "かっこいい":
        if adjective == "かっこいい":
            adjective = "かっこ"
        else:
            adjective = ""

        if adjectiveIsPositive and adjectiveInPresentTense:
            return adjective + "いい"
        elif not adjectiveIsPositive and adjectiveInPresentTense:
            return adjective + "よくない"
        elif adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective + "よかった"
        elif not adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective + "よくなかった"

    if adjectiveType == Type.NA_ADJECTIVE:
        if adjectiveIsPositive and adjectiveInPresentTense:
            return adjective + "な"
        elif not adjectiveIsPositive and adjectiveInPresentTense:
            return adjective + "じゃない"
        elif adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective + "だった"
        elif not adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective + "じゃなかった"
    elif adjectiveType == Type.I_ADJECTIVE:
        if adjectiveIsPositive and adjectiveInPresentTense:
            return adjective
        elif not adjectiveIsPositive and adjectiveInPresentTense:
            return re.sub(r"い$", "", adjective) + "くない"
        elif adjectiveIsPositive and not adjectiveInPresentTense:
            return re.sub(r"い$", "", adjective) + "かった"
        elif not adjectiveIsPositive and not adjectiveInPresentTense:
            return re.sub(r"い$", "", adjective) + "くなかった"

def convertVerb(verb, verbType, verbIsPositive, verbInPresentTense):
    aEquivalent = {
        "う":"あ",
	    "く":"か",
        "す":"さ",
	    "つ":"た",
        "ぬ":"な",
	    "ふ":"は",
        "む":"ま",
	    "ゆ":"や",
        "る":"ら",
        "ぐ":"が",
        "ず":"ざ",
        "づ":"だ",
        "ぶ":"ば",
        "ぷ":"ぱ",
    }

    if verbType == Type.RU_VERB:
        if verbIsPositive and verbInPresentTense:
           return verb
        elif not verbIsPositive and verbInPresentTense:
            if verb == "する":
                return "しない"
            elif verb == "くる":
                return "こない"
            elif verb == "ある":
                return "ない"

            return re.sub(r"る$", "", verb) + "ない"
        elif verbIsPositive and not verbInPresentTense:
            if verb == "する":
                return "した"
            elif verb == "した":
                return "こない"
            
            return re.sub(r"る$", "", verb) + "た"
        elif not verbIsPositive and not verbInPresentTense:
            if verb == "する":
                verb = "しない"
            elif verb == "くる":
                verb = "こない"
            elif verb == "ある":
                verb = "ない"

            verb = re.sub(r"る$", "", verb) + "ない"
           
            return re.sub(r"い$", "", verb) + "かった"
    elif verbType == Type.U_VERB:
        if verbIsPositive and verbInPresentTense:
            return verb
        elif not verbIsPositive and verbInPresentTense:
            if re.search(r"(う$)", verb):
                return re.sub(r"う$", "", verb) + "わない"
            else:
                lastSymbol = re.search("([ぁ-ゔァ-ヴー])$", verb)
                return re.sub("([ぁ-ゔァ-ヴー])$", "", verb) + aEquivalent[lastSymbol.group(0)] + "ない"
        elif verbIsPositive and not verbInPresentTense:
            if verb == "いく":
                return "いた"
            elif (re.search(r"す$", verb)):
                return re.sub("す$", "した", verb)
            elif (re.search(r"く$", verb)):
                return re.sub("く$", "いた", verb)
            elif (re.search(r"す$", verb)):
                return re.sub("ぐ$", "いだ", verb)
            elif (re.search(r"む$|ぬ$|ぶ$", verb)):
                return re.sub("む$|ぬ$|ぶ$", "んだ", verb)
            elif (re.search(r"る$|つ$|う$", verb)):
                return re.sub("る$|つ$|う$", "った", verb)
        elif not verbIsPositive and not verbInPresentTense:
            if re.search(r"(う$)", verb):
                verb = re.sub(r"う$", "", verb) + "わない"
            else:
                lastSymbol = re.search("([ぁ-ゔァ-ヴー])$", verb)
                verb = re.sub("([ぁ-ゔァ-ヴー])$", "", verb) + aEquivalent[lastSymbol.group(0)] + "ない"

            return re.sub(r"い$", "", verb) + "かった"

if __name__=="__main__":
    print("Hiragana virtual keyboard in: https://lexilogos.com/keyboard/hiragana.htm")
    print("How many questions do you want?")
    numberOfQuestions = int(input())
    totalScore = 0

    for questionNumber in range(1, numberOfQuestions + 1):
        adjective = getAdjective()
        noun = getNoun()
        verb = getVerb()
        particle = "が";

        while (verb.japanese == "いる" and noun.type != Type.ANIMATE_NOUN):
            noun = getNoun()
        while (verb.japanese == "ある" and noun.type != Type.INANIMATE_NOUN):
            noun = getNoun()

        adjectiveInPresentTense = random.randint(0, 1)
        adjectiveIsPositive = random.randint(0, 1)
        verbInPresentTense = random.randint(0, 1)
        verbIsPositive = random.randint(0, 1)

        print(f"""{questionNumber} - How do you say\n'{noun.english} that {
        'is ' if adjectiveInPresentTense else 'was '}{
        '' if adjectiveIsPositive else 'not '}{adjective.english}{
        ' do ' if verbInPresentTense else ' did '}{
        '' if verbIsPositive else 'not '}{verb.english}'\nin Japanese?\n""")
       
        correctAnswer = convertAdjective(adjective.japanese, adjective.type, adjectiveIsPositive, adjectiveInPresentTense)
        correctAnswer += noun.japanese
        correctAnswer += particle
        correctAnswer += convertVerb(verb.japanese, verb.type,verbIsPositive, verbInPresentTense)
        userAnswer = input()

        if userAnswer == correctAnswer:
            print("Correct!\n")
            totalScore += 1
        else:
            print(f"Wrong! The correct answer is:\n{correctAnswer}\n")
        
    print(f"You got {totalScore} out of {numberOfQuestions} right.")
