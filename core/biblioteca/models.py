from django.db import models

# Create your models here.

ESTADO_LIBRO = [
    ('IN', 'Biblioteca'),
    ('BW', 'Prestado'),
    ('RQ', 'Pedido'),
    ('RV', 'Reservado'),
]
class Material(models.Model):
    codigo = models.CharField(max_length=30)

class Libro(Material):
    editorial = models.CharField(max_length=30)
    fotoPortada = models.ImageField(max_length=100, blank=True)

class Revista(Material):
    pass

class Material(models.Model):
    codigo = models.CharField(max_length=20)
    autor = models.CharField(max_length=40)
    titulo = models.CharField(max_length=30)
    año = models.IntegerField()
    status = models.CharField(max_length=2, choices=ESTADO_LIBRO, default='En la biblioteca')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = ('Material Lectura')
        verbose_name_plural = ('Materiales de Lectura')

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.EmailField()
    telefono = models.IntegerField()
    num_libros = models.IntegerField()
    deuda = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    num_empleado = models.IntegerField()
    class Meta:
        verbose_name = ('Profesor')
        verbose_name_plural = ('Profesores')

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 30)
    fecha_salida = models.DateField(auto_now=False)
    fecha_regreso = models.DateField(auto_now=False)
    persona = models.ForeignKey('Persona',on_delete=models.CASCADE,null=False)
    material = models.ForeignKey('Material',on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.codigo
