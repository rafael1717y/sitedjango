from django.db import models
from ordered_model.models import OrderedModel
from django.urls import reverse

# Create your models here.
class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descrico = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('modulos:detalhe', kwargs={'slug':self.slug})