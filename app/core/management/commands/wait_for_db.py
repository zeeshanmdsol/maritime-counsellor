"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
# from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                # Get the 'default' database connection
                # connection = connections['default']

                # Print DB name and other infos
                # database_name = connection.settings_dict['NAME']
                # database_host = connection.settings_dict['HOST']
                # database_port = connection.settings_dict['PORT']
                # database_user = connection.settings_dict['USER']
                # self.stdout.write(f'Connecting to database: {database_name}')
                # self.stdout.write(f'Connecting to database: {database_host}')
                # self.stdout.write(f'Connecting to database: {database_port}')
                # self.stdout.write(f'Connecting to database: {database_user}')

                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
