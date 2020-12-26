import inject
from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        from polls.inject_config import default_config
        """
        DI設定
        アプリケーションにおいてどのDI設定を使うかを注入するか設定する
        """
        inject.configure_once(default_config)
