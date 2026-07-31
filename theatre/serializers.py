from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from theatre.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username"]


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class PlaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres"]


class PlayListSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres"]


class TheatreHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time"]


class PerformanceListSerializer(serializers.ModelSerializer):
    play = PlayListSerializer()
    theatre_hall = TheatreHallSerializer()

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time"]


class ReservationSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ["id", "created_at"]


class TicketListSerializer(serializers.ModelSerializer):
    performance = PerformanceListSerializer()
    reservation = ReservationSimpleSerializer()

    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "performance", "reservation"]


class TicketCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ["row", "seat", "performance"]


class ReservationCreateSerializer(serializers.ModelSerializer):
    tickets = TicketCreateSerializer(many=True)

    class Meta:
        model = Reservation
        fields = ["tickets"]

    @transaction.atomic
    def create(self, validated_data):
        tickets_data = validated_data.pop("tickets")

        reservation = Reservation.objects.create(
            user=User.objects.first()
        )

        for ticket_data in tickets_data:
            Ticket.objects.create(
                reservation=reservation,
                **ticket_data
            )

        return reservation


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tickets = TicketCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user", "tickets"]
