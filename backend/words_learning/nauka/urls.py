from django.urls import path
from nauka.views import * #WordViewSet, LearningViewSet, UserViewSet, WordToLearnViewSet, RegistrationAPIView, LoginView, LogoutView, UserWordsViewSet, UserLearningViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('words', WordViewSet, basename='words')
router.register('userwords', UserWordsViewSet, basename='userwords')
router.register('wordstolearn', WordToLearnViewSet, basename='wordstolearn')
router.register('learnings', LearningViewSet, basename='learnings')
router.register('userlearnings', UserLearningViewSet, basename='userlearnings')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls

urlpatterns += [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    #path('check_login_status/', check_login_status, name='check_login_status'),
]