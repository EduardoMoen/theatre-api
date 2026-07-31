from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view
)

from rest_framework import viewsets

from theatre.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Reservation,
    Ticket,
)

from theatre.serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    ReservationCreateSerializer,
    PlayListSerializer,
    PerformanceListSerializer,
    TicketListSerializer,
)


@extend_schema_view(
    list=extend_schema(summary="List genres"),
    retrieve=extend_schema(summary="Retrieve a genre"),
    create=extend_schema(summary="Create a genre"),
    update=extend_schema(summary="Update a genre"),
    partial_update=extend_schema(summary="Partially update a genre"),
    destroy=extend_schema(summary="Delete a genre"),
)
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@extend_schema_view(
    list=extend_schema(summary="List actors"),
    retrieve=extend_schema(summary="Retrieve an actor"),
    create=extend_schema(summary="Create an actor"),
    update=extend_schema(summary="Update an actor"),
    partial_update=extend_schema(summary="Partially update an actor"),
    destroy=extend_schema(summary="Delete an actor"),
)
class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List plays",
        description="Returns all plays with genres and actors.",
        responses=PlayListSerializer(many=True),
    ),
    retrieve=extend_schema(
        summary="Retrieve a play",
        description="Returns detailed information about a play.",
        responses=PlayListSerializer,
    ),
    create=extend_schema(summary="Create a play"),
    update=extend_schema(summary="Update a play"),
    partial_update=extend_schema(summary="Partially update a play"),
    destroy=extend_schema(summary="Delete a play"),
)
class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PlayListSerializer

        return PlaySerializer


@extend_schema_view(
    list=extend_schema(summary="List theatre halls"),
    retrieve=extend_schema(summary="Retrieve a theatre hall"),
    create=extend_schema(summary="Create a theatre hall"),
    update=extend_schema(summary="Update a theatre hall"),
    partial_update=extend_schema(summary="Partially update a theatre hall"),
    destroy=extend_schema(summary="Delete a theatre hall"),
)
class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List performances",
        description="Returns performances with play and theatre hall details.",
        responses=PerformanceListSerializer(many=True),
    ),
    retrieve=extend_schema(
        summary="Retrieve a performance",
        responses=PerformanceListSerializer,
    ),
    create=extend_schema(summary="Create a performance"),
    update=extend_schema(summary="Update a performance"),
    partial_update=extend_schema(summary="Partially update a performance"),
    destroy=extend_schema(summary="Delete a performance"),
)
class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PerformanceListSerializer

        return PerformanceSerializer


@extend_schema_view(
    list=extend_schema(summary="List reservations"),
    retrieve=extend_schema(summary="Retrieve a reservation"),
    create=extend_schema(
        summary="Create a reservation",
        description=(
            "Creates a reservation for the authenticated user and all "
            "associated tickets in a single transaction."
        ),
        request=ReservationCreateSerializer,
        responses=ReservationSerializer,
    ),
    destroy=extend_schema(summary="Cancel a reservation"),
)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ReservationCreateSerializer

        return ReservationSerializer


@extend_schema_view(
    list=extend_schema(summary="List tickets"),
    retrieve=extend_schema(summary="Retrieve a ticket"),
)
class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
