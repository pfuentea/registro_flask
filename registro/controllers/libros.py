from registro import app
from flask import request,flash,render_template,redirect,session 
from registro.models.libro import Libro

@app.route('/libros/new')
def new_libro():
    #1.-mostrar formulario para ingresar el nuevo dato
    return render_template("crear.html")

@app.route('/libro/create', methods=['POST'])
def create_libro():
    #1.-mostrar formulario para ingresar el nuevo dato
        #request.form aca viene la info del formulario (titulo)
    Libro.create(request.form)

    return redirect("/dashboard")
    

@app.route('/libros/editar/<int:id_libro>')
def editar_libro(id_libro):
    data={
        "libro_id":id_libro
    }
    libro=Libro.get_libro_by_id(data) 
    return render_template("editar.html",libro=libro)



@app.route('/libros/modificar', methods=['POST'])
def mod_libro():
    
    Libro.save(request.form)
    return redirect("/dashboard")