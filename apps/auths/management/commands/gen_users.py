# Python
import random
import itertools
from typing import Any

# Third party
import names

# Django
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.db import IntegrityError

# First party
from abstracts.decorators import performance_counter
from auths.models import CustomUser


class Command(BaseCommand):
    help = 'Command.'

    @performance_counter
    def generate_superuser(self) -> None:
        data: dict[str, str] = {
            'email': 'root@mail.cc',
            'password': '123'
        }
        if CustomUser.objects.filter(email=data['email']).exists():
            return

        CustomUser.objects.create_superuser(**data)

    @performance_counter
    def generate_users(self) -> None:

        def _generate_email(name: str, surname: str) -> str:
            email_options: tuple[str, ...] = (
                'gmail.com',
                'outlook.com',
                'hotmail.com',
                'yahoo.com',
                'yandex.ru',
                'mail.ru'
            )
            return f'{name}.{surname}@{random.choice(email_options)}'.lower()

        def _generate_password(name: str, surname: str) -> str:
            number: int = random.randint(100000, 999999)
            raw_password: str = f'@{name}%{surname}&{number}*'
            return make_password(raw_password)

        COUNT: int = 100
        count_current: int = CustomUser.objects.count()
        if count_current >= COUNT:
            return

        objs: list[CustomUser] = []
        count_diff: int = COUNT - count_current

        while count_diff > 0:
            name: str = names.get_first_name()
            surname: str = names.get_last_name()
            email: str = _generate_email(name, surname)
            data: dict[str, str] = {
                'email': email,
                'password': _generate_password(name, surname),
                'name': name,
                'surname': surname
            }
            objs.append(CustomUser(**data))
            count_diff -= 1

        try:
            CustomUser.objects.bulk_create(objs)
        except IntegrityError as exc:
            print(f'ERROR: {exc}')
            return

        #-------------------------------------------------
        # DOCS
        #
        # # NOTE: default is to create all objects in one batch
        # #       SQLite allows creating maximum of 999 objs per query
        # #
        # batch_size: int = 999
        # while True:
        #     batch: list = list(
        #         itertools.islice(objs, batch_size)
        #     )
        #     if not batch:
        #         break
        #
        #     # NOTE: bulk_create already uses atomic-transactions
        #     #       no need for using: with transactions.atomic()
        #     #
        #     CustomUser.objects.bulk_create(batch, batch_size)

    @performance_counter
    def handle(self, *args: Any, **kwargs: Any) -> None:
        self.generate_superuser()
        self.generate_users()
