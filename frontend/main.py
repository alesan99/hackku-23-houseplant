import json
from js import document
from pyodide import ffi
from quiz import Quiz

categories = ["Inattentive-Distractable", "Impulse-Hyper", "Combined"]

# Load Questions
testquiz = Quiz("/quiz.json")

def submitQuiz(placeholder):
	for qi in range(len(testquiz.questions)):
		score = document.querySelector(f'input[name="answers{qi}"]:checked').value
		testquiz.giveAnswer(int(qi), int(score))
	result = testquiz.getResult()
	document.getElementById("result").innerHTML = "Result: " + categories[result]

document.getElementById("button").addEventListener("click", ffi.create_proxy(submitQuiz))

def createScale(name, qi, checked):
	radioHtml = ''
	for i in range(0,5):
		radioHtml += f'<input type="radio" id="q{qi}answer{i}" name="{name}" value="{i+1}"'
		if checked:
			radioHtml += ' checked="checked"'
		radioHtml += '/>'
	radioFragment = document.createElement('div')
	radioFragment.innerHTML = radioHtml

	currentDiv = document.getElementById("result")
	document.body.insertBefore(radioFragment, currentDiv.nextSibling)

	
# Interaction with HTML
for qi in range(len(testquiz.questions)):
	newDiv = document.createElement("div")
	newDiv.innerHTML = f'<p id="question{qi}">{testquiz.getQuestionString(qi)}</p>'
	currentDiv = document.getElementById("result")
	createScale(f'answers{qi}', qi, False)
	document.body.insertBefore(newDiv, currentDiv.nextSibling)

# def addElement(placeholder):
	# create a new div element
	# newDiv = document.createElement("div")

	# and give it some content
	# newContent = document.createTextNode("Hi there and greetings!")

	# add the text node to the newly created div
	# newDiv.appendChild(newContent)

	# add the newly created element and its content into the DOM
	# currentDiv = document.getElementById("question1")
	# print(currentDiv)
	# document.body.insertBefore(newDiv, currentDiv)