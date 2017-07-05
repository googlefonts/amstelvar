import os
import string

f = open('index.html', 'w')

header = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AmstelvarBeta</title>
</head>
<body>
"""
footer = """</body>
</html>
"""

f.write(header)
f.write("<style>\n")

for filename in os.listdir("instances"):
	if filename.endswith(".ttf"):
		fontface = "@font-face {font-family: '%s'; src: url('%s');}" % (filename, os.path.join("instances", filename))
		f.write(fontface)
		
f.write("</style>\n")

for filename in os.listdir("instances"):
	if filename.endswith(".ttf"):
		location = filename.replace("AmstelvarAlpha-VF", "").replace(".ttf", "").split("-")
		location = " ".join(location)
		f.write("<p>%s</p>"%(location))
		f.write("<p style=\"font-size: 50px;font-family: '%s';\">%s</p>" % (filename, string.printable))
		f.write("<hr/>")


f.write(footer)
f.close()