from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.messages import constants


def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if email == "":
            messages.add_message(request, constants.ERROR, 'Email inválido!')
        else:        
            try:
                data = {
                    'name': name, 
                    'email': email, 
                    'subject': subject, 
                    'message': message
                }
                message = '''
        Nova mensagem: 

        {}
                
        From: EMAIL_REMETENTE
                '''.format(data['message'], data['email'])
                send_mail(data['subject'], message, 'EMAIL_REMETENTE', recipient_list=[email])
                
                messages.add_message(request, constants.SUCCESS, 'Email enviado com sucesso!')        
                
            except:
                messages.add_message(request, constants.ERROR, 'Email inválido!')        
            
    return render(request, 'contactform/index.html', {})
