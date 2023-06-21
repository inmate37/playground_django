# # Python
# from typing import Optional

# # Django
# from django.contrib import admin
# from django.core.handlers.wsgi import WSGIRequest

# # Local
# from .models import (
#     Event,
#     Player,
#     Team
# )


# class EventAdmin(admin.ModelAdmin):
#     model = Event

#     readonly_fields = (
#         'dt_created',
#         'dt_updated',
#         'dt_deleted'
#     )
#     list_display = (
#         'status',
#     )

#     def get_readonly_fields(
#         self,
#         request: WSGIRequest,
#         obj: Optional[Event] = None
#     ) -> tuple[str, ...]:
#         if obj:
#             return self.readonly_fields + ('teams',)
#         return self.readonly_fields


# class PlayerAdmin(admin.ModelAdmin):
#     model = Player

#     readonly_fields = (
#         'name',
#         'surname',
#     )
#     list_display = (
#         'name',
#         'surname',
#         'power',
#         'team'
#     )


# class PlayerInline(admin.StackedInline):
#     model = Player

#     readonly_fields = (
#         'name',
#         'surname',
#         'power'
#     )


# class TeamAdmin(admin.ModelAdmin):
#     model = Team

#     readonly_fields = (
#         'title',
#     )
#     list_display = (
#         'title',
#         'power'
#     )
#     ordering = (
#         'title',
#     )
#     inlines = [
#         PlayerInline,
#     ]


# admin.site.register(Event, EventAdmin)
# admin.site.register(Player, PlayerAdmin)
# admin.site.register(Team, TeamAdmin)
