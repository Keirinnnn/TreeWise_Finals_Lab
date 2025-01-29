# Generated by Django 5.1.2 on 2024-10-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to=''),
        ),
    ]
