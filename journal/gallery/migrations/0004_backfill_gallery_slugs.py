# Generated for backfilling empty image_slug on Gallery

import uuid
from django.db import migrations
from django.utils.text import slugify


def backfill_slugs(apps, schema_editor):
    Gallery = apps.get_model("gallery", "Gallery")
    for gallery in Gallery.objects.filter(image_slug=""):
        gallery.image_slug = (slugify(gallery.caption) if gallery.caption else "") or str(uuid.uuid4())[:8]
        gallery.save(update_fields=["image_slug"])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0003_gallery_excerpt"),
    ]

    operations = [
        migrations.RunPython(backfill_slugs, noop),
    ]
