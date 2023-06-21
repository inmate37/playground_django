# Django
from django.db import (
    migrations,
    models
)


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]
    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='datetime created')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='datetime updated')),
                ('dt_deleted', models.DateTimeField(blank=True, null=True, verbose_name='datetime deleted')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('name', models.CharField(default='', max_length=50, verbose_name='name')),
                ('surname', models.CharField(default='', max_length=50, verbose_name='surname')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'custom user',
                'verbose_name_plural': 'custom users',
                'ordering': ('-id',),
            },
        ),
    ]
