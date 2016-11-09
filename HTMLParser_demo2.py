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

        # 这里重新定义了处理开始标签的函数

        if tag == 'li' and _attr(attrs,'data-title'):
            # 判断标签<a>的属性
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
    # 传入要分析的数据，是html。
    my.feed(rs)