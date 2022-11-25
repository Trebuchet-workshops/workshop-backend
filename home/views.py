from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response

from home.models import Session, Coupon
from home.serializer import SessionSerializer, CouponSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Session.objects.all()
        return queryset


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        code_name = request.data['code']
        queryset = Coupon.objects.filter(code=code_name).first()
        if queryset and queryset.is_active:
            serializer = CouponSerializer(queryset, many=False)
            return Response(serializer.data)
        else:
            return Response({'error': 'invalid coupon code'}, status=400)


class HomeView(TemplateView):
    template_name = "login/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context
