from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import re

from DB import criar,ler,editar,apagar,buscar
load_dotenv()

app = Flask(__name__) 
app.config['MYSQL_HOST'] = os.getenv('HOST')
app.config['MYSQL_USER'] = os.getenv('USER')
app.config['MYSQL_PASSWORD'] = os.getenv('PSW')
app.config['MYSQL_DB'] = os.getenv('DB')
mysql = MySQL(app)

@app.post('/adicionar')
def adicionar_contato():
    request_data = request.get_json()
    obrigatorios = ['Nome','Telefone']
    nome=''
    telefone=''
    for campo in obrigatorios:
        if campo not in request_data:
            return jsonify(f'Esta faltando o campo {campo}'),401
        if len(request_data[campo]) <= 0:
            return jsonify(f'O campo {campo} nao pode estar vazio'),401
        elif len(request_data[campo]) > 100:
            return jsonify(f'O campo {campo} nao pode ser maior que 100'),401
        else: 
            if campo == 'Nome':
                nome = request_data['Nome']
            if campo == 'Telefone':
                if len(request_data[campo]) > 20:
                    return jsonify(f'O campo {campo} nao pode ser maior que 20'),401
                else:
                    telefone = request_data['Telefone']

    opcionais = ['Email','Sobrenome']
    sobrenome=''
    email=''
    for campo in opcionais:
        if campo in request_data:
            if len(request_data[campo]) > 100:
                return jsonify(f'O campo {campo} nao pode ser maior que 100'),401
            else:
                if campo == 'Email':
                    if re.match(r'[A-Za-z0-9_]+@[a-zA-Z0-9]+[.][a-z]+|[A-Za-z0-9_]+@[a-zA-Z0-9][.][a-zA-Z0-9]+[.][a-z]+',request_data[campo]):
                        email = request_data['Email']
                    else:
                        jsonify('email invalido'),401
                if campo == 'Sobrenome':
                    sobrenome = request_data['Sobrenome']
    
    id_inserido = criar(mysql,nome,sobrenome,email,telefone)
    if type(id_inserido) == str:
        return jsonify({id_inserido}),400
    return jsonify({'id_contato':id_inserido}),201
        

@app.get('/ler')
def obter_contato():
    request_data = request.get_json()
    if 'id_contato' in request_data:
        if request_data['id_contato'] > 0:
            id = request_data['id_contato']
            data = ler(mysql, id)
            if type(data) == str:
                return jsonify(data),400
            return jsonify(data),200
        else:
            return jsonify('O id fornecido nao pode ser menor que 0'),401
    else:
        return jsonify('O campo id_contato precisa ser fornecido')
        
@app.post('/atualizar')
def atualizar_contato():
    request_data = request.get_json()
    if 'id_contato' in request_data:
        if request_data['id_contato'] <= 0:
            return jsonify(f'O campo id_contato nao pode ser menor que 0'),401
        else:
            id_contato = request_data['id_contato']
    obrigatorios = ['Nome','Telefone']
    nome=''
    telefone=''
    for campo in obrigatorios:
        if campo not in request_data:
            return jsonify(f'Esta faltando o campo {campo}'),401
        if len(request_data[campo]) <= 0:
            return jsonify(f'O campo {campo} nao pode estar vazio'),401            
        if len(request_data[campo]) > 100:
            return jsonify(f'O campo {campo} nao pode ser maior que 100'),401
        else: 
            if campo == 'Nome':
                nome = request_data['Nome']
            if campo == 'Telefone':
                if len(request_data[campo]) > 20:
                    return jsonify(f'O campo {campo} nao pode ser maior que 20'),401
                telefone = request_data['Telefone']
    opcionais = ['Email','Sobrenome']
    sobrenome=''
    email=''
    for campo in opcionais:
        if campo in request_data:
            if len(request_data[campo]) > 100:
                return jsonify(f'O campo {campo} nao pode ser maior que 100'),401
            else:
                if campo == 'Email':
                    if re.match(r'[A-Za-z0-9_]+@[a-zA-Z0-9]+[.][a-z]+|[A-Za-z0-9_]+@[a-zA-Z0-9][.][a-zA-Z0-9]+[.][a-z]+',request_data[campo]):
                        email = request_data['Email']
                    else:
                        jsonify('email invalido'),401
                if campo == 'Sobrenome':
                    sobrenome = request_data['Sobrenome']
    data = editar(mysql,nome,sobrenome,email,telefone,id_contato)
    if type(data) == str:
        return jsonify(data),400
    return jsonify(data),200
    

@app.delete('/deletar')
def delete():
    request_data = request.get_json()
    if 'id_contato' in request_data:
        if request_data['id_contato'] <= 0:
            return jsonify(f'O campo id_contato nao pode ser menor que 0'),401
        else:
            id_contato = request_data['id_contato']
        data = apagar(mysql,id_contato)
        if type(data) == str:
            return jsonify(data),400
        return jsonify('Contato apagado com sucesso'),200
    else:
        return jsonify('Precisa conter o campo id_contato com o id desejado'),401

@app.route('/Busca')
def buscar_contato():
    busca = request.args.get('buscar')
    data_list = buscar(mysql,busca)
    return jsonify(data_list), 200

if __name__ == '__main__': 
    app.run(debug = True) 