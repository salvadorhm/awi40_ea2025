import web  # Carga la libreria web.py

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render("views",base="master")

def notfound():
    return web.notfound(render.not_found())

def internalerror():
    return  web.internalerror(render.internal_error())

class Index:
    def GET(self):
        return render.index()



if __name__ == "__main__":
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()
