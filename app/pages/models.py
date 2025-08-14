from django.db import models

class Category(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Слаг", unique=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="dishes", verbose_name="Категория")
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    image = models.ImageField("Фото", upload_to="dishes/", blank=True, null=True)  # опционально
    is_visible = models.BooleanField("Показывать", default=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["category", "order", "name"]
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
