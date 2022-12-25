# Generated by Django 4.1.4 on 2022-12-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_adicional"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="classificacao",
            field=models.CharField(
                choices=[
                    ("ENTRADA", "Entradas"),
                    ("PRATOPRINCIPAL", "Pratos Principais"),
                    ("BEBIDA", "Bebidas"),
                    ("SOBREMESA", "Sobremesas"),
                ],
                max_length=20,
            ),
        ),
    ]
