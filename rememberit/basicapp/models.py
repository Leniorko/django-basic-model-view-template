from django.db import models

# Create your models here.
# Below example complete model for auto service

"""
Что может быть в бд для учёта оказаний услуг автосервиса?

Список услуг
Клиенты
Оказанные услуги

При желании можно распространить это дополнительными таблицами типа:

Тип машины
Может ещё что, мне думать лень
"""


# Список услуг
class Service(models.Model):
    # Явно задаю id, хоть он и автогенерируется
    id = models.BigAutoField(primary_key=True)
    # Имя услуги
    name = models.CharField(max_length=250)
    # Стоимость. Предположим что у нас они стоят без всяких копеек
    price = models.IntegerField()

    # Определяет как будет выглядеть запись в админке джанго
    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    current_car = models.CharField(max_length=250)
    # Содержить номер телефона в виде простой строки без всякой валидации. Бывает
    contact_number = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.surname


class PastService(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Foreign Key на клиента которому услуга оказана
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Дата и время указания услуги
    date = models.DateTimeField()

    # Будет использован __str__ с модели Client
    def __str__(self):
        return f"{self.client}: {self.date}"
