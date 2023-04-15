import json

class Question:
    def __init__(self, data):
        self.question = data["Question"]
        self.category = data["Category"]
        self.weight = data["Weight"] # float

    def getScore(self, val): # val should be 1-5
        return val*self.weight

class Quiz:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            self.data1 = json.load(f)
            self.data = self.data1["Quiz"]

        self.questions = []
        for i in range(len(self.data)):
            obj = Question(self.data[i])
            self.questions.append(obj)

        self.scores = [0.0, 0.0, 0.0]
        self.category_count = len(self.data)
        self.q = 0 # current question
        
        self.result_category = -1

        self.finished = False

    def getQuestion(self):
        return self.questions[self.q]

    def getQuestionString(self):
        return self.questions[self.q].question

    def giveAnswer(self, val):
        q = self.getQuestion()
        self.scores[q.category] += q.getScore(val)

        if self.q >= len(self.questions)-1:
            print("finished")
            self.finish()

    def nextQuestion(self):
        self.q += 1

    def finish(self):
        self.result_category = self.getResult()
		
        print("You fit into category " + str(self.result_category))
        self.finished = True
        
    def getResult(self):
        highest = 0
        for i in range(len(self.scores)):
            if self.scores[i] > 0:
                highest = i
        return highest

# Here is how to use it. 
testquiz = Quiz("backend/quiz.json")
while not testquiz.finished:
    print(testquiz.getQuestionString()) # Get question string to display the actual question
    testquiz.giveAnswer(int(input("1-5:")))
    testquiz.nextQuestion() # Move onto the next question, repeat
print(testquiz.getResult())