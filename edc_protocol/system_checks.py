from django.core.management import color_style
from edc_utils.dashboard_middleware_check import edc_middleware_check

style = color_style()


def middleware_check(app_configs, **kwargs):
    return edc_middleware_check(
        app_configs,
        app_label="edc_protocol",
        middleware_name="edc_protocol.middleware.ResearchProtocolConfigMiddleware",
        error_code=None,
        **kwargs,
    )
