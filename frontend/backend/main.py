import json
from js import document, alert, window
from pyodide import ffi
from backend.quiz import Quiz
from backend.characteristics import characteristicsList


# Load Questions
characteristics_list = characteristicsList('./backend/characteristics.json')
categories = characteristics_list.categories
quiz = Quiz("./quiz.json")

def submitQuiz(placeholder):
	for qi in range(len(quiz.questions)):
		score = 0
		select = document.querySelector(f'input[name="answers{qi}"]:checked')
		if select:
			score = select.value
		quiz.giveAnswer(int(qi), int(score))
	result = quiz.getResult()
	document.getElementById("result").innerHTML = "Result: " + categories[result]
	alert("Result: " + categories[result].capitalize())
	window.location.replace("./results.html")


def createScale(name, qi, checked):
	radioHtml = f'<div class="question"><p>{quiz.getQuestionString(qi)}</p><div class="radios"><p>agree</p>'
	for i in range(0,5):
		radioHtml += f'<input type="radio" id="radio{i+1}" name="{name}" value="{i+1}"'
		if checked:
			radioHtml += ' checked="checked"'
		radioHtml += '/>'
	radioHtml += '<p>disagree</p></div>'
	return radioHtml
	# radioFragment = document.createElement('div')
	# radioFragment.innerHTML = radioHtml

	# currentDiv = document.getElementById("inserted")
	# currentDiv.innerHTML = radioHtml

	
# Interaction with HTML
addHtml = '<div class="quizform">'
for qi in range(len(quiz.questions)):
	newDiv = document.createElement("div")
	newDiv.innerHTML = f'<p id="question{qi}">{quiz.getQuestionString(qi)}</p>'
	currentDiv = document.getElementById("insert-questions-here")
	addHtml += createScale(f'answers{qi}', qi, False)
	# document.body.insertBefore(newDiv, currentDiv.nextSibling)
addHtml += '</div><div id="button"><input type="submit" value="Submit" id="submit"></div></div>'
currentDiv = document.getElementById("inserted")
currentDiv.innerHTML = addHtml

# document.getElementById("submit").addEventListener("click", ffi.create_proxy(submitQuiz))
document.getElementById("button").addEventListener("click", ffi.create_proxy(submitQuiz))

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