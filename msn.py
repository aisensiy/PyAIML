# -*- coding: utf-8 -*-

import msnp
import time


import aiml
import sys
from aiml.Kernel import k

loadfiles = ['aisen/main.xml', 'client.aiml']

def loadlearnfiles(kernel, files):
	for file in files:
		kernel.learn(file)

def prestart():
	loadlearnfiles(k, loadfiles)
	k.respond(u'加载系统标签')

class MsnChatListener(msnp.ChatCallbacks):
	def message_received(self, passport_id, display_name, text, charset):
		print "%s %s" % (display_name, text)
		self.chat.send_message(k.respond(text), charset)
	
#	def friend_joined(self, passport_id, display_name):
#		print "%s start a chat" % display_name

class MsnListener(msnp.SessionCallbacks):
	def chat_started(self, chat):
		callbacks = MsnChatListener()
		chat.callbacks = callbacks
		callbacks.chat = chat
		print chat.display_name, ' start a conversation'
#		chat.send_message('hi')

if __name__ == '__main__':
	msn = msnp.Session(MsnListener())
	msn.login('aisensiy@live.cn', '000000')
	
	prestart()
	
	while True:
		msn.process(chats=True)
		time.sleep(1)
		
