from django.shortcuts import render
from django.http import JsonResponse

from datetime import datetime
import random
import os

def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = {
        'servername': 'lab server',
        'random': random.randint(0, 256),
        'datetime': datetime.now().isoformat(),
        'url': request.build_absolute_uri(),

        'server_iinfo': {
            'system': os.name,
            'srv_pid': os.getpid(),
            'user': os.getlogin(),
        },

        'client_info': {
            'user agent': request.META['HTTP_USER_AGENT'],
            'remote addr': request.META['REMOTE_ADDR'],
            'remote host': request.META['REMOTE_HOST'],
        }
    }


    return JsonResponse(response)
