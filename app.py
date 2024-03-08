from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

## Configuración de la conexión a la base de datos
db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='',
                     database='crud de py',
                     cursorclass=pymysql.cursors.DictCursor)

##Ruta para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre = data['nombre']
    edad = data['edad']

    cursor = db.cursor()
    sql = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
    cursor.execute(sql, (nombre, edad))
    db.commit()

    return jsonify({'mensaje': 'Usuario creado correctamente'}), 201

## Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    return jsonify(usuarios)

## Ruta para obtener un usuario por su ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=%s", id)
    usuario = cursor.fetchone()
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404

## Ruta para actualizar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    nombre = data['nombre']
    edad = data['edad']

    cursor = db.cursor()
    sql = "UPDATE usuarios SET nombre=%s, edad=%s WHERE id=%s"
    cursor.execute(sql, (nombre, edad, id))
    db.commit()

    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

## Ruta para eliminar un usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", id)
    db.commit()
    return jsonify({'mensaje': 'Usuario eliminado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)
