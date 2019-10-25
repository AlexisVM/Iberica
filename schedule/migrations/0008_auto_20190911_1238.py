# Generated by Django 2.2.1 on 2019-09-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_auto_20190724_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemental',
            name='j2',
            field=models.CharField(blank=True, choices=[('9:00 am - 10:30 am | José Galán', '9:00 am - 10:30 am | José Galán'), ('10:35 am - 12:05 pm | Nazaret Reyes (Tangos)', '10:35 am - 12:05 pm | Nazaret Reyes (Tangos)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='s3',
            field=models.CharField(blank=True, choices=[('NIVEL INTERMEDIO - Juan Paredes (Bailes festeros, bulerías)', 'NIVEL INTERMEDIO - Juan Paredes (Bailes festeros, bulerías)'), ('NIVEL AVANZADO - Javier LaTorre (Farruca)', 'NIVEL AVANZADO - Javier LaTorre (Farruca)'), ('NIVEL AVANZADO - Karen Lugo (Martinete)', 'NIVEL AVANZADO - Karen Lugo (Martinete)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='independiente',
            name='s9',
            field=models.CharField(blank=True, choices=[('NIÑOS INTERMEDIO - Nazaret Reyes (Alegrías)', 'NIÑOS INTERMEDIO - Nazaret Reyes (Alegrías)'), ('NIVEL BÁSICO - José Galán', 'NIVEL BÁSICO - José Galán'), ('NIVEL INTERMEDIO - El Carpeta (Seguiriyas)', 'NIVEL INTERMEDIO - El Carpeta (Seguiriyas)'), ('NIVEL INTERMEDIO - Eduardo Guerrero (Bulerías)', 'NIVEL INTERMEDIO - Eduardo Guerrero (Bulerías)'), ('NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)', 'NIVEL AVANZADO - María Moreno (Bata de Cola por Alegrías)'), ('NIVEL AVANZADO - Ana Morales (Seguiriya)', 'NIVEL AVANZADO - Ana Morales (Seguiriya)'), ('NIVEL PROFESIONAL - Pedro Córdoba', 'NIVEL PROFESIONAL - Pedro Córdoba')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i1m1',
            field=models.CharField(blank=True, choices=[('El Carpeta (Bulerías)', 'El Carpeta (Bulerías)'), ('Nazaret Reyes (Alegrías)', 'Nazaret Reyes (Alegrías)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i1m2',
            field=models.CharField(blank=True, choices=[('Rafael Estévez (Tangos)', 'Rafael Estévez (Tangos)'), ('Nazaret Reyes (Caña)', 'Nazaret Reyes (Caña)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i1v1',
            field=models.CharField(blank=True, choices=[('María Juncal (Fandangos)', 'María Juncal (Fandangos)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i1v2',
            field=models.CharField(blank=True, choices=[('Ana Morales (Alegrías de Córdoba)', 'Ana Morales (Alegrías de Córdoba)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i2m1',
            field=models.CharField(blank=True, choices=[('Eduardo Guerrero (Bulerías)', 'Eduardo Guerrero (Bulerías)'), ('El Carpeta (Seguiriyas)', 'El Carpeta (Seguiriyas)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i2m2',
            field=models.CharField(blank=True, choices=[('María Moreno (Romance)', 'María Moreno (Romance)'), ('Ana Morales (Guajira)', 'Ana Morales (Guajira)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i2v1',
            field=models.CharField(blank=True, choices=[('Karen Lugo (Bambera)', 'Karen Lugo (Bambera)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='intensivo',
            name='i2v2',
            field=models.CharField(blank=True, choices=[('Juan Paredes (Bailes festeros por bulerías)', 'Juan Paredes (Bailes festeros por bulerías)')], max_length=150),
        ),
    ]