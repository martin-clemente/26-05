from django.db import models

# --> Class + Nombre.
class Alumnos(models.Model):
    ID_Alumno=models.AutoField(primary_key=True)
    DNI=models.TextField(max_lenght=10)
    Apellido=models.TextField(max_lenght=35)
    Nombre=models.TextField(max_lenght=35)
    Edad=models.IntegerField()
    Calle=models.TextField(max_lenght=50)
    Altura=models.IntegerField()

    def __str__(self):
        return self.DNI