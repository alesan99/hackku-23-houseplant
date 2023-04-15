from js import document, getTaxt
from pyodide import ffi
from backend.extraction import extractor 

# Upload and convert pdf somewhere here
def scan(placeholder):
	#fileContent
	#with open('./backend/syllubuses/syll.txt', 'r') as f:
	#	s = f.read()
	s = getTaxt()
	scanner = extractor()
	data = scanner.loadString(s)
	display(data)

# Important dates
def display(data):
	for i in range(len(data)):
		# newDiv = document.createElement("div")
		# newDiv.innerHTML = f'<p>{data[i][0]},{data[i][1]}</p>'
		document.getElementById("location1").innerHTML = f'{data[i][0]}'
		document.getElementById("date").innerHTML = f'{data[i][1]}'
		document.getElementById("time").innerHTML = f'{data[i][0]},{data[i][1]}'
		#document.body.insertBefore(newDiv, currentDiv)

document.getElementById("scanbutton").addEventListener("click", ffi.create_proxy(scan))

#display()