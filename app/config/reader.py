from typing import Final as const

from app.config.loader import settings


__all__ = (
    'database_url',
    'run_host',
    'run_port',
    'general_salt',
)


database_url: const = str(settings.database_url)
run_host: const = settings.run_host.get_secret_value()
general_salt: const = settings.database_general_salt.get_secret_value()
run_port: const = settings.run_port
