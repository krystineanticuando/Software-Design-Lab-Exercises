"""
Imperial, Samuel
Group 6
Python code for Project 5 regarding Doctor class
"""


import random

class Doctor(object):
    history = []

    hedges = ("Please tell me more.",
              "Many of my patients tell me the same thing.",
              "Please coninue.")

    qualifiers = ("Why do you say that ",
                  "You seem to think that ",
                  "Can you explain why ")

    replacements = {"I": "you", "me": "you", "my": "your",
                    "we": "you", "us": "you", "mine": "yours",
                    "you": "I", "your": "my", "yours": "mine"}
    def __init__(self):
        pass

    #  modified reply method from doctor.py
    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)
        if probability in (1, 2):
            # Just hedge
            answer = random.choice(Doctor.hedges)
        elif probability == 3 and len(Doctor.history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
                self.changePerson(random.choice(Doctor.history))
        else:
            # Transform the current input
            answer = random.choice(Doctor.qualifiers) + \
                self.changePerson(sentence)
        # Always add the current sentence to the history list
        Doctor.history.append(sentence)
        return answer

    def changePerson(self, sentence):
        """
        Replaces first person pronouns with second person
        pronouns.
        """
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(Doctor.replacements.get(word, word))
        return " ".join(replyWords)

    # two functions added for greeting and
    # farewell message
    def greeting(self):
        return "Good morning, I hope you are well today"
    def signoff(self):
        return "Have a nice day!"
def main():
    d = Doctor()
    print(d.greeting())
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(d.signoff())
            break
        print(d.reply(sentence))
# The entry point for program execution
if __name__ == "__main__":
    main()
