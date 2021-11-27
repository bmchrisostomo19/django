import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('cursos', '0002_aulas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cursos.aulas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
    ]
