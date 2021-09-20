from rest_framework import serializers
from itertools import chain
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework import serializers, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from constructor import models
from drf_multiple_model.views import FlatMultipleModelAPIView
from django.http import JsonResponse
import json
from django.http import HttpResponse


class SpecializationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = ['id', 'name']


class CourseNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name']


class DisciplineNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Discipline
        fields = ['id', 'name']


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 25


class TextSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=500)


# class CourseSuggestion(APIView):
#     """
#     List all matches ,with in course, discipline,specialization. models
#     """
#
#     def get(self, request, format=None):
#         qs = models.Course.objects.all()
#         query_dict = {}
#         if request.GET.get('name'):
#             query_dict['name__contains'] = request.GET.get('name').strip()
#         qs = qs.filter(**query_dict).order_by('name')
#         serializer = CourseSuggestionSerializer(qs, many=True)
#         return Response(serializer.data)

def specialization_filter(queryset, request, *args, **kwargs):
    params = request.query_params['search']
    return queryset.filter(name__istartswith=params).order_by('name').distinct('name')


class TextAPIView(APIView):

    def get(self, request):
        qs = []
        if request.GET.get('search'):
            name = request.GET.get('search').strip()
            sp = models.Specialization.objects.filter(name__contains=name)
            ds = models.Discipline.objects.filter(name__contains=name)
            results = chain(sp, ds)
            qs = sorted(results, key=lambda instance: instance.pk, reverse=True)
        serializer = TextSerializer(qs, many=True)
        return Response(serializer.data)


# class SpecializationDisciplineSuggestionView(FlatMultipleModelAPIView):
#     search_fields = ['name']
#     filter_backends = (filters.SearchFilter,)
#     pagination_class = LimitPagination
#     querylist = [
#
#         {'queryset': models.Discipline.objects.all(),
#          'serializer_class': DisciplineNameSerializer},
#         {'queryset': models.Specialization.objects.all(),
#          'serializer_class': SpecializationNameSerializer},
#     ]

# class SpecializationDisciplineSuggestionView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         from django.db.models import Q, ExpressionWrapper, BooleanField
#         search_query = request.GET.get('search', '').strip()
#         if not search_query:
#             raise CustomApiException("Please provide atleast one character to search Institute by name",
#                                      status.HTTP_400_BAD_REQUEST)
#         query = models.Specialization.objects.filter(name__istartswith=search_query)[1:15]
#         results = []
#         for obj in query:
#             results.append({'id': obj.id, 'name': obj.name, 'type': 'Specialization'})
#
#         dump = json.dumps(results)
#         return HttpResponse(dump, content_type='application/json')


class SpecializationDisciplineSuggestionView(FlatMultipleModelAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitPagination
    querylist = [
        {'queryset': models.Specialization.objects.all(),
         'serializer_class': SpecializationNameSerializer,
         'filter_fn': specialization_filter},
    ]


# def get(self, request, *args, **kwargs):
#     querylist = []
#     if request.GET.get('name'):
#
#         name = request.GET.get('name').strip()
#
#         querylist = [
#             {'queryset': models.Course.objects.filter(name__contains=name),
#              'serializer_class': CourseNameSerializer},
#             # {'queryset': models.Discipline.objects.filter(name__contains=name), 'serializer_class': CourseNameSerializer},
#         ]
#         print(querylist)
#     return Response({'results': json.dumps(querylist)})

class RegionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['id', 'name']


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ['id', 'name']


class StateNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.State
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.name + ' (' + obj.country.name + ')'


class CityNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.City
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.name + ' (' + obj.state.country.name + ')'


# def country_filter(queryset, request, *args, **kwargs):
#     params = request.query_params['name']
#     return queryset.filter(name__startswith=params)

def country_filter(queryset, request, *args, **kwargs):
    params = request.query_params['search'].strip()
    if params:
        params = params.strip()
    return queryset.filter(name__istartswith=params)


def state_filter(queryset, request, *args, **kwargs):
    params = request.query_params['search'].strip()
    if params:
        params = params.strip()
    return queryset.filter(name__istartswith=params).order_by('name')


def city_filter(queryset, request, *args, **kwargs):
    params = request.query_params['search'].strip()
    if params:
        params = params.strip()
    return queryset.filter(name__istartswith=params).order_by('name')


class LocationAPIView(FlatMultipleModelAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitPagination
    querylist = [
        # {'queryset': models.Region.objects.all(),
        #  'serializer_class': RegionNameSerializer},
        {'queryset': models.Country.objects.all(),
         'serializer_class': CountryNameSerializer,
         'filter_fn': country_filter},
        {'queryset': models.State.objects.all(),
         'serializer_class': StateNameSerializer,
         'filter_fn': state_filter,
         },
        {'queryset': models.City.objects.all(),
         'serializer_class': CityNameSerializer,
         'filter_fn': city_filter,
         },

    ]


class InstituteNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.Institute
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.institute_name


class CourseTitleNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseTitle
        fields = ['id', 'name']

    def get_name(self, obj):
        return obj.display_name


def institute_filter(queryset, request, *args, **kwargs):
    params = request.query_params['name']
    return queryset.filter(institute_name__istartswith=params)


def title_filter(queryset, request, *args, **kwargs):
    params = request.query_params['name']
    return queryset.filter(display_name__istartswith=params)


def course_filter(queryset, request, *args, **kwargs):
    params = request.query_params['name']
    return queryset.filter(name__istartswith=params)


def discipline_filter(queryset, request, *args, **kwargs):
    params = request.query_params['name']
    return queryset.filter(name__istartswith=params)


def specialization_site_filter(queryset, request, *args, **kwargs):
    params = request.query_params['name']
    return queryset.filter(name__istartswith=params)


class GenaricSuggestionAPIView(FlatMultipleModelAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    pagination_class = LimitPagination
    querylist = [
        {'queryset': models.Institute.objects.all(),
         'serializer_class': InstituteNameSerializer,
         'filter_fn': institute_filter},
        {'queryset': models.Course.objects.all(),
         'serializer_class': CourseNameSerializer,
         'filter_fn': course_filter},
        {'queryset': models.Discipline.objects.all(),
         'serializer_class': DisciplineNameSerializer,
         'filter_fn': discipline_filter},
        {'queryset': models.Specialization.objects.all(),
         'serializer_class': SpecializationNameSerializer,
         'filter_fn': specialization_site_filter},
        {'queryset': models.CourseTitle.objects.all(),
         'serializer_class': CourseTitleNameSerializer,
         'filter_fn': title_filter},

    ]


class AllSearchSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

    def get_name(self, obj):
        if str(obj._meta.model.__name__) == "CourseTitle":
            return obj.display_name
        else:
            return obj.name

    def get_type(self, obj):
        return obj._meta.model.__name__


class AllSearch(APIView):

    def get(self, request, *args, **kwargs):
        from django.db.models import Q, ExpressionWrapper, BooleanField
        search_query = request.GET.get('q', '').strip()
        if not search_query:
            raise CustomApiException("Please provide atleast one character to search Institute by name",
                                     status.HTTP_400_BAD_REQUEST)

        course_title_results = models.CourseTitle.objects.filter(
            Q(display_name__istartswith=search_query) | Q(display_name__icontains=search_query)
        ).annotate(
            is_start=ExpressionWrapper(
                Q(display_name__istartswith=search_query),
                output_field=BooleanField()
            )
        ).order_by('-is_start')
        course_results = models.Course.objects.filter(
            Q(name__istartswith=search_query) | Q(name__icontains=search_query)
        ).annotate(
            is_start=ExpressionWrapper(
                Q(name__istartswith=search_query),
                output_field=BooleanField()
            )
        ).order_by('-is_start')
        discipline_results = models.Discipline.objects.filter(
            Q(name__istartswith=search_query) | Q(name__icontains=search_query)
        ).annotate(
            is_start=ExpressionWrapper(
                Q(name__istartswith=search_query),
                output_field=BooleanField()
            )
        ).order_by('-is_start')
        specialization_results = models.Specialization.objects.filter(
            Q(name__istartswith=search_query) | Q(name__icontains=search_query)
        ).annotate(
            is_start=ExpressionWrapper(
                Q(name__istartswith=search_query),
                output_field=BooleanField()
            )
        ).order_by('-is_start')

        # combine querysets
        queryset_chain = chain(
            course_title_results,
            course_results,
            discipline_results,
            specialization_results,

        )
        qs = sorted(queryset_chain,
                    key=lambda
                        instance: instance.display_name if str(
                        instance._meta.model.__name__) == "CourseTitle" else instance.name,
                    reverse=True)
        relevant = []
        irr_relevant = []

        for idx in qs:
            if str(idx._meta.model.__name__) == "CourseTitle":
                if idx.display_name.lower().startswith(search_query):
                    relevant.append(idx)
                else:
                    irr_relevant.append(idx)
            else:
                if idx.name.lower().startswith(search_query):
                    relevant.append(idx)
                else:
                    irr_relevant.append(idx)

        results = relevant + irr_relevant

        # res = [idx for idx in qs if idx.name.lower().startswith(search_query)]
        # print(res)

        serializer = AllSearchSerializer(results, many=True)
        return Response(serializer.data)


class InstitutesSearch(APIView):

    def get(self, request, *args, **kwargs):
        from django.db.models import Q, ExpressionWrapper, BooleanField
        search_query = request.GET.get('q', '').strip()
        if not search_query:
            raise CustomApiException("Please provide atleast one character to search Institute by name",
                                     status.HTTP_400_BAD_REQUEST)
        qs = models.Institute.objects.filter(
            Q(institute_name__istartswith=search_query) | Q(institute_name__icontains=search_query)
        ).annotate(
            is_start=ExpressionWrapper(
                Q(institute_name__istartswith=search_query),
                output_field=BooleanField()
            )
        ).order_by('-is_start')

        serializer = InstituteNameSerializer(qs, many=True)
        return Response(serializer.data)
