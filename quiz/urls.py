from django.urls import path,include
from rest_framework import routers
from quiz.views import AnswerViewSet, CategoryView,HomeView, LogView, QuestionViewSet, QuizSubmit, QuizViewSet, Registration_view,SelectedCategoryView, StartQuiz
router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),
    path('r/', include(router.urls)),
    path('', HomeView,name='home'),
    path('categories/',CategoryView,name='categories'),
    path('categories/<slug:slug>',SelectedCategoryView,name='category'),
    path('startquiz/<int:id>',StartQuiz,name='startquiz'),
    path('quiz-submit/',QuizSubmit,name='submit'),
    path('log/',LogView,name='log'),
    path('register/', Registration_view.as_view(),name='register'),

]