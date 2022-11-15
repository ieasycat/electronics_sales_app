# Generated by Django 4.1.3 on 2022-11-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_networkelement_provider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='main.address'),
        ),
        migrations.AlterField(
            model_name='objectrelationship',
            name='type_object',
            field=models.CharField(choices=[('Завод', 'Завод'), ('Дистрибьютор', 'Дистрибьютор'), ('Дилерский центр', 'Дилерский центр'), ('Крупная розничная сеть', 'Крупная розничная сеть'), ('Индивидуальный предприниматель', 'Индивидуальный предприниматель')], max_length=255, verbose_name='Type provider'),
        ),
    ]
