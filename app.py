from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)


# Função de conexão com banco de dados
def pega_connetion():
    conn = sqlite3.connect('filmes.db')
    conn.row_factory = sqlite3.Row
    return conn
    

# Rota principal -- HomePage
@app.route('/')
def HomePage():
    conn = pega_connetion()
    filmes = conn.execute('SELECT * FROM filmes').fetchall()
    conn.close()
    return render_template('index.html', filmes=filmes)


# Rota de adicionar
@app.route('/adicionar', methods=('GET', 'POST'))
def AdicionarFilme():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        nota = request.form['nota']
        
        conn = pega_connetion()
        conn.execute('INSERT INTO filmes(titulo, genero, nota) VALUES (?, ?, ?)', 
                    (titulo, genero, nota))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('adicionarFilmes.html')

# Rota de editar
@app.route('/editar/<int:id>', methods=('GET', 'POST'))
def editarFilme(id):
    conn = pega_connetion()
    filme = conn.execute('SELECT * FROM filmes WHERE id = ?', (id,)).fetchone()
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        nota = request.form['nota']
        
        conn.execute('UPDATE filmes SET titulo = ?, genero = ?, nota = ? WHERE id = ?',
                     (titulo, genero, nota, id))
        conn.commit()
        conn.close()
        return redirect('/')

    conn.close()
    return render_template('editarFilme.html', filme=filme)


# Rota de Deletar
@app.route('/deletar/<int:id>')
def deletarFilme(id):
    conn = pega_connetion()
    conn.execute('DELETE FROM filmes WHERE id= ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

app.run(debug=True)