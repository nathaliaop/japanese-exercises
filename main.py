import re
from enum import Enum

# TODO: ramdomly generate past and positive
# TODO: implement convert function
# TODO: ramdomly return verbs, nouns and adjectives
# TODO: fill verbs, nouns and adjetives lists
# TODO: treat 3 exception verbs, iru and aru and ii and kakoii
# TODO: README

class Type(Enum):
  U_VERB = 1
  RU_VERB = 2
  NA_ADJECTIVE = 3
  I_ADJECTIVE = 4
  NOUN = 5

class Word:
    def __init__(self, japanese, english, type):
        self.japanese = japanese
        self.english = english
        self.type = type

word = Word("しずか", "quiet", Type.NA_ADJECTIVE)

# print(word.type.name)

adjectives = [
  Word("しずか", "quiet", Type.NA_ADJECTIVE),
  Word("たかい】", "like", Type.I_ADJECTIVE)
]

verbs = [
  Word("たべる", "eat", Type.RU_VERB),
  Word("はなす", "talk", Type.U_VERB)
]

nouns = [
  Word("ひと", "person", Type.NOUN)
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
