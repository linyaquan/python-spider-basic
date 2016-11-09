import urllib
import urllib2
import cookielib

def demo():
    print "hello world"


def read():
    rs=urllib.urlopen("http://doveic.com")
    headers={"User-Agent":"Chorme"}
    data={"username":"linyaquan","password":"xxxxx"}
    req = urllib2.Request("http://www.douban.com",data=urllib.urlencode(data),headers=headers)
    opener=urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1))
    s=opener.open(req)
    print s.read()

def handle_cookie():
    forms={'form_email':'linyaquan@qq.com','form_password':'l12345'}
    data='source=movie&redir=https%3A%2F%2Fmovie.douban.com%2F&form_email=linyaquan%40qq.com&form_password=l12345&login=%E7%99%BB%E5%BD%95'
    req=urllib2.Request("http://movie.douban.com",data=data)
    cj=cookielib.CookieJar()
    handlers=urllib2.HTTPCookieProcessor(cj)
    opener=urllib2.build_opener(handlers,urllib2.HTTPHandler(debuglevel=1))
    rs=opener.open(req)

    print rs.read()
    rs.close()









if __name__=="__main__":
    handle_cookie()
