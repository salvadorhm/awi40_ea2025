import web  # Carga la libreria web.py

urls = (
    '/', 'Hello',
    '/bye', 'Bye'
)
app = web.application(urls, globals())

class Hello:
    def GET(self):
        return 'Hello, Web.py!'

class Bye:
    def GET(self):
        return 'Bye, Web.py!'


if __name__ == "__main__":
    app.run()
