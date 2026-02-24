# Generated manually for db_table rename

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("daily_track", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="dailytrack",
            table="daily_track",
        ),
    ]
