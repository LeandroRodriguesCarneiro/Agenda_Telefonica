def criar(mysql,nome,sobrenome,email,telefone):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        sql = f"INSERT INTO contato (`Nome`, `Sobrenome`, `Email`, `Telefone`) VALUES ('{nome}', '{sobrenome}', '{email}', '{telefone}');"
        cursor.execute(sql)
        cursor.execute('SELECT LAST_INSERT_ID()')
        id_inserido = cursor.fetchone()[0]

        conn.commit()
        cursor.close()

        return id_inserido
    except:
        return 'Houve um problema e não foi possivel adionar o contato'

def ler(mysql,id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(f'SELECT `Nome`, `Sobrenome`, `Email`, `Telefone` FROM contato WHERE Id = {id}')
        data_query = cursor.fetchall()
        cursor.close()
        for nome,sobrenome,email,telefone in data_query:
            data={
                'nome':nome,
                'sobrenome': sobrenome,
                'email': email,
                'telefone': telefone
            }
        return data
    except:
        return 'Houve um problema e não foi possivel encontrar o contato'
    
def editar(mysql,nome,sobrenome,email,telefone,id_contato):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        sql = f"UPDATE contato SET `Nome` = '{nome}', `Sobrenome` = '{sobrenome}', `Email` = '{email}', `Telefone` = '{telefone}' WHERE Id = {id_contato};"
        cursor.execute(sql)
        conn.commit()
        cursor.execute(f'SELECT `Nome`, `Sobrenome`, `Email`, `Telefone` FROM contato WHERE Id = {id_contato}')
        data_query = cursor.fetchall()
        cursor.close()
        for nome,sobrenome,email,telefone in data_query:
            data={
                'nome':nome,
                'sobrenome': sobrenome,
                'email': email,
                'telefone': telefone
            }
        return data
    except:
        return 'Houve um problema e não foi possivel modificar o contato'
    
def apagar(mysql,id_contato):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        sql = f"DELETE FROM contato WHERE `contato`.`Id` = {id_contato}"
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    except:
        return 'Houve um problema e não foi possivel apagar o contato'
    
def buscar(mysql,busca):
    try:
        conn = mysql.connection
        cursor = conn.cursor()
        sql = f"SELECT `Nome`, `Sobrenome`, `Email`, `Telefone` FROM contato WHERE Nome LIKE '%{busca}%'"
        cursor.execute(sql)
        data_query = cursor.fetchall()
        data_list=[]
        for nome,sobrenome,email,telefone in data_query:
            data={
                'nome':nome,
                'sobrenome': sobrenome,
                'email': email,
                'telefone': telefone
            }
            data_list.append(data)

        cursor.close()
        return data_list
    except:
        return 'Houve um problema e não foi possivel buscar o contato'