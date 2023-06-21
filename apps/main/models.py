# Python
from typing import Any
from decimal import Decimal

# Django
from django.core.exceptions import ValidationError
from django.db.models import (
    CASCADE,
    PROTECT,
    Avg,
    CharField,
    Count,
    ForeignKey,
    IntegerField,
    Manager,
    ManyToManyField,
    Model,
    OneToOneField
)
from django.db.models.query import QuerySet


class TeamManager(Manager):
    """TeamManager."""

    def get_incomplete_teams(self) -> QuerySet['Team']:
        return self.annotate(
            player_count=Count('players__id')
        ).filter(
            player_count__lt=Team.PLAYERS_COUNT
        )


class Team(Model):
    """Team."""

    PLAYERS_COUNT: int = 11

    title = CharField(
        max_length=25,
        verbose_name='название'
    )

    objects = TeamManager()

    @property
    def power(self) -> Decimal:
        return Decimal(
            str(
                round(
                    sum(
                        player.power for player in self.players.all()
                    ) / self.PLAYERS_COUNT, 1
                )
            )
        )

    @property
    def is_team_completed(self) -> bool:
        return bool(self.players.count() == self.PLAYERS_COUNT)

    class Meta:
        ordering = ('title',)
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self) -> str:
        return f'{self.title} | {self.power}'


class PlayerManager(Manager):
    """PlayerManager."""

    def get_free_agents(self) -> QuerySet['Player']:
        return self.filter(
            team__isnull=True
        )


# # Strength
# # Perception
# # Endurance
# # Intelligence
# # Agility


# class Attribute(Model):
#     """Attribute."""

#     title = models.CharField(
#         max_length=25,
#         verbose_name='название'
#     )
#     value = models.CharField(
#         max_length=25,
#         verbose_name='значение'
#     )

#     class Meta:
#         ordering = ('-id',)
#         verbose_name = 'атрибут'
#         verbose_name_plural = 'атрибуты'

#     def __str__(self) -> str:
#         return f'{self.title} | {self.value}'


class Player(Model):
    """Player."""

    name = CharField(
        max_length=25,
        verbose_name='имя'
    )
    surname = CharField(
        max_length=25,
        verbose_name='фамилия'
    )
    power = IntegerField(
        verbose_name='сила'
    )
    team = ForeignKey(
        Team,
        on_delete=PROTECT,
        related_name='players',
        verbose_name='команда',
        null=True,
        blank=True
    )

    objects = PlayerManager()

    class Meta:
        ordering = ('-power',)
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self) -> str:
        return f'{self.name} {self.surname} | {self.power}'

    def clean(self) -> None:
        if self.power > 10:
            raise ValidationError(
                {
                    'power': 'Power cannot be more than 10'
                }
            )
        if self.team and self.team.players.count() <= Team.PLAYERS_COUNT:
            raise ValidationError(
                {
                    'team': 'Cannot switch team unless more players in current one'  # noqa
                }
            )

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)


# # class Result(Model):
# #     team_1_score
# #     team_2_score


# class Coefficient(Model):
#     """Coefficient."""

#     event = ForeignKey(
#         Event,
#         on_delete=CASCADE,
#         related_name='coefficients',
#         verbose_name='событие'
#     )
#     team = OneToOneField(
#         Team,
#         on_delete=PROTECT,
#         verbose_name='команда'
#     )

#     class Meta:
#         ordering = ('-id',)
#         verbose_name = 'коэффицент'
#         verbose_name_plural = 'коэффиценты'

#     def __str__(self) -> str:
#         return f'{self.event.id}'


# class Event(AbstractDateTime):
#     """Event."""

#     STATUS_PLANNED: str = 'planned'
#     STATUS_ONGOING: str = 'ongoing'
#     STATUS_FINISHED: str = 'finished'
#     EVENT_STATUSES: tuple[tuple[str, str], ...] = (
#         (STATUS_PLANNED, 'Запланировано'),
#         (STATUS_ONGOING, 'В процессе'),
#         (STATUS_FINISHED, 'Завершено')
#     )
#     status = CharField(
#         choices=EVENT_STATUSES,
#         default=STATUS_PLANNED,
#         max_length=10,
#         verbose_name='статус'
#     )
#     # result = OneToOneField(
#     #     Result,
#     #     on_delete=CASCADE,
#     #     null=True,
#     #     blank=True,
#     #     verbose_name='результат'
#     # )
#     teams = ManyToManyField(
#         Team,
#         related_name='events',
#         verbose_name='команда'
#     )

#     @property
#     def teams_titles(self) -> str:
#         return ' vs '.join(team.title for team in self.teams.all())

#     @property
#     def coefficents(self) -> dict[str, float]:
#         stronger_team: Team
#         weaker_team: Team
#         stronger_team, weaker_team = self.teams.annotate(
#             avg_power=Avg('players__power')
#         ).order_by('-avg_power')

#         default_coef: float = Decimal('1.1')
#         diff: float = stronger_team.power - weaker_team.power

#         return default_coef + diff
#         # return {
#         #     stronger_team.title: default_coef,
#         #     weaker_team.title: float(Decimal(str(default_coef + diff)))
#         # }

#     class Meta:
#         ordering = ('-dt_created',)
#         verbose_name = 'событие'
#         verbose_name_plural = 'события'

#     def __str__(self) -> str:
#         return f'{self.teams_titles} | {self.get_status_display()} | {self.coefficents}'
