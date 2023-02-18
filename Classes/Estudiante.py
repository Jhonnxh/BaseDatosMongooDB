from Classes.DbMongo import DBMongo
import pymongo
class Estudiante:

      def __init__(self,id, nombre, apellido, telefono):
            self.id=id
            self.nombre = nombre
            self.apellido = apellido
            self.telefono = telefono
        ##self.__collection = "Estudiante" decidi quitar esto porque al momento de guardar los datos en mongodb aparace escrita tambien la coleccion

      def save(self):
            client, db = DBMongo.getDB()
            collection = db["Estudiante"]
            collection.insert_one(self.__dict__)
            client.close()
      
      def update(self,id):
            clien, db  = DBMongo.getDB()
            collection = db["Estudiante"]
            collection.update_one(
                        {"id": id},
                        {"$set": { "nombre" : self.nombre , "apellido": self.apellido, "telefono": self.telefono}, })
            clien.close()