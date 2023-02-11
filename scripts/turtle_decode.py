import turtle

with open("turtle", "r") as f:
	data = f.readlines()


def draw(pen: turtle.Turtle, line):
	if "droite" in line:
		msg = int(''.join(list(filter(str.isdigit, line))))
		pen.right(msg)
	elif "gauche" in line:
		msg = int(''.join(list(filter(str.isdigit, line))))
		pen.left(msg)
	elif "Recule" in line:
		msg = int(''.join(list(filter(str.isdigit, line))))
		pen.backward(msg)
	elif "Avance" in line:
		msg = int(''.join(list(filter(str.isdigit, line))))
		pen.forward(msg)
	elif line == "":
		pen.penup()
		pen.goto(0,0)
		pen.pendown()
	else:
		print([line])

pen = turtle.Turtle()
pen.speed(500)
pen.goto(0,0)
pen.setheading(-90)
pen.pendown()

for line in data:
	draw(pen, line.strip())

"""
{'Tourne droite de 150 degrees\n',
'Tourne gauche de 1 degrees\n',
'Avance 120 spaces\n',
'Recule 210 spaces\n',
'Recule 200 spaces\n',
'Avance 100 spaces\n',
'Tourne droite de 10 degrees\n',
'Tourne droite de 1 degrees\n',
'\n', 'Recule 100 spaces\n',
'Tourne droite de 120 degrees\n',
'Avance 200 spaces\n',
'Avance 210 spaces\n',
'Tourne gauche de 90 degrees\n',
'Tourne droite de 90 degrees\n',
'Can you digest the message? :)\n',
'Avance 1 spaces\n',
'Avance 50 spaces\n'}
"""
