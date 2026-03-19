import os, sys
from pathlib import Path

def main():
	wd = Path(".")
	target = Path("./src/Gallery")
	files = []
	for file in target.iterdir():
		if file.is_file():
			if file != "desktop.ini":
				files.append(file.name)
	thumbs = list(filter(lambda x: "THUMB" in x, files))
	with open("out.txt", "w") as f:
		for file in thumbs:
			f.write(f"<div class='SM gi' onclick='window.open(\"src/Gallery/{file.replace("-THUMB", "").replace(".jpg", ".png")}\");'><img class='SM' src='src/Gallery/{file}'></img></div>\n")
main()