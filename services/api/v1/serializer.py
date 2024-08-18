from rest_framework import serializers
from services.models import Service ,Team , Category , Skill 
from ...models import Category , Option

class Serviceserializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField()
    name = serializers.SerializerMethodField(method_name='cat_name')
    created_at = serializers.SerializerMethodField(method_name='year')                                     
    category = serializers.SlugRelatedField(many=True, queryset=Category.objects.all(),slug_field ='title')
    generals = serializers.SlugRelatedField(many=True, queryset=Option.objects.all() , slug_field ='title')
    detail_link = serializers.SerializerMethodField(method_name='detail')

    class Meta:
        model = Service
        fields = ['name','content' , 'title' , 'description' , 'price' , 'category' , 'generals' ,'created_at' , 'detail_link']
        read_only_fields = ['name']
    def cat_name(self , instance):
        return str(instance.name).upper()
    
    def year(self , instance):
        return (str(instance.created_at).split('-'))[0]
    
    def detail(self , instance):
        request = self.context.get('request')
        return str(request.build_absolute_uri())+f'/{instance.pk}'
        
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['category'] = [cat.title for  cat in instance.category.all()]
    #     return rep
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')

        if kwargs.get('pk'):
            rep['category'] = [cat.title for  cat in instance.category.all()]

        else :
            rep.pop('category')

        return rep


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class skillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'
