from django.db import models

# Таблица категории имеющая поле с названием категории
class Сategory(models.Model):
    name = models.CharField(max_length=50)

    # Процедура возвращающая названия при преобразовании в строку, иначе будет объект
    def __str__(self):
        return self.name

# Описание должности, должности может быть активна, 
# При удалении isDeleted будет True. 
# Так как внешний ключ не даст удалить должность без удаления всех сотрудников, 
# то приходится Переходить к таким мерам 
class Position(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    
    def SetData(self, id, name, isActive):
        self.id = id
        self.name = name
        self.isActive = isActive
        
    # Процедура возвращающая названия при преобразовании в строку, иначе будет объект
    def __str__(self):
        return self.name
    
# Описание Сотрудника как в тз.
class Employee(models.Model):
    fullName = models.CharField(max_length=255)
    isMan = models.BooleanField(default=True) 
    # Возраст хранится в дате рождения, при запросе всех, преобразуется в цифру
    birthDay = models.DateTimeField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    category = models.ForeignKey(Сategory, on_delete=models.CASCADE)

    def SetData(self, id, fullName, isMan, birthDay, position, category):
        self.id = id
        self.fullName = fullName
        self.isMan = isMan
        self.birthDay = birthDay
        self.position = position
        self.category = category
