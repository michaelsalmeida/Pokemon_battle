def conex():

    import mysql.connector

    mydb = mysql.connector.connect(

    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "gamepoke"

    )

    if mydb.is_connected():
        return mydb
    else:
        import sys
        print('Conexão falhou')
        sys.exit()
