from libquote import *
import simpsons.models


def build_database(quotelist):
    keys = set()
    [keys.update(elem.keywords) for elem in quotelist]
    chars = set()
    [chars.update(elem.chars) for elem in quotelist]
    [Character(name=elem).save() for elem in chars]
    [Keyword(word=elem, score=0).save() for elem in keys]
    for elem in quotelist:
        series = int(elem.epno.split(".")[0])
        ep_no = int(elem.epno.split(".")[1])
        txt = elem.html_text()
        q = simpsons.models.Quote(season=series,\
                epno=ep_no,text=txt,source=u'The Simpsons',\
                popularity=0,title=elem.title)
        q.save()
        for key in elem.keywords:
            kword = Keyword.objects.filter(word=key)[0]
            q.keywords.add(kword)
        for char in elem.chars:
            chr = Character.objects.filter(name=char)[0]
            q.characters.add(chr)
# save_quoter(qlist, ind, 'qlist.p', 'ind.p')
