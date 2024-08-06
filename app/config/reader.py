from typing import Final as const

from app.config.loader import settings


__all__ = (
    'database_url',
    'run_host',
    'run_port'
)


database_url: const = str(settings.database_url)
run_host: const = settings.run_host.get_secret_value()
run_port: const = settings.run_port
