#!python
# -*- coding: utf-8 -*-

import datetime
import time

def parsechinesedate(chstr):
	return datetime.date.fromtimestamp(time.mktime(time.strptime(chstr, u"%Y年%m月%d日")))

class Cal:
	chineseweekday = u"一二三四五六日"
	def chineseformat(self, date):
		return date.strftime("%Y年%m月%d日").decode('utf8')

	def today(self):
		tod = datetime.date.today()
		return tod

	def tomorrow(self, tod=datetime.date.today()):
		tom = tod + datetime.timedelta(days=1)
		return tom

	def yesterday(self, tod=datetime.date.today()):
		yest = tod - datetime.timedelta(days=1)
		return yest

	def before(self, day, tod=datetime.date.today()):
		if not (day >= 0):
			raise OutOfRangeError, "the day should >= zero"
		date = tod - datetime.timedelta(days=day)
		return date

	def after(self, day, tod=datetime.date.today()):
		if not (day >= 0):
			raise OutOfRangeError, "the day should >= zero"
		date = tod + datetime.timedelta(days=day)
		return date

	def weekday(self, prefix=u'周', tod=datetime.date.today()):
		return prefix + self.chineseweekday[int(tod.weekday())]

	def dateofweekday(self, weekday, tod=datetime.date.today()):
		if not (-1 < weekday < 7):
			raise OutOfRangeError, "the weekday should in [0..6]"
		
		delta = weekday - tod.weekday()
		return tod + datetime.timedelta(days=delta)
	
	def chineseweek2num(self, c):
		if len(c)!=1 or self.chineseweekday.find(c) == -1:
			raise OutOfRangeError, "the chinese should in weekdays"
		return self.chineseweekday.find(c)	

class CalendarError(Exception): pass
class OutOfRangeError(CalendarError): pass
