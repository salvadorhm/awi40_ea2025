import web  # Carga la libreria web.py

urls = (
    '/', 'Index',
    '/bienvenida', 'Bienvenida'
)

app = web.application(urls, globals())
render = web.template.render("views")

class Index:
    def GET(self):
        mensaje = "Hola python y html"
        return render.index(mensaje)

class Bienvenida:
    def GET(self):
        return render.bienvenida()

if __name__ == "__main__":
    app.run()