import re
from enum import Enum

# TODO: ramdomly generate past and positive
# TODO: ramdomly return verbs, nouns and adjectives
# TODO: fill verbs, nouns and adjetives lists
# TODO: treat 3 exception verbs, iru and aru and ii and kakoii
# TODO: README
# TODO: differentiate iru and aru based on noun
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
  Word("きれい", "hateful", Type.I_ADJECTIVE),
  Word("しんせつ", "thoughtful", Type.NA_ADJECTIVE),
  Word("すき", "like", Type.NA_ADJECTIVE),
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
  Word("くる", "come", Type.RU_VERB),
  Word("かく", "write", Type.U_VERB),
  Word("もつ", "hold", Type.U_VERB),
  Word("すてる", "throw away", Type.RU_VERB),
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
  Word("ねだん】", "price", Type.INANIMATE_NOUN),
  Word("おかね", "money", Type.INANIMATE_NOUN),
  Word("えいが", "movie", Type.INANIMATE_NOUN),
  Word("ごはん", "rice", Type.INANIMATE_NOUN),
]

def getNoun():
    return nouns[0]

def getAdjective():
    return adjectives[0]

def getVerb():
    return verbs[0]

def convertAdjective(adjective, adjectiveIsPositive, adjectiveInPresentTense):
    if adjective.type == Type.NA_ADJECTIVE:
        if adjectiveIsPositive and adjectiveInPresentTense:
            return adjective.japanese + "な"
        elif not adjectiveIsPositive and adjectiveInPresentTense:
            return adjective.japanese + "じゃない"
        elif adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective.japanese + "だった"
        elif not adjectiveIsPositive and not adjectiveInPresentTense:
            return adjective.japanese + "じゃなかった"
    elif adjective.type == Type.I_ADJECTIVE:
        if adjectiveIsPositive and adjectiveInPresentTense:
            return adjective.japanese
        elif not adjectiveIsPositive and adjectiveInPresentTense:
            return re.sub(r"い$", "", adjective.japanese) + "くない"
        elif adjectiveIsPositive and not adjectiveInPresentTense:
          return re.sub(r"い$", "", adjective.japanese) + "かった"
        elif not adjectiveIsPositive and not adjectiveInPresentTense:
          return re.sub(r"い$", "", adjective.japanese) + "くなかった"

def convertVerb(verb, verbIsPositive, verbInPresentTense):
    uEquivalent = {
        "あ":"う",
	    "か":"く",
        "さ":"す",
	    "た":"つ",
        "な":"ぬ",
	    "は":"ふ",
        "ま":"む",
	    "や":"ゆ",
        "ら":"る",
        "が":"ぐ",
        "ざ":"ず",
        "だ":"づ",
        "ば":"ぶ",
        "ぱ":"ぷ"
    }
    if verb.type == Type.RU_VERB:
        if verbIsPositive and verbInPresentTense:
           return verb.japanese
        elif not verbIsPositive and verbInPresentTense:
           return re.sub(r"る$", "", verb.japanese) + "ない"
        elif not verbIsPositive and not verbInPresentTense:
            return re.sub(r"る$", "", verb.japanese) + "た"
        elif not verbIsPositive and not verbInPresentTense:
           return re.sub(r"る$", "", verb.japanese) + "なかった"
    elif verb.type == Type.U_VERB:
        if verbIsPositive and verbInPresentTense:
            return verb.japanese
        elif not verbIsPositive and verbInPresentTense:
            if re.search(r"(う$)", verb.japanese):
                return re.sub(r"う$", "", verb.japanese) + "わ"
            else:
                lastSymbol = re.search("([ぁ-ゔァ-ヴー])$", verb.japanese)
                return re.sub("([ぁ-ゔァ-ヴー])$", "", verb.japanese) + uEquivalent[lastSymbol.group(0)] + "ない"
        elif verbIsPositive and not verbInPresentTense:
            if (re.search(r"す$", verb.japanese)):
                return re.sub("す$", "した", verb.japanese)
            elif (re.search(r"く$", verb.japanese)):
                return re.sub("く$", "いた", verb.japanese)
            elif (re.search(r"す$", verb.japanese)):
                return re.sub("ぐ$", "いだ", verb.japanese)
            elif (re.search(r"む$|ぬ$|ぶ$", verb.japanese)):
                return re.sub("む$|ぬ$|ぶ$", "んだ", verb.japanese)
            elif (re.search(r"る$|つ$|う$", verb.japanese)):
                return re.sub("る$|つ$|う$", "った", verb.japanese)
        elif not verbIsPositive and not verbInPresentTense:
            if re.search(r"(う$)", verb.japanese):
                verb.japanese = re.sub(r"う$", "", verb.japanese) + "わない"
            else:
                lastSymbol = re.search("([ぁ-ゔァ-ヴー])$", verb.japanese)
                verb.japanese = re.sub("([ぁ-ゔァ-ヴー])$", "", verb.japanese) + uEquivalent[lastSymbol.group(0)] + "ない"

            return re.sub(r"い$", "", verb.japanese) + "かった"

if __name__=="__main__":
    print("How many questions do you want?\n")
    numberOfQuestions = int(input())
    totalScore = 0

    for _ in range(numberOfQuestions):
        adjective = getAdjective()
        noun = getNoun()
        verb = getVerb()
        particle = "が";

        adjectiveInPresentTense = True
        adjectiveIsPositive = True
        verbInPresentTense = True
        verbIsPositive = True

        print(f"""How do you say\n'{noun.english} that {
        'is ' if adjectiveInPresentTense else 'was '}{
        '' if adjectiveIsPositive else 'not '}{adjective.english}{
        ' do ' if verbInPresentTense else 'did '}{
        '' if verbIsPositive else 'not '}{verb.english}'\nin Japanese?\n""")
       
        correctAnswer = convertAdjective(adjective, adjectiveIsPositive, adjectiveInPresentTense)
        correctAnswer += noun.japanese
        correctAnswer += particle
        correctAnswer += convertVerb(verb, verbIsPositive, verbInPresentTense)
        userAnswer = input()

        if userAnswer == correctAnswer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is:\n{correctAnswer}\n")
        
    print(f"You got {totalScore} out of {numberOfQuestions} right.")
