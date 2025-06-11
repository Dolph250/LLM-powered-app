from django.shortcuts import render, redirect
from django.http import JsonResponse
from openai import OpenAI
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest


def chatbot(request):
    #members = Member.objects.all()
    return render(request, 'chatbot.html')

client = OpenAI(api_key="MyKey")
@csrf_exempt
def ask_openai(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            answer = response.choices[0].message.content
            return JsonResponse({"response": answer})
        except Exception as e:
            return JsonResponse({"response": f"Error: {str(e)}"})



def index(request):
    #members = Member.objects.all()
    return render(request, 'chatbot.html')

def logout_view(request):
    #request.session.flush()
    email = request.session.get("email", "adoizere@gmail.com")
    name = request.session.get("name", "Dolph")
    return render(request, 'panel.html', {"email": email, "name": name})

def users(request):
    #members = Member.objects.all()
    return render(request, 'users.html')


def login(request):
    #members = Member.objects.all()
    email = request.session.get("email", "adoizere@gmail.com")
    name = request.session.get("name", "Dolph")
    return render(request, 'panel.html', {"email": email, "name": name})