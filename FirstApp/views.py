# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Pri
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
@login_required(login_url="FirstApp:login")
def index(request):
    all_records = Pri.objects.all()
    #for record in all_records:
    #    url = '/FirstApp/' + str(record.id) + '/'
    #    html += '<a href="' + url + '">' + record.Pcol1 + '</a><br>'
    context = {'all_records': all_records}
    return render(request, 'FirstApp/index.html' ,context)
    #return HttpResponse(html)


@login_required(login_url='FirstApp:login')
def details(request, rid):
    return HttpResponse("<h3><i>Record number "+str(rid)+"</i></h3>")


class PriCreate(CreateView):
    model = Pri
    fields = ['Pcol1','Pcol2', 'Pcol3']

    @method_decorator(login_required(login_url='FirstApp:login'))
    def dispatch(self, *args, **kwargs):
            return super(PriCreate, self).dispatch(*args, **kwargs)



class NewUser(View):
    form_class = NewUserForm
    template_name = 'FirstApp/newlogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user =  authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('FirstApp:index')

        return render(request, self.template_name, {'form':form})
