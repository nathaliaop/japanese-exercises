import re
from adjectives_verbs import Word, Type, getNoun, getVerb, getAdjective

verbs = [
    Word("たべる", "eat"),
    Word("ならう", "learn"),
    Word("わすれる", "forget"),
    Word("さげる", "lower"),
    Word("あげる", "raise"),
]

adjectives = [
    Word("はやい", "early/fast", Type.I_ADJECTIVE),
    Word("べんり", "convenient", Type.NA_ADJECTIVE),
    Word("おもしろい", "interesting", Type.I_ADJECTIVE),
    Word("いそがしい", "busy", Type.I_ADJECTIVE),
    Word("かなしい", "sad", Type.I_ADJECTIVE),
    Word("うれしい", "happy", Type.I_ADJECTIVE),
    Word("さびしい", "lonely", Type.I_ADJECTIVE),
    Word("へた", "unskillful/awkward/poor", Type.NA_ADJECTIVE),
    Word("じょうず", "skilful", Type.NA_ADJECTIVE),
    Word("まじめ", "serious", Type.NA_ADJECTIVE),
    Word("ひつよう", "necessary", Type.NA_ADJECTIVE),
    Word("たいせつ", "important", Type.NA_ADJECTIVE),
    Word("ゆうめい", "famous", Type.NA_ADJECTIVE),
    Word("かわいい", "cute", Type.I_ADJECTIVE),
    Word("あぶない", "dangenrous", Type.I_ADJECTIVE),
    Word("たいへん", "hard", Type.NA_ADJECTIVE),
    Word("おおき", "big", Type.NA_ADJECTIVE),
]

nouns = [
    Word("あさごはん", "breakfast"),
    Word("ひるごはん", "lunch"),
    Word("ぱんごはん", "dinner"),
    Word("のみもの", "drink"),
    Word("としょうかん", "library"),
    Word("えいがかん", "movie theater"),
    Word("おにいさん", "older brother"),
    Word("おねえさん", "older sister"),
    Word("おとうとさん", "younger brother"),
    Word("いもうとさん", "younger sister"),
    Word("こども", "kid"),
    Word("きょうだい", "siblings"),
    Word("へや", "bedroom"),
    Word("がっこう", "school"),
    Word("ちゅうがくせい", "middle school student"),
    Word("こうこうせい", "high school student"),
    Word("だいがくせい", "university student"),
    Word("おとな", "adult"),
    Word("ぎんこう", "bank"),
    Word("こうえん", "park"),
    Word("しごと", "work"),
    Word("いしゃ", "doctor"),
    Word("べんごし", "lawyer"),
]

def convertAdverb(adjective, type):
    if (type == Type.I_ADJECTIVE):
        return re.sub("い$", "", adjective) + "く"
    elif (type == Type.NA_ADJECTIVE):
        return adjective + "に"

if __name__=="__main__":
    print("Hiragana virtual keyboard in: https://lexilogos.com/keyboard/hiragana.htm")
    print("How many questions do you want?")
    numberOfQuestions = int(input())
    totalScore = 0

    for questionNumber in range(1, numberOfQuestions + 1):
        verb = getVerb(verbs)
        noun = getNoun(nouns)
        adjective = getAdjective(adjectives)

        print(f"""{questionNumber}-How do you say\n'{
        verb.english} {noun.english} {
        adjective.english}ly'\nin Japanese?\n""")

        userAnswer = input()
        correctAnswer = noun.japanese + "を" + convertAdverb(adjective.japanese, adjective.type) + verb.japanese

        if (userAnswer == correctAnswer):
            print("Correct!")
            totalScore += 1
        else:
            print(f"Wrong! The correct answer is:\n{correctAnswer}\n")

    print(f"You got {totalScore} out of {numberOfQuestions} right.")
