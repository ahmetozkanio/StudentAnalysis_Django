from django.db import models

# Create your models here.

class Lesson(models.Model):
       # djangonun icindeki hazir olan authentication tablosundan bir tane
    # foreignKey aliyoruz
    # cunku her bir dersi bir kullaniciya ait olmali
   
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length = 50)
    
    # bu bize o anki tarihi atar.Veri eklendiginde
    created_date = models.DateTimeField(auto_now_add=True)

    # def str bize admin panelinde lesson_name bilgisini ozellestirerek gosteriyor
    def __str_(self):
        return self.lesson_name
    
    #modelimizde en son eklenen en ustte gosterildi
    class Meta:
        ordering = ['-created_date']