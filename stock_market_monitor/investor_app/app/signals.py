from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Asset
from .tasks import update_assets

@receiver(post_save, sender=Asset)
def schedule_asset_update(sender, instance, **kwargs):
    # Schedule the asset update task using Celery
    update_assets.apply_async(args=[instance.id], countdown=instance.interval * 60)