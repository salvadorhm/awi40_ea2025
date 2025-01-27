import web  # Carga la libreria web.py

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())
render = web.template.render("views")

class Index:
    def GET(self):
        return render.index()
    
    def POST(self):
        form = web.input()
        nombre = form.nombre
        email = form.email
        print(f"Nombre: {nombre}")
        print(f"Email: {email}")
        response = {
            "nombre":nombre,
            "email":email
        }
        return response

if __name__ == "__main__":
    app.run()
