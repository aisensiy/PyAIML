# -*- coding: utf-8 -*-

import msnp
import time

class MsnListener(msnp.SessionCallbacks):
	def state_changed(self, state):
		if state == msnp.States.ONLINE:
			print 'online'

msn = msnp.Session(MsnListener())
msn.login('aisensiy@hotmail.com', 'muttian88')

while True:
	msn.process()
	time.sleep(1)
