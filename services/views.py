from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect
from .models import SpecialService, Team, Skill , Category , Option , Service , Comment
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import ListView , DetailView

class ServiceView(ListView):
    template_name = 'services/services.html'
    context_object_name = 'services'
    paginate_by =  2
    def get_queryset(self):
        if self.kwargs.get('category'):
            all_service = Service.objects.filter(category__title=self.kwargs.get('category'))

        if self.kwargs.get('search'):
            all_service = Service.objects.filter(content__contains=self.kwargs.get('search'))

        if self.kwargs.get('price'):
            all_service = Service.objects.filter(price__lte=self.kwargs.get('price'))
        else:
            all_service = Service.objects.filter(status = True)

        return all_service

# def services(request, **kwargs):
#     if kwargs.get('category'):
#         all_service = Service.objects.filter(category__title=kwargs.get('category'))

#     elif request.GET.get('search') is not None:
#         all_service = Service.objects.filter(content__contains=request.GET.get('search'))

#     elif kwargs.get('price'):
#         all_service = Service.objects.filter(price__lte=kwargs.get('price'))

#     else:    
#         all_service = Service.objects.filter(status=True)


#     all_services = Paginator(all_service,2)

#     try:
#         page_number = request.GET.get('page')
#         all_services = all_services.get_page(page_number)

#     except PageNotAnInteger:
#         all_services = all_services.get_page(1)

#     except EmptyPage:
#         all_services = all_services.get_page(1)
    

#     context = {            
#             "services" : all_services,
#             "special_services": SpecialService.objects.filter(status=True), 
#         }
#     return render(request, 'services/services.html' , context = context)

class Service_detail_view(DetailView):
    model = Service
    template_name = 'services/service-details.html'
    context_object_name = 'service_detail'

    def get(self, request, *args , **kwargs):
        service = self.model.objects.get(pk=kwargs.get('pk'))
        service.counted_view += 1
        service.save()
    # def get_context_data(self,**kwargs):







# def services_detail(request ,id):

#     try:
#         service = get_object_or_404(Service ,  id=id)
#         comment = Comment.objects.filter(product_name=service.name , status=True)
#         service.counted_view += 1
#         service.save()

#         context = {
#         'service_detail': service,
#         'comment' : comment

#         }
#         return render(request, 'services/service-details.html' , context=context)

#     except: 
#         return render(request, 'services/404.html' )


def qoute(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'your comment was delivered succssesfully and will be publish asap!')
                return redirect(request.path_info)
            else:
                messages.add_message(request,messages.ERROR,'your input data may be incorrect')
                return redirect(request.path_info)
        else:
            return redirect('accounts:login')
    else:
        return render(request, 'services/get-a-quote.html')
    
def edit_comment(request , id):
    comment = get_object_or_404(Comment , id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status = False
            obj.save()
            return redirect('services:services')
        else:
            messages.add_message(request,messages.ERROR , 'not save comment')
            return redirect(request.path_info)

    else:
        form = CommentForm(instance=comment)
        context = {
            'form': form,
        }
        return render(request, 'services/edit-comment.html' , context=context)


    
