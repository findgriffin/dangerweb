from libquote import *

qlist = quoteloader('quotelist.xml')
ind = makeindex(qlist)

save_quoter(qlist, ind, 'qlist.p', 'ind.p')
