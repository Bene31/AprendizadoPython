import MySQLdb
#pip install mysqlclient -> cmd

host = "localhost"
user = "root"
password = ""
db = "udemy"
port = 3307

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):
	
	global c
	
	query = "select " + fields + " from " + tables
	if (where):
		query = query + " where " + where
	
	c.execute(query)
	return c.fetchall()
	
result = select("nome, cpf", "alunos", "id_aluno = 3")

#print(result)


def insert(values, table, fields=None):
	
	global c, con
	
	query = "insert into " + table
	if (fields):
		query = query + " (" + fields + ") "
	query = query + " VALUES " + ",".join(["(" + v + ")" for v in values]) 
	
	c.execute(query)
	con.commit()
	
	values = [
	"DEFAULT, 'Douglas', '2000-01-01', 'rua c', 'Rio de Janeiro', 'RJ', '789692564'",
	"DEFAULT, 'Edu', '1759-04-21', 'rua c', 'Rio de Janeiro', 'RJ', '789514564'"
	]

#insert(values, "alunos")


def update(sets, table, where):
	
	global c, con
	
	query = "update " + table + " set " + ",".join([field + " = '" + value + "'" for field, value in sets.items()]) + " where " + where
	
	c.execute(query)
	con.commit()
		
#update({"nome":"Carlos"}, "alunos", "id_aluno = 3")


def delete(table, where):
	
	global c, con
	
	query = "delete from " + table + " where " + where
	
	c.execute(query)
	con.commit()
	
#delete("alunos", "id_aluno = 4")

