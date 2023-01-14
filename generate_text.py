printables = " .0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
printables_ascii = [32, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

print("supported characters: " + printables)
string = input("what text would you like converted (type \\ instead of newlines):\n ")

text = ">"

for i in range(0, len(string)):
	if string[i] == "\\":
		s = 10
		c = printables_ascii[j] - s
		text += '<++++++++++[>'
		for k in range(s):
			text += "+"
		text += "<-].[-]"
	else:
		for j in range(0, len(printables)):
			if printables[j] == string[i]:
				s = round(printables_ascii[j]/10)
				c = printables_ascii[j] - (s * 10)
				text += '<++++++++++[>'
				text += "+" * s
				text += "<-]>"
				if c < 0:
					text += "-" * -c
				elif c > 0:
					text += "+" * c
				text += ".[-]"

print(text)
