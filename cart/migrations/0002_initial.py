# Generated by Django 4.2.7 on 2024-04-14 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='labtest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.labtest', verbose_name='анализ'),
        ),
        migrations.AddField(
            model_name='cart',
            name='labtests',
            field=models.ManyToManyField(blank=True, through='cart.CartItem', to='main.labtest', verbose_name='анализы'),
        ),
    ]
