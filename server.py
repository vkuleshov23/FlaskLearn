import numpy.random as random
import random as shuffle
from ai import ArtificialIntelligence
from flask import Flask, redirect, render_template, request, jsonify
from urllib.request import urlretrieve
from PIL import ImageColor
import colorImg
import webInst

way = "db/"
allQuestionsFile = way+"AllQuestions.json"
mainQuestionsFile = way+"MainQuestions.json"
resultsFile = way+"Results.json"
webImgsFile = way+"WebImg.json"
webimage = "static/img/webImage.jpg"

AI = ArtificialIntelligence(allQuestionsFile, mainQuestionsFile, resultsFile, webImgsFile)
question = None
answer = None
webImages = AI.getWebImages()
shuffle.shuffle(webImages)
webImageIndex = random.randint(0, len(webImages))



def getBeginQuestion():
	global question
	question = AI.begin()
	return question

def getNextQuestion():
	global question
	question = AI.getNextQuestion(answer)
	return question

def getAnswersStr():
	global question
	context = {}
	context["question"] = str(question.getName())
	context["image"] = str(question.getImage())
	context["answers"] = []
	for answer in question.getAnswers():
			context["answers"].append({"answer" : str(answer.getName()), "pos": str(answer.getPosition())})
	return context

def getAnswer_(index):
	global answer
	global question
	answers = question.getAnswers()
	answer = answers.getAnswer(index)

def changeBGImage():
	global webImageIndex
	global webImages
	webImageIndex += 1
	if webImageIndex >= len(webImages)-1:
		webImageIndex = 0
	webInst.downloadImage(webImages[webImageIndex])

def getGradientColors():
	global webImageIndex
	global webImages
	colorMap = colorImg.colorz(webimage)
	colors = ""
	colorsForButton = ""
	for color in colorMap:
		clr = str(ImageColor.getcolor(color, "RGB"))
		clr = clr[:len(clr)-1]
		colors += ( (",rgba") +  clr + ", 0.5)")
		colorsForButton += ( (",rgba") +  clr + ", 0.8)")
	return colors, colorsForButton

def getImageStr():
	global webImages
	global webImageIndex
	changeBGImage()
	colors, colorsForButton = getGradientColors()
	context = {}
	context["imageURL"] = str(webImages[webImageIndex])
	context["imageURL2"] = str(webImages[webImageIndex+1])
	context["gradients"] = colors
	context["buttonColor"] = colorsForButton
	return context

def createApp():
	app = Flask(__name__)

	@app.route("/")
	def hello():
		context = getImageStr()
		return render_template("index.html", context=context)

	@app.route("/question")
	def quest():
		context = getAnswersStr()
		return render_template("question.html", context=context)

	@app.route("/begin")
	def begin():
		question = getBeginQuestion()
		return redirect("question")

	@app.route("/next")
	def next():
		question = getNextQuestion()
		if question != None:
			return redirect("question")
		else:
			return redirect("/result")

	@app.route("/answer", methods=['POST'])
	def answer():
		getAnswer_(int(request.form["position"]))
		return redirect("next")

	@app.route("/result")
	def results():
		result = AI.findPlace()
		return render_template("result.html", answer=result.getPlace(), image=result.getImage())


	return app