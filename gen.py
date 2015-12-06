#coding:utf-8
import json
import Queue
import os
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

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

if __name__ == "__main__":

	mypath = "."
	tuples = []
	pathMap = {}
	root = newDir(".")
	pathMap["."] = root
	for (dirpath, dirnames, filenames) in walk(mypath):
		#tuples.append((dirpath, dirnames, filenames))
		currentDir = pathMap[dirpath]
		for d in dirnames:
			child = newDir(d)
			currentDir["children"].append(child)
			pathMap[path.join(dirpath, d)] = child

		for f in filenames:
			size = path.getsize(path.join(dirpath, f))
			currentDir["children"].append(newFile(f, size))

	#for (dirpath, dirnames, filenames) in tuples:
		#print (dirpath, dirnames, filenames)
		
	print json.dumps(root, indent=4)
