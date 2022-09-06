from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="نام")
    last_name = models.CharField(max_length=200, verbose_name="نام خانوادگی")
    username = models.CharField(max_length=200, verbose_name="نام کاربری")
    mobile = models.CharField(max_length=200, verbose_name="موبایل")

    def __str__(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)

    def getAll(self):
        return self.objects.all()

    def create(self, data=[]):
        self.objects.create(data)
        return self.save()

    def getById(self, data):
        return self.objects.get(data=data)

    def ascOrdesc(self, data):
        return self.objects.all().orderby(data)
