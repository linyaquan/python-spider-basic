# -*- encoding: gb2312 -*-
import HTMLParser
import urllib2


class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.movies=[]



    def handle_starttag(self, tag, attrs):

        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        # �������¶����˴���ʼ��ǩ�ĺ���

        if tag == 'li' and _attr(attrs,'data-title'):
            # �жϱ�ǩ<a>������
            movie={} #test
            movie['title']=_attr(attrs,'data-title')
            movie['score']=_attr(attrs,'data-rate')
            movie['actors']=_attr(attrs,'data-actors')
            self.movies.append(movie)

            print "--" * 80
            print "%s-%s-%s"%(movie['title'],movie['score'],movie['actors'])




if __name__ == '__main__':
    s=urllib2.urlopen("https://movie.douban.com")
    rs=s.read()
    my = MyParser()
    # ����Ҫ���������ݣ���html��
    my.feed(rs)