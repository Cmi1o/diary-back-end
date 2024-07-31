from typing import Final as const

from app.config.reader import settings


__all__ = (
    'database_url',
    'run_host',
    'run_port',
)


database_url: const = str(settings.database_url)
run_host: const = settings.host.get_secret_value()
run_port: const = settings.port
