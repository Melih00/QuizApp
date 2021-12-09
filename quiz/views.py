from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from accounts.serializers import UserSerializer
from quiz.models import Answer, Categories, Questions, Quiz
from quiz.serializers import AnswerSerializer, QuestionSerializer, QuizSerializer, RegistrationSerializer
from django.contrib.auth import logout,login
from django.contrib.auth.hashers import make_password
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

def HomeView(req):
    is_login = req.user.is_authenticated
    print(is_login)
    return render(req,'home.html',{'user':req.user})
    
def CategoryView(req):
    user = req.user
    slug = Categories.objects.all()
    return render(req,'categories.html',{'user':user,'slug':slug})
def SelectedCategoryView(req,slug):
    user = req.user
    slug = Quiz.objects.filter(category=list(Categories.objects.filter(link=str(slug)))[0].id)
    owners = {}
    for i in slug:
        if i.user_id:
            owners[f'{i.user_id}'] = User.objects.filter(id=i.user_id)
    return render(req,'category_quizzes.html',{'user':user,'slug':list(slug),'owners':owners})

def StartQuiz(req,id):
    quiz = Quiz.objects.filter(id=id)[0]
    questions = Questions.objects.filter(quiz=quiz.id)
    book = {}
    for i in questions:
        answer = Answer.objects.filter(question = i.id)
        book[f'{i}'] = answer
    return render(req,'startquiz.html',{'quiz':quiz,'book':book,'user':req.user})
    
def QuizSubmit(req):
    if req.method == 'POST':
        trues = 0
        falses = 0
        query = {}
        for i in req.POST:
            if i != 'csrfmiddlewaretoken':
                if (req.POST[i])[0:4] == 'True':
                    trues += 1
                else:
                    falses += 1
                    query[str((req.POST[i])[5::])]=i
        return render(req,'result.html',{'trues':trues,'falses':falses,'query':query,'user':req.user})
    return render(req,'home.html',{'user':req.user})

def LogView(req):
    if req.user.is_authenticated:
        print(req.user)
        logout(req)
        return render(req,'home.html',{'user':req.user,})
    else:
        return redirect('/login')
class Registration_view(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'
    def get(self, request):
        return Response({'serializer':'merhaba', })
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            serializer.validated_data['password'] = make_password(password)
            user = serializer.save()
            logout(request)
            login(request,user)
            
        return redirect('home')