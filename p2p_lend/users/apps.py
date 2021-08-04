from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "p2p_lend.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import p2p_lend.users.signals  # noqa F401
        except ImportError:
            pass
