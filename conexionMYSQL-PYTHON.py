import pymysql

class DataBase:

    def __init__(self):

        self.connection = pymysql.connect(
            
            #Dentro del aatributo debemos poner algunos parametros necesarios:

            host="localhost", #Si la base de datos es remota pones la ip
            
            user="root",
            password="Kyra_y_bruno_2021",
            db="bct"
        )

        #A cursor is an object which helps to execute the query and fetch the records from the database.
        #The cursor plays a very important role in executing the query. This article will learn some deep information about the execute methods
        #and how to use those methods in python.

        self.cursor = self.connection.cursor()

        print(f"Se ha establecido exitosamente la conexión con la base de datos")


    def select_user(self,id):
        sql = "SELECT idcliente, name, age FROM cliente WHERE idcliente = {}".format(id)

        try:
            self.cursor.execute(sql)

            #como solo nos va a retornar un solo registro 'por el where', entonces
            user = self.cursor.fetchone()

            #El fetchone sale para traer uno por uno de la lista que regresa
            print("Id: ", user[0])
            print("Username", user[1])
            print("Age: ", user[2])

        except Exception as e:
            raise

    def select_all_user(self):

        sql = "SELECT * FROM cliente"

        try:
            self.cursor.execute(sql)

            #Como ya no solo nos retorna un registro, sino más d euno

            users = self.cursor.fetchall()

            #Podemos iterar

            for user in users:
                print("Id: ", user[0])
                print("Document", user[1])
                print("Name: ", user[2])
                print("Age: ", user[3])
                print("Numero de cuenta: ", user[4])
                print("Status: ", user[5])
                print("Money_ID: ", user[6])
                print("---------------------")

        except Exception as e:
            raise
    
    def update_user(self, id, username):

        sql = "UPDATE cliente SET name = '{}' WHERE id = {}".format(username, id)

        try:

            self.cursor.execute(sql)

            #Esto nos servirá para que nuestro cambio persista en el tiempo
            self.connection.commit()
 
        except Exception as e:
            raise

database = DataBase()

database.select_user(1)
database.update_user(1, 'Pepe')
database.select_user(1)