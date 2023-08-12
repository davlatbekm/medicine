from django.db import models


class Contact(models.Model):
    author = models.OneToOneField("main.hospital", on_delete=models.CASCADE, related_name="contacts")

    phone = models.CharField("Телефон", max_length=12)
    email = models.EmailField("Эл.почта")
    photo = models.ImageField(upload_to='media')
    works = models.TextField(max_length=200)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self) -> str:
        return f"Контакты {self.author}"
