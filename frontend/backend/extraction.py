import json

class extractor:
	def __init__(self):
		self.input = ""
		self.input_len = 0
		self.out = {}

	def loadString(self, s): # s: converted plain text
		self.input = s
		self.input_len = len(self.input)
		return self.read()

	def read(self):
		s = self.input
		self.data = []
		cursor = 0
		# print("starting scan..")
		while cursor < self.input_len and cursor >= 0:
			cursor = s.find('/', cursor+1, -1) # todo, use predefined key words
			if cursor != -1:
				space1 = s.rfind(" ", 0,cursor+1)
				space2 = s.find(" ", cursor+1)
				if space1 != -1 and space2 != -1 and space1 != space2 :
					self.data.append(["Midterm Day", s[space1:space2+1]])
					# print("found at ", cursor)
		# self.data = [["midterm time", "1/7"]]
		# print("done!")
			
		return self.data
			

	def findPrefix():
		pass

	def findSuffix():
		pass
