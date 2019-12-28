import web

# http://webpy.org/
# `easy_install web.py`
# `pip install lpthw.web`

# https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
# `brew services start mongodb-community@4.2`
# `ps aux | grep -v grep | grep mongod`
# `mongo`

urls = ('/.*', 'webhooks')

app = web.application(urls, globals())

class webhooks:
    def POST(self):
        # 1. Receive the webhook data.
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        return 'OK'
        # 2. Create the order.
        # 3. Recieve and handle the response.

if __name__ == '__main__':
    app.run()
