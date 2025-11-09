from django.shortcuts import render, redirect #render= renderiza as paginas html; redirect= redireciona
from django.http import HttpResponse, StreamingHttpResponse #função para retornar uma resposta http pro usuario
from django.contrib.auth.models import User #tabela do banco de dados 
from django.contrib.messages import constants #tipo de erro
from django.contrib import messages #função que cria a msg
from openai import OpenAI
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from django.conf import settings



# Create your views here.
@csrf_exempt
def ia(request):
    if request.method == "GET":
        return render(request, 'ia.html')
    elif request.method == "POST":
        question = request.POST.get('question')

        # OPENAI_API_KEY = config("API_KEY")


        client = OpenAI(api_key="REMOVIDOproj-6gy_Cv8BXsrL7hzA2I-EGuuEQLFHizq5Ns-HB-PQU1HQd4PaRwjHXMk1bG3XBDH5d3B0TWb11IT3BlbkFJP4f5MTIMoub50lYBVEZBxLTPByk-R1TBoZFdpGUlkvT4skDSLQ_siIvTV7TBZRKsysxfc0bFoA")
      
        def stream_gpt():
            result = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': f"Você é um assistente pessoal, tire todas as duvidas."},
                {'role': 'user', 'content': question}
                ],
                stream=True
            )

            for chunk in result: 
                yield chunk.choices[0].delta.content

        response_server = StreamingHttpResponse(stream_gpt())
        response_server['Cache-Control'] = 'no-cache'
        response_server['X-acceel-Buffering'] = 'no'

        return response_server