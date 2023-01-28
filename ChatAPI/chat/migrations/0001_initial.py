# Generated by Django 4.1.5 on 2023-01-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('attachment', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.conversation')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
