# A library for the Simpsons Quote App


import xml.etree.ElementTree as etree
import sys
from collections import defaultdict
import pickle
from operator import attrgetter

def save_quoter(qlist, index, qfilename, ifilename):
    """ Save a quotelist and index using pickle
    """
    qfile = open(qfilename, mode='w')
    ifile = open(ifilename, mode='w')
    pickle.dump(qlist, qfile)
    pickle.dump(index, ifile)

def load_quoter(qfilename, ifilename):
    """ Load a quotelist and index using pickle
    """
    qfile = open(qfilename, mode='r')
    ifile = open(ifilename, mode='r')
    return (pickle.load(qfile), pickle.load(ifile))

def or_search(keywords, index):
    """ Returns a list of all the quotes that contain
    at least one keyword.
    """
    list = []
    for key in keywords:
        if key in index:
            for quote in index[key]:
                if quote not in list:
                    list.append(quote)
    return list

def and_search(keywords, qlist):
    """ Returns a list of all the quotes
    that contain *every* keyword.
    """
    list = []
    for quote in qlist:
        keyinquote = True
        for key in keywords:
            if key in quote.keywords:
                continue
            else:
                keyinquote = False
                break
        if keyinquote:
            list.append(quote)
    return list

def sort_results(qlist, keywords):
    for quote in qlist:
        for key in keywords:
            if key in quote.keywords:
                quote.score = quote.score + quote.keywords[key]
    qlist.sort(key=attrgetter('score'), reverse=True)
    return qlist

def makeindex(qlist):
    """ Create a search index from a list of quotes
    returns a dictionary of lists
    where the keys are the search terms eg. 'homer'
    and the list contains all the quotes that
    mention 'homer'
    """
    index = defaultdict(list)
    for elem in qlist:
        for key in elem.keywords.keys():
            if key in index:
                index[key].append(elem)
            else:
                index[key] = [elem]
    return index


def quoteloader(filename):
    """import list of quotes from xml file
    file format:
    <quotelist>
    <quote epno='1.10' title='eptitle'>
    Character1: Quote
    Character2: Quote
    </quote>
    </quotelist>
    """
    tree = etree.parse(filename)
    xmquotes = []
    [xmquotes.append(child) for child in tree.getroot()]
    qlist = [Quote(elem.attrib['epno'], elem.attrib['title'], elem.text) for elem in xmquotes]
    return qlist

class Quote():
    "A class to represent a quote!"
    chars = []
    keywords = dict()
    title = ''
    epno = ''
    text = []
    score = 0 # temporary variable used when sorting results
    def __init__(self, epno, title, text):
        temp = text.strip()
        self.text = [elem.split(':') for elem in temp.split('\n')] # turn self.text into a list of lists
        self.chars = [] # so if this line is not included it only creates one instance of chars????
        [self.chars.append(elem[0]) for elem in self.text]
        self.chars = set(self.chars)
        self.epno = epno
        self.title = title
        self.keywords = dict()
        for line in temp.split('\n'):
            for word in line.split():
                if word not in self.keywords:
                    self.keywords[word.strip(""" ,./\<>?;:'"[]{}|-()!$""").lower()] = 1
                else:
                    self.keywords[word] = self.keywords[word] + 1

    def inc_keyword(key):
        self.keywords[key] = self.keywords[key] + 1
    
    def dec_keyword(key):
        self.keywords[key] = self.keywords[key] - 1

    def getScore(self):
        return self.score

    def __str__(self):
        outtext = self.epno+': '+self.title+'  Score: '+str(self.score)+'\n'
        for elem in self.text:
            outtext = outtext+elem[0]+':'+elem[1]+'\n'
        outtext = outtext+'Characters: '
        for elem in self.chars:
           outtext = outtext+elem+', '
        outtext = outtext+'\nKeywords: ' 
        for elem in self.keywords.keys():
            outtext = outtext+elem+', '
        return outtext

    def compare(self, other):
        """ other and self are reversed when calling cmp(self, other) so sort_results returns
        a list in descending order
        renamed from __cmp__ as it broke the or_search method
        """
        return cmp(other.score, self.score)
        
