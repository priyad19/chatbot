from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def home(request):
    return render(request, 'core/base.html')

def get_bot_response(request):
    user_text = request.GET.get('msg')
    bot_response = str(chatbot.get_response(user_text))
    return JsonResponse({'response': bot_response})

class ChatBotView(APIView):
    def post(self, request, format=None):
        user_input = request.data['message']
        response = chatbot.get_response(user_input)
        data = {'message': str(response)}
        return JsonResponse({'status': 201, 'success': True, 'data': data,"message": "Success"})