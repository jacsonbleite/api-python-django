from django.contrib import admin
from escola.models import Aluno

# criando admin aluno
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

# registrando aluno (Model, Class)
admin.site.register(Aluno, Alunos)
