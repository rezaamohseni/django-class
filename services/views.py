from django.shortcuts import render , get_object_or_404
from .models import SpecialService, Team, Skill , Category , Option , Service
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger

def services(request, **kwargs):
    if kwargs.get('category'):
        all_service = Service.objects.filter(category__title=kwargs.get('category'))

    elif request.GET.get('search') is not None:
        all_service = Service.objects.filter(content__contains=request.GET.get('search'))

    elif kwargs.get('price'):
        all_service = Service.objects.filter(price__lte=kwargs.get('price'))

    else:    
        all_service = Service.objects.filter(status=True)


    all_services = Paginator(all_service,2)

    try:
        page_number = request.GET.get('page')
        all_services = all_services.get_page(page_number)

    except PageNotAnInteger:
        all_services = all_services.get_page(1)

    except EmptyPage:
        all_services = all_services.get_page(1)
    

    context = {            
            "services" : all_services,
            "special_services": SpecialService.objects.filter(status=True), 
        }
    return render(request, 'services/services.html' , context = context)


def services_detail(request ,id):

    try:
        service = get_object_or_404(Service ,  id=id)
        service.counted_view += 1
        service.save()

        context = {
        'service_detail': service
        }
        return render(request, 'services/service-details.html' , context=context)

    except: 
        return render(request, 'services/404.html' )


def qoute(request):
    return render(request, 'services/get-a-quote.html')