from django.db import models

# Create your models here.

class Lesson(models.Model):
       # djangonun icindeki hazir olan authentication tablosundan bir tane
    # foreignKey aliyoruz
    # cunku her bir dersi bir kullaniciya ait olmali
   
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length = 50 ,verbose_name ="Ders Adi")
    content = models.CharField(max_length = 250 ,verbose_name ="Ders Aciklamasi",null=True)
    # bu bize o anki tarihi atar.Veri eklendiginde
    created_date = models.DateTimeField(auto_now_add=True)

    # def str bize admin panelinde lesson_name bilgisini ozellestirerek gosteriyor
    def __str_(self):
        return self.author
    
    #modelimizde en son eklenen en ustte gosterildi
    class Meta:
        ordering = ['-created_date']


class Attendance(models.Model):
    
    lesson = models.ForeignKey(Lesson,on_delete = models.CASCADE,verbose_name ="Ders Adi")
    attendance_date = models.DateTimeField(verbose_name ="Yoklama Tarihi")
    created_date = models.DateTimeField(auto_now_add = True)

    def __str_(self):
        return self.lesson

    class Meta:
        ordering = ['-created_date']
