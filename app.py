from Classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante(3,"Jhonny","Lara","32522021")
    estudiante.save()
    print("Estudiante guardado")
    estudiante.apellido="Hernandez"
    estudiante.update(3)
    print("Estudiante actualizado")
    #Si se va a guardar un dato elimine el metodo "update"
    #Si se va a actualizar un dato elimine el metodo "save" y especifique el id del objeto a actualizar
    
if __name__ == "__main__":
    load_dotenv()

    main()



