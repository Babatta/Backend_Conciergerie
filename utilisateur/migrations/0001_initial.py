# Generated by Django 4.0.2 on 2022-02-22 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('telephone', models.IntegerField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('login', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('sexe', models.CharField(max_length=50, null=True)),
                ('cni', models.IntegerField(max_length=13, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]