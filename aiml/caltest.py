#!python
# -*- coding: utf-8 -*-

import cal
import unittest
import datetime

class CalTest(unittest.TestCase):
	testdate = datetime.date(2011, 5, 12)
	def setUp(self):
		self.cal = cal.Cal()
	
	def testChineseformat(self):
		self.assertEqual(self.cal.chineseformat(self.testdate), u'2011年05月12日')

	def testToday(self):
		result = self.cal.today()
		self.assertEqual(self.cal.chineseformat(result), u'2011年05月12日')
	
	def testTomorrow(self):
		result = self.cal.tomorrow()
		self.assertEqual(self.cal.chineseformat(result), u'2011年05月13日')

	def testYesterday(self):
		result = self.cal.yesterday()
		self.assertEqual(self.cal.chineseformat(result), u'2011年05月11日')
	
	def testBefore(self):
		self.assertRaises(cal.OutOfRangeError, self.cal.before, -1, self.testdate)
		result = self.cal.before(3, self.testdate)
		self.assertEqual(result, datetime.date(2011, 5, 9))
	
	def testAfter(self):
		self.assertRaises(cal.OutOfRangeError, self.cal.after, -1, self.testdate)
		result = self.cal.after(3, self.testdate)
		self.assertEqual(result, datetime.date(2011, 5, 15))

	def testWeekday(self):
		result = self.cal.weekday(tod=self.testdate)
		self.assertEqual(result, u'周四')
		result = self.cal.weekday(prefix=u'星期', tod=self.testdate)
		self.assertEqual(result, u'星期四')
	
	def testmix(self):
		result = self.cal.after(3, self.cal.before(3, self.testdate))
		self.assertEqual(result, self.testdate)
		result = self.cal.weekday(tod=self.cal.after(2, self.testdate))
		self.assertEqual(result, u'周六')
	
	def testDateofweekday(self):
		self.assertRaises(cal.OutOfRangeError, self.cal.dateofweekday, -1, self.testdate)
		self.assertRaises(cal.OutOfRangeError, self.cal.dateofweekday, 7, self.testdate)
		result = self.cal.dateofweekday(0, self.testdate)
		self.assertEqual(result,datetime.date(2011, 5, 9)) 
		result = self.cal.dateofweekday(6, self.testdate)
		self.assertEqual(result,datetime.date(2011, 5, 15)) 
	
	def testchinese2num(self):
		for i in range(7):
			self.assertEqual(self.cal.chineseweek2num(self.cal.chineseweekday[i]), i)
		self.assertRaises(cal.OutOfRangeError, self.cal.chineseweek2num, u'九')
	
	def testParsechinesedate(self):
		self.assertEqual(cal.parsechinesedate(u"2011年5月12日"), datetime.date(2011, 5, 12))
if __name__ == "__main__":
	unittest.main()
