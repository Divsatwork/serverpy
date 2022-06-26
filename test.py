import web, json

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def POST(self, endpoint):
        print(web.ctx.env)
        if not endpoint:
            endpoint = ''
            return "ok"
        else:
            params = web.input()
            s = '&'.join([str(param[0]+'='+str(param[1])) for param in params.items()])
            print('/'+endpoint+s)
            print(json.loads(web.data()))
            return "got something"

if __name__ == "__main__":
    app.run()