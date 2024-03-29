from django.db import migrations

def create_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User(name="Joe Silver", email="joe@email.com", document="22342342", phone="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]