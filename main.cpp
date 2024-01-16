#include<bits/stdc++.h>

using namespace std;

// TODO: ramdomly generate past and positive
// TODO: implement convert function
// TODO: ramdomly return verbs, nouns and adjectives
// TODO: fill verbs, nouns and adjetives lists
// TODO: treat 3 exception verbs, iru and aru and ii and kakoii
// TODO: README

enum Type {
  U_VERB,
  RU_VERB,
  NA_ADJECTIVE,
  I_ADJECTIVE,
  NOUN
};

struct Word {
  string japanese;
  string english;

  Type type;

  Word(string japanese, string english, Type type) :
  japanese(japanese), english(english), type(type) {};
};

const vector<Word> adjectives = {
  Word("しずか", "quiet", Type::NA_ADJECTIVE),
  Word("すき", "like", Type::I_ADJECTIVE)
};

const vector<Word> verbs = {
  Word("たべる", "eat", Type::RU_VERB),
  Word("はなす", "talk", Type::U_VERB)
};

const vector<Word> nouns = {
  Word("ひと", "person", Type::NOUN)
};

Word getNoun() {
  return nouns[0];
}

Word getAdjective() {
  return adjectives[0];
}

Word getVerb() {
  return verbs[0];
}

string convertAdjective(Word adjective, bool adjectiveIsPositive, bool adjectiveInPresentTense) {
  switch (adjective.type) {
    case NA_ADJECTIVE:
      if (adjectiveIsPositive && adjectiveInPresentTense) {
        return adjective.japanese + "な";
      } else if (!adjectiveIsPositive && adjectiveInPresentTense) {
        return adjective.japanese + "じゃない";
      } else if (adjectiveIsPositive && !adjectiveInPresentTense) {
        return adjective.japanese + "だった";
      } else if (!adjectiveIsPositive && !adjectiveInPresentTense) {
        return adjective.japanese + "じゃなかった";
      }
      break;
    case I_ADJECTIVE:
     if (adjectiveIsPositive && adjectiveInPresentTense) {
        return adjective.japanese;
      } else if (!adjectiveIsPositive && adjectiveInPresentTense) {
          return regex_replace(adjective.japanese, regex("い$"), "") + "くない";
      } else if (adjectiveIsPositive && !adjectiveInPresentTense) {
          return regex_replace(adjective.japanese, regex("い$"), "") + "かった";
      } else if (!adjectiveIsPositive && !adjectiveInPresentTense) {
          return regex_replace(adjective.japanese, regex("い$"), "") + "くなかった";
      }
      break;
    default:
      return ""; 
  }
  return "";
}

string convertVerb(Word verb, bool verbIsPositive, bool verbInPresentTense) {
  switch (verb.type) {
    case RU_VERB:
      if (verbIsPositive && verbInPresentTense) {
        return verb.japanese;
      } else if (!verbIsPositive && verbInPresentTense) {
        return regex_replace(verb.japanese, regex("る$"), "") + "ない";
      } else if (verbIsPositive && !verbInPresentTense) {
        // TODO
      } else if (!verbIsPositive && !verbInPresentTense) {
        // TODO
      }
    break;
    case U_VERB:
      if (verbIsPositive && verbInPresentTense) {
        return verb.japanese;
      } else if (!verbIsPositive && verbInPresentTense) {
        if (regex_search(verb.japanese, regex(R"(う$)"))) {
          return regex_replace(verb.japanese, regex("う$"), "") + "わない";
        }
        // TODO: verbs not ending in u
      } else if (verbIsPositive && !verbInPresentTense) {
        // TODO
      } else if (!verbIsPositive && !verbInPresentTense) {
        // TODO 
      }
      break;
    default:
      return "";
  }
  return "";
}

int main() {

  cout << "How many questions do you want?\n";
  int numberOfQuestions;
  cin >> numberOfQuestions;
  int totalScore = 0;

  for (int _ = 0; _ < numberOfQuestions; _++) {
    Word adjective = getAdjective();
    Word noun = getNoun();
    Word verb = getVerb();
    const string particle = "が";

    // present or past
    // negative or positive
    bool adjectiveIsPositive = true;
    bool adjectiveInPresentTense = true;
    bool verbIsPositive = true;
    bool verbInPresentTense = true;

    cout << "How do you say\n" <<
    noun.english << " that " <<
    (adjectiveInPresentTense ? "is " : "was ")  <<
    (adjectiveIsPositive ? "" : "not ")  <<
    adjective.english << " " <<
    (verbInPresentTense ? "do " : "did ")  <<
    (verbIsPositive ? "" : "not ")  <<
    verb.english <<
    "\nin Japanese?\n";

    string userAnswer, correctAnswer = "";
    correctAnswer += convertAdjective(adjective, adjectiveIsPositive, adjectiveInPresentTense);
    correctAnswer += noun.japanese;
    correctAnswer += particle;
    correctAnswer += convertVerb(verb, verbIsPositive, verbInPresentTense);

    cin >> userAnswer;

    if (userAnswer == correctAnswer) {
      cout << "Correct!\n";
      totalScore++;
    } else {
      cout << "Wrong! The correct answer is:\n";
      cout << correctAnswer << '\n';
    }
  }

  cout << "You got " << totalScore << " out of " << 
  numberOfQuestions << " right.\n";

  return 0;
}
