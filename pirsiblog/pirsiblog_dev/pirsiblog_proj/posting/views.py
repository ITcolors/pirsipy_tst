#from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

from posting.models import Post


class Index(TemplateView):
    template_name = 'posting/index.html'
    # latest_posts = Post.objects.order_by('created')[:10]
    # posts_out = ', '.join([ps.title for ps in latest_posts])
    
    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.order_by('created')
    
        return context

class Details(TemplateView):
    # def get(self, request):
    #     return HttpResponse('Details of post with ID %s:' % id)
    pass

        