from libquote import *

qlist = quoteloader('quotelist.xml')
ind = makeindex(qlist)
keywords = ['bart', 'homer']
print 3 in [1, 2, 3]
print and_search(keywords, qlist)
print sort_results(or_search(keywords, ind), keywords)

# save_quoter(qlist, ind, 'qlist.p', 'ind.p')
