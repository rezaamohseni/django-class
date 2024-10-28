from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from services.models import Service, Team, Comment
from .serializer import Serviceserializer, TeamSerializer, CommentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)
from rest_framework import viewsets
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import MethodNotAllowed
# from .pagination import Custompagination


class ServiceApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Serviceserializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category", "name"]
    search_fields = ["price"]
    ordering_fields = ["created_at"]
    # pagination_class = Custompagination

    def get_queryset(self):
        return Service.objects.all()


class TeamApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TeamSerializer

    def get_queryset(self):
        return Team.objects.all()


class CommentApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def destroy(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs.get("pk"))
        if comment.user == request.user:
            comment.delete()
            return Response(
                "service deleted successfully", status=status.HTTP_204_NO_CONTENT
            )
        else:
            raise MethodNotAllowed("DELETE")

    def patch(self, instance, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=kwargs.get("pk"))
        user = request.user
        if comment.user == request.user:
            comment.update(instance)
            return Response(
                "service update successfully", status=status.HTTP_204_NO_CONTENT
            )
        else:
            raise MethodNotAllowed("Update")


# ======================================================
# start level 5
# ======================================================
# class ServiceApiViewSet(viewsets.ViewSet):

#     serializer_class = Serviceserializer

#     def get_queryset(self):
#         return Service.objects.all()

#     def list(self , request, *args, **kwargs):
#         serializer = self.serializer_class(self.get_queryset(), many=True)
#         return Response(serializer.data)

#     def create(self , request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error)


#     def update(self , request, *args, **kwargs):
#         services = get_object_or_404(Service , id=kwargs.get('pk'))
#         serializer = self.serializer_class(services, data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data ,status=status.HTTP_200_OK)


#     def destroy(self , request, *args, **kwargs):
#         services = get_object_or_404(Service , id=kwargs.get('pk'))
#         services.delete()
#         return Response('service deleted', status=status.HTTP_204_NO_CONTENT)


#     def retrieve(self , request, *args, **kwargs):
#         services = get_object_or_404(Service , id=kwargs.get('pk'))
#         serializer = self.serializer_class(services)
#         return Response(serializer.data ,status=status.HTTP_200_OK)
# ======================================================
# end level 5
# ======================================================


# ======================================================
# start level 4
# ======================================================

# class ServiceApiView(GenericAPIView , RetrieveModelMixin , DestroyModelMixin , UpdateModelMixin):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class = Serviceserializer
#     lookupp_fiels = 'id'

#     def get(self , request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


#     def patch(self , request, *args, **kwargs):
#         return self.update(request , *args, **kwargs)


#     def delete(self , request, *args, **kwargs):
#         return self.destroy(request , *args, **kwargs)
# ======================================================
# end level 4
# ======================================================


# ======================================================
# start level 3
# ======================================================

# class ServiceApiView(GenericAPIView , ListModelMixin , CreateModelMixin):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class = Serviceserializer

#     def get_queryset(self):
#         return Service.objects.all()

#     def get(self , request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self , request, *args, **kwargs):
#         return self.create(request , *args, **kwargs)
# ======================================================
# end level 3
# ======================================================


# ===========================================
# start class base level  2
# ==========================================

# class ServiceApiView(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     def get(self , request, *args, **kwargs):
#         services = Service.objects.all()
#         serializer = Serviceserializer(services ,many = True)
#         return Response(serializer.data)


#     def post(self , request, *args , **kwargs):
#         if request.user.is_superuser:
#             serializer = Serviceserializer(data=request.data )
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status=status.HTTP_201_created)

#             else:
#                 return Response(serializer.error)
#         else:
#             return Response('permission denied' , status=status.HTTP_401_UNAUTHORIZED)


# class ServiceDetailApiview(APIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]

#     def get(self , request, *args, **kwargs):
#         id = kwargs.get('id')
#         services = get_object_or_404(Service , id=id)
#         serializer = Serviceserializer(services)
#         return Response(serializer.data)
#     def patch(self , request, *args, **kwargs):
#         services = get_object_or_404(Service , id=id)
#         serializer = Serviceserializer(services , data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data ,status=status.HTTP_200_OK)


#     def delete(self , request, *args, **kwargs):
#         services = get_object_or_404(Service , id=id)
#         services.delete()
#         return Response('service deleted', status=status.HTTP_204_NO_CONTENT)

# =====================================
# end class base level 2
# =====================================


# ==============================
# start level 1   functions base !!!!!
# ==============================
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def services(request):
#     if request.method == 'GET':
#         services = Service.objects.all()
#         serializer = Serviceserializer(services ,many = True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         if request.user.is_superuser:
#             serializer = Serviceserializer(data=request.data )
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status=status.HTTP_201_created)
#             else:
#                 return Response(serializer.error)
#         else:
#             return Response('permission denied' , status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['GET', 'PATCH','DELETE'])
# def services_detail(request , id):
#     service = get_object_or_404(Service,id=id)
#     if request.method == 'GET':
#         # try:
#         #     services = Service.objects.get(id=id)
#         #     serializer = Serviceserializer(services)
#         #     return Response(serializer.data)
#         # except:
#         #     return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = Serviceserializer(service)
#         return Response(serializer.data)
#     elif request.method == 'PATCH':
#         serializer = Serviceserializer(service , data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data ,status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         service.delete()
#         return Response('service deleted', status=status.HTTP_204_NO_CONTENT)

# ==================================
# end level 1
# =================================
