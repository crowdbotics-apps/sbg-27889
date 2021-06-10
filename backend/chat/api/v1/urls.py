from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ForwardedMessageViewSet,
    MessageViewSet,
    MessageActionViewSet,
    ThreadViewSet,
    ThreadActionViewSet,
    ThreadMemberViewSet,
)

router = DefaultRouter()
router.register("thread", ThreadViewSet)
router.register("message", MessageViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("threadaction", ThreadActionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
