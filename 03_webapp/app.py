import web  # Carga la libreria web.py

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render("views")

class Index:
    def GET(self):
        mensaje = "Hola python y html"
        return render.index(mensaje)

if __name__ == "__main__":
    app.run()
