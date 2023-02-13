import pycdlib
import sys

path = "/"
if len(sys.argv) > 1:
	path += sys.argv[1]

iso = pycdlib.PyCdlib()
iso.open('BornToSecHackMe-v1.1.iso')

for child in iso.list_children(iso_path=path):
	print(child.file_identifier().decode())

iso.close()
