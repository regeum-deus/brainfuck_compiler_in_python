import os

tabs = 1
tab = "  "

file_content = [
	'#include <stdio.h>',
	'int main() {',
	'  char temp_c;',
	'  int temp_i;'
	'  int *cells = calloc(30000, sizeof(int));',
	'  int index = 0;',
]

file = open(input("file path/name: "))
data = file.read()
file.close()

for i in range(len(data)):
	if data[i] == ">":
		file_content.append((tab * tabs) + 'index += 1;')
	if data[i] == "<":
		file_content.append((tab * tabs) + 'index -= 1;')
	if data[i] == "+":
		file_content.append((tab * tabs) + 'cells[index] += 1;')
	if data[i] == "-":
		file_content.append((tab * tabs) + 'cells[index] -= 1;')
	if data[i] == ".":
		file_content.append((tab * tabs) + 'printf("%c", cells[index]);')
	if data[i] == ",":
		file_content.append((tab * tabs) + 'scanf("input: %c", &temp_c);')
		file_content.append((tab * tabs) + 'temp_i = temp_c;')
		file_content.append((tab * tabs) + 'cells[index] = temp_i;')
	if data[i] == "[":
		file_content.append((tab * tabs) + 'while(cells[index] != 0) {')
		tabs += 1
	if data[i] == "]":
		tabs -= 1
		file_content.append((tab * tabs) + '}')

file_content.append("  free(cells);")
file_content.append("  return 0;")
file_content.append("}")
file_content.append("")

with open("main.c", "w") as file:
   data = "\n".join(file_content)
   file.write(data)

os.system("gcc main.c -o main.exe")

