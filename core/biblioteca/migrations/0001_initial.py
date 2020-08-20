# Generated by Django 2.2 on 2020-08-20 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Material')),
                ('editorial', models.CharField(max_length=30)),
                ('fotoPortada', models.ImageField(blank=True, upload_to='')),
            ],
            bases=('biblioteca.material',),
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='biblioteca.Material')),
            ],
            bases=('biblioteca.material',),
        ),
    ]