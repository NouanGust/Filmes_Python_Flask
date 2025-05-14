from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)

# Função para conectar no banco de dados
def pega_connection():
    conn = sqlite3.connect('filmes.db')
    conn.row_factory = sqlite3.Row
    return conn

# HomePage
@app.route('/')
def Home():
    conn = pega_connection()
    filmes = conn.execute('SELECT * FROM filmes').fetchall()
    conn.close()
    return render_template('filmes.html', filmes=filmes)



# Função CREATE

@app.route('/adicionar', methods=('GET', 'POST'))
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        nota = request.form['nota']
        
        conn = pega_connection()
        conn.execute('INSERT INTO filmes (titulo, genero, nota) VALUES (?, ?, ?)', 
                     (titulo, genero, nota))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('adicionar.html')


if __name__ == '__main__':
    app.run(debug=True)      
