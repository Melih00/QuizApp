from rest_framework import serializers
from .models import Answer, Questions, Quiz
from django.contrib.auth.models import User
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question','text','is_right']
    def create(self, validated_data):
        answer = Answer.objects.create(**validated_data)
        answer.save()
        return answer
        
class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Questions
        fields = ['question','quiz','difficulty','answers']
class QuizSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=False,read_only=True)
    questions = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Quiz
        fields = '__all__'
    def create(self, validated_data):
        owner = self.context['request'].user.id
        validated_data['user_id'] = owner
        quiz = Quiz.objects.create(**validated_data)
        quiz.save()
        return quiz
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']