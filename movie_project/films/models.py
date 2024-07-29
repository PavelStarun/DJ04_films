from django.db import models

class Movie(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    review = models.TextField("Отзыв")
    rating = models.DecimalField("Оценка", max_digits=3, decimal_places=1, default=0.0)
    link = models.URLField("Ссылка", blank=False, null=False, default="https://example.com")


    def __str__(self):
        return self.title
