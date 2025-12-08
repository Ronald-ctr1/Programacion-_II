import json

class Medico:
    def __init__(self, idMed, nombreMed, apellidoMed,aniosExperiencia):
        self.idMed = idMed
        self.nombreMed = nombreMed
        self.apellidoMed = apellidoMed
        self.aniosExperiencia = aniosExperiencia

class Consulta(Medico):
    def __init__(self,idMed, nombreMed, apellidoMed,aniosExperiencia, ci, nombrePaciente, apellidoPaciente, dia, mes, anio):
        super().__init__(idMed, nombreMed, apellidoMed,aniosExperiencia)
        self.ci=ci
        self.nombrePaciente= nombrePaciente
        self.apellidoPaciente=apellidoPaciente
        self.dia=dia
        self.mes=mes
        self.anio=anio

    def to_dict(self):
        return {
            "idMed": self.idMed,
            "nombreMed": self.nombreMed,
            "apellidoMed": self.apellidoMed,
            "aniosExperiencia": self.aniosExperiencia,
            "ci": self.ci,
            "nombrePaciente": self.nombrePaciente,
            "apellidoPaciente": self.apellidoPaciente,
            "dia" : self.dia,
            "mes":self.mes,
            "anio": self.anio
        }


class Consultorio:
    def __init__(self, consultas, medicos):
        self.consultas = consultas
        self.medicos = medicos


    def agregar_consulta(self, consulta):
        self.consulta.append(consulta)

   

    def to_dict(self):
        return {
            "consultas": self.consultas,
            "medicos": self.medicos,
            
        }

    @staticmethod
    def from_dict(data):
        c = Consultorio(data["consultas"], data["medicos"])
        for d in data["consultas"]:
            c.agregar_consultas(
               Consulta(d["idMed"], d["nombreMed"], d["apellidoMed"], d["aniosExperiencia"], d["ci"], d["nombrePaciente"], d["apellidoPaciente"], d["dia"], d["mes"], d["mes"], d["anio"])
            )
        return c


class ArchivoConsultorio:
    def __init__(self, consultas):
        self.consultas = consultas

    def guardar(self, Consultorio):
        with open(self.consultas, "w") as archivo:
            json.dump(Consultorio.to_dict(), archivo, indent=4)

    def cargar(self):
        with open(self.consultas, "r") as archivo:
            data = json.load(archivo)
            return Consultorio.from_dict(data)



# Main
#a

c = Consultorio ("9","3")

c.agregar_consultas(Consulta(1000,"luis","salvador",3,190"grover","fluor",26,"enero",2015))
c.agregar_consultas(Consulta(1001,"luis","salvador",3,190"robet","gio",5,"enero",2015))
c.agregar_consultas(Consulta(1002,"luis","salvador",3,190"florencio","teran",6,"enero",2015))
c.agregar_consultas(Consulta(1003,"leo","ramos",1,191"felix","teres",3,"enero",2015))
c.agregar_consultas(Consulta(1004,"leo","ramos",1,191"adreianm","vaca",10,"enero",2015))
c.agregar_consultas(Consulta(1005,"leo","ramos",1,191"ruth","flores",11,"enero",2015))
c.agregar_consultas(Consulta(1006,"alex","gutierrez",10,192"ademar","choque",19,"enero",2015))
c.agregar_consultas(Consulta(1007,"ales","gutierrez",10,192"jjopsu","apaza",12,"enero",2015))
c.agregar_consultas(Consulta(1008,"ales","gutierrez",10,192"yamil","torrez",13,"enero",2015))

archivo = ArchivoConsultorio("consultorio.json")
archivo.guardar(c)

print("Archivo guardado.")

# baja

#c


