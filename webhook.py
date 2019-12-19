import web

# http://webpy.org/
# `easy_install web.py`
# `pip install lpthw.web`

urls = ('/.*', 'webhooks')

app = web.application(urls, globals())

class webhooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        return 'OK'

if __name__ == '__main__':
    app.run()
