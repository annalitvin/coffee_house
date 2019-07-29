from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from django.core.paginator import Paginator

from core import models
# Create your views here.

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        m = models.Hall.objects.all()

        return render(request, self.template_name)
def Tables(request):
    all_tables = Table.objects.all()
    current_page = Paginator
    return render_to_response('index.html', {'tables': Table.objects.all()})

    # def post(self, request):
    #     form = AnalysesAction(request.POST)
    #
    #     text = ''
    #     languages = ''
    #     sentences = ''
    #     result = ''
    #
    #     if form.is_valid():
    #         actions = form.cleaned_data.get('actions')
    #         languages = form.cleaned_data.get('languages')
    #         format = form.cleaned_data.get('format')
    #         text = form.cleaned_data.get('text')
    #
    #
    #         if languages.lower() == 'uk' or languages.lower() == 'ru':
    #             languages = form.cleaned_data.get('languages')
    #
    #         if format.lower() == 'json' or format.lower() == 'xml':
    #             format = form.cleaned_data.get('format')
    #
    #
    #         if actions == 'relation_parse':
    #
    #
    #         return HttpResponse(result, content_type='text/plain')

        #return render(request, self.template_name)
