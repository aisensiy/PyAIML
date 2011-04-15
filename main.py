# -*- coding: utf-8 -*-

import aiml
from aiml.Kernel import k
#from xml.dom import minidom

loadfiles = ['aisen/main.xml']

def loadlearnfiles(kernel, files):
	for file in files:
		kernel.learn(file)

#def createcategory(pattern, template):
#	xmldoc = minidom.Document()
#	root = xmldoc.appendChild(xmldoc.createElement('aiml'))
#	cg = xmldoc.createElement('category')
#	pt = xmldoc.createElement('pattern')
#	pt.appendChild(xmldoc.createTextNode(pattern))
#	tp = xmldoc.createElement('template')
#	tp.appendChild(xmldoc.createTextNode(template))
#	cg.appendChild(pt)
#	cg.appendChild(tp)
#	root.appendChild(cg)
#	return xmldoc

#def addcategory(xmldoc, cgdom):
#	root = xmldoc.getElementsByTagName('aiml')[0]
#	cg = cgdom.getElementsByTagName('category')[0]
#	root.appendChild(cg)
#	return xmldoc
#
#def addtobrain(kernel, filename, xmldoc):
#	if not os.path.exists(filename):
#		file = codecs.open(filename, 'w', encoding='utf-8')
#		xmldoc.writexml(file, '', '\t', '\n')
#		file.close()
#	else:
#		file = codecs.open(filename, 'w+', encoding='utf-8')
#		xmldom = minidom.parse(file)
#		addcategory(xmldom, cg)
#		xmldom.writexml(file, '', '\t', '\n')
#		file.close()
#	kernel.learn(filename)

if __name__ == '__main__':
	loadlearnfiles(k, loadfiles)
#    k._brain.dump()
#	print k.respond(u"加载系统标签")
#	print k.respond(u'支持中文么')
#	print k.respond('bad answer')
#	print k.respond(u'支持中文的')
#	print k.respond(u'支持中文么')
#	print raw_input('>').encode('gbk', 'ignore').decode('utf8')
#	while True: print k.respond(raw_input('>'))
	#cgdom = minidom.parseString('<?xml version="1.0" encoding="utf-8"?><aiml><category><pattern>abc</pattern><template>def</template></category></aiml>')
	#cgdom = createcategory(u'在哦和你顾问', 'def')
#	orignaldom = createcategory('aaa', 'bbb')
#	addcategory(orignaldom, cgdom)
#	print orignaldom.toprettyxml(indent = '\t', newl='\n', encoding='utf-8')

