import json
from pprint import pprint
import getpass
import sys
import random

#pprint(data['questions'])

class Question:

    def __init__(self, rawQ):
        #self.section = rawQ['section']
        self.question = rawQ['question']
        self.answers = rawQ['answers']
        self.correct = rawQ['correct']

    def ask(self):
        print self.tostr()

        response = int(sys.stdin.readline().strip())  # answers are integers
        if response == self.correct:
            print "CORRECT"
            return 10
        else:
            print "WRONG"
            return 0


    def tostr(self):
        res = self.question + "\n"
        for i in range(len(self.answers)):
            res += "\t" + str(i+1) + ". " + self.answers[i] + "\n"
        return res

class Questions:
    questions = []

    def __init__(self, fName):
        with open(fName,'r') as data_file:
            data = json.load(data_file)

        for q in data['questions']:
            self.questions.append(Question(q))

        random.shuffle(self.questions)

    def tostr(self, title):
        res = title + "\n"
        for i in range(len(self.questions)):
            res += str(i+1) + ". " + self.questions[i].tostr() + "\n"
        return res

# data = Questions('quiz.json')
# print(len(data.questions))
# print(data.tostr("QUIZZZZZZ"))
