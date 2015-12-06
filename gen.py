#coding:utf-8
import json
import Queue
from os import walk
from os import path


def parseFile(filename):
	with open(filename, "r") as f:
		return json.loads(f.read())

def newDir(name):
	d = {}
	d["name"] = name
	d["children"] = []
	return d

def newFile(name, size):
	f = {}
	f["name"] = name
	f["size"] = size
	return f

if __name__ == "__main__":
	#parsedJSON = parseFile("example.json")
	#print(parsedJSON)
	#print(json.dumps(parsedJSON))

	mypath = "."
	tuples = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		tuples.append((dirpath, dirnames, filenames))

	pathMap = {}
	root = newDir(".")
	pathMap["."] = root
	for (dirpath, dirnames, filenames) in tuples:
		#print (dirpath, dirnames, filenames)
		currentDir = pathMap[dirpath]
		for d in dirnames:
			child = newDir(d)
			currentDir["children"].append(child)
			pathMap[path.join(dirpath, d)] = child

		for f in filenames:
			currentDir["children"].append(newFile(f, 42))
		
		#print pathMap

	print json.dumps(root, indent=4)


			#	systemMap[dirpath] = {"dirs":dirnames, "files": filenames}

			#q = Queue.Queue()	
			#q.put(".")
			#current = root
			#while not q.empty():
			#	nextPath = q.get()
			#	currentDir = systemMap[nextPath]
			#	for d in currentDir["dirs"]:
			#		current["children"].append(d)
			
