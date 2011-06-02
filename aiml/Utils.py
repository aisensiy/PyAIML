# -*- coding: utf8 -*-
"""This file contains assorted general utility functions used by other
modules in the PyAIML package.

"""
import re

def chineseSplit(input):
	print 'split: \n', input
	result = re.sub(u'([\u2e80-\uffffa-zA-Z0-9])(?=[\u2e80-\uffff])', r'\1 ', input)
	result = re.sub(u'([\u2e80-\uffff])(?=[\u2e80-\uffffa-zA-Z0-9])', r'\1 ', result)
	print result
	return result

def chineseCon(output):
	print 'split: \n', output
	result = re.sub(u'([\u2e80-\uffffa-zA-Z0-9]) +(?=[\u2e80-\uffff])', r'\1', output)
	result = re.sub(u'([\u2e80-\uffff]) +(?=[\u2e80-\uffffa-zA-Z0-9])', r'\1', result)
	print result
	return result

def toUpperCase(strs):
	return strs.upper()	

def commandnormalize(command):
    """a util function to format the code in <system> tag"""
    newcommand = re.sub('(^\n+)|(\n+$)', '', command)
    cmds = newcommand.split('\n')
    firstindent = re.match('^(\s+)', cmds[0]).group(1)
    cmds = [re.sub('^' + firstindent + '|\s$', '', cmd) for cmd in cmds]
    return '\n'.join(cmds) + '\n'
#    print repr(firstindent)
#    print command
#    print '\n'.join(cmds)
    
def sentences(s):
    """Split the string s into a list of sentences."""
    try: s + ""
    except: raise TypeError, "s must be a string"
    pos = 0
    sentenceList = []
    l = len(s)
    while pos < l:
        try: p = s.index('.', pos)
        except: p = l + 1
        try: q = s.index('?', pos)
        except: q = l + 1
        try: e = s.index('!', pos)
        except: e = l + 1
        end = min(p, q, e)
        sentenceList.append(s[pos:end].strip())
        pos = end + 1
    # If no sentences were found, return a one-item list containing
    # the entire input string.
    if len(sentenceList) == 0: sentenceList.append(s)
    return sentenceList

# Self test
if __name__ == "__main__":
    # sentences
    sents = sentences("First.  Second, still?  Third and Final!  Well, not really")
    assert(len(sents) == 4)
    # cmd normalize
    cmd = '\n         echo hhh\n           echo bbbb\n      \t\t'
    print commandnormalize(cmd)
    sss = u'测 试 测 试 ali ce'
    sss2 = u'测试测试 alice'
    print repr(sss)
    print chineseCon(sss)
    print chineseSplit(sss2)

