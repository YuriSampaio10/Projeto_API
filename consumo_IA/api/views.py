from django.shortcuts import render
import openai
from django.http import HttpResponse

# Create your views here.

def ia(request):
    if request.method == "GET":
        return render(request, 'ia.html')
    elif request.method == "POST":
        question = request.POST.get('question')

        # client = openai.OpenAI(api_key='##############')
        result = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': "Você é um assistente pessoal, tire todas as duvidas."},
                {'role': 'user', 'content': question}
            ]
        )
        result HttpResponse(result)