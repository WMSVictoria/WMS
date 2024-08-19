# Generated by Django 4.2.11 on 2024-08-13 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='inventory',
            name='section',
            field=models.CharField(choices=[('Section I', 'Section I'), ('Section II', 'Section II'), ('Section III', 'Section III'), ('Section IV', 'Section IV'), ('Section V', 'Section V')], default='Section I', max_length=20),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='location',
            field=models.CharField(choices=[('Melbourne', 'Melbourne'), ('Kilmore', 'Kilmore'), ('Stawell', 'Stawell'), ('Shepparton', 'Shepparton'), ('Hamilton', 'Hamilton')], max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
