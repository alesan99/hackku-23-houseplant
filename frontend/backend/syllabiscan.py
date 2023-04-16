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
	t1 = '<table>'
	for i in range(len(data)):
		# newDiv = document.createElement("div")
		# newDiv.innerHTML = f'<p>{data[i][0]},{data[i][1]}</p>'
		t1 += '<tr>'
		for i2 in range(len(data[i])):
			t1 += f'<th>{data[i][i2]}</th>'
		t1 += '</tr>'
	t1 += '</table>'
	document.getElementById("important_dates").innerHTML = t1

document.getElementById("scanbutton").addEventListener("click", ffi.create_proxy(scan))

#display()