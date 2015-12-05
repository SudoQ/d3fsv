#coding:utf-8
import json
from os import walk


def parseFile(filename):
	with open(filename, "r") as f:
		return json.loads(f.read())

def newDir():
	d = {}
	d["name"] = ""
	d["children"] = []
	return d

def newFile(name, size):
	d = {}
	d["name"] = name
	d["size"] = size

if __name__ == "__main__":
	#parsedJSON = parseFile("example.json")
	#print(parsedJSON)

	#print(json.dumps(parsedJSON))
	mypath = "."
	f = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		print (dirpath, dirnames, filenames)
		f.extend(filenames)
		break
