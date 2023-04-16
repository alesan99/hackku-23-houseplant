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
		s = self.input.lower()
		self.data = []

		keywords = ["midterm", "exam", "test", "due"]
		cursor = 0
		# print("starting scan..")
		self.data.append(["Name","Date","Time"])
		while cursor < self.input_len and cursor >= 0:
			cursor = s.find('/', cursor+1, -1) # todo, use predefined key words
			if cursor != -1:
				# seperate the word by finding the surrounding spaces
				space1 = s.rfind(" ", 0,cursor+1)
				space2 = s.find(" ", cursor+1)

				# see if its a date and important by finding if there are important keywords nearby
				tolerance = 80
				important1 = cursor-tolerance-99999
				keyword1 = 0
				important2 = cursor+tolerance+99999
				keyword2 = 0

				for kw in range(len(keywords)):
					f1 = s.rfind(keywords[kw], 0,cursor+1)
					f2 = s.find(keywords[kw], cursor+1)
					if f1 > -1:
						important1 = max(important1, f1)
						keyword1 = keywords[kw]
					if f2 > -1:
						important2 = min(important2, f2)
						keyword2 = keywords[kw]

				if space1 != -1 and space2 != -1 and space1 != space2 and ((abs(important1-cursor) < tolerance) or (abs(important2-cursor) < tolerance)):
					dist1 = abs(important1-cursor)
					dist2 = abs(important2-cursor)
					closestkeyword = "Important Date"
					if dist1 < dist2:
						closestkeyword = keyword1.capitalize()
						kws1 = s.rfind(" ", 0, important1)
						kws1 = s.rfind(" ", 0, kws1-1)
						kws1 = s.rfind(" ", 0, important1+1)
						kws2 = s.find(" ", kws1+1)
					else:
						closestkeyword = keyword2.capitalize()
						kws1 = s.rfind(" ", 0, important2)
						kws1 = s.rfind(" ", 0, kws1-1)
						kws2 = s.find(" ", important2+1)
						kws2 = s.find(" ", kws2+1)
					possibledate = s[space1:space2+1].strip()
					possibledate = possibledate.replace("(","")
					possibledate = possibledate.replace(")","")
					possibledate = possibledate.replace(".","")
					possibledate2 = possibledate.replace("/","")
					
					if possibledate2.isdigit():
						name = s[kws1:kws2].strip()
						self.data.append([name.capitalize(), possibledate, "N/A"])
					# print("found at ", cursor)
		# self.data = [["midterm time", "1/7"]]
		# print("done!")
			
		return self.data
			

	def findPrefix():
		pass

	def findSuffix():
		pass
