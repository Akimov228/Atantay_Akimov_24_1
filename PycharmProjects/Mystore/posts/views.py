from django.shortcuts import HttpResponse
import datetime




def main(reguest):
    if reguest.method == 'GET':
        return HttpResponse('Hello! Its my project')


def show_date(reguest):
    global current_date
    current_date = datetime.date.today()
    if reguest.method == 'GET':
        return HttpResponse(f'{current_date}')

def say_bye(reguest):
    if reguest.method == 'GET':
        return HttpResponse('Goodbye user!')
