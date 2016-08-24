from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_protocol.model_mixins import EnrollmentCapMixin


class EnrollmentModel(EnrollmentCapMixin, BaseUuidModel):

    class Meta:
        app_label = 'example'
