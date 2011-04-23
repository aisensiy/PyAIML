# -*- coding: utf-8 -*-

import aiml
import sys
from aiml.Kernel import k
#from xml.dom import minidom

loadfiles = ['aisen/main.xml', 'client.aiml']

def loadlearnfiles(kernel, files):
	for file in files:
		kernel.learn(file)

if __name__ == '__main__':
	loadlearnfiles(k, loadfiles)
	print k.respond(u"加载系统标签")
	while True: print k.respond(raw_input('>'))#.encode(sys.argv[1], 'ignore').decode('utf8'))
