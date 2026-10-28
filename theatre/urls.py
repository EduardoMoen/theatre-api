from rest_framework.routers import DefaultRouter

from theatre.views import (
    GenreViewSet,
    ActorViewSet, PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)

app_name = "theatre"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("theatre-halls", TheatreHallViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet, basename="reservation")
router.register("tickets", TicketViewSet, basename="ticket")

urlpatterns = router.urls
