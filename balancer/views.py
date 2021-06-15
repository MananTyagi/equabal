from django.shortcuts import render
from balancer.models import reactions
# Create your views here.

def test(request):
    allreactionscontent=reactions.objects.all()
    print(allreactionscontent)
    context={'allreact':allreactionscontent}
    for item in context['allreact']:
        print(item.reactant1)
    return render(request, 'test.html',context)
