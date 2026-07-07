from django.contrib import admin

from cinema.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    list_filter = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_filter = ["title"]
    search_fields = ["title"]


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ["name", "rows", "seats_in_row", "capacity"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ["play", "theatre_hall", "show_time"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["row", "seat", "reservation", "performance"]
