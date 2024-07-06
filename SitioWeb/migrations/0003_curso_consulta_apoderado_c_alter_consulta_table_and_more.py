# Generated by Django 4.1.2 on 2024-07-06 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SitioWeb', '0002_delete_asistente_delete_imagen_delete_utp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCurso', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='apoderado_c',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='consulta',
            table='SitioWeb_consulta',
        ),
        migrations.AddField(
            model_name='consulta',
            name='curso',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='SitioWeb.curso'),
        ),
    ]
