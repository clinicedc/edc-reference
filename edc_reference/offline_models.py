from django.apps import apps as django_apps
from django_offline.offline_model import OfflineModel
from django_offline.site_offline_models import site_offline_models
from edc_base.model_mixins import ListModelMixin

offline_models = []
app = django_apps.get_app_config('edc_reference')
for model in app.get_models():
    if not issubclass(model, ListModelMixin):
        offline_models.append(model._meta.label_lower)

site_offline_models.register(offline_models, OfflineModel)
