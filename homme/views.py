from django.shortcuts import render,redirect
from .models import Header,Skill,Setting,Review,Team,Work,Partner,Service,Price,Subscribe,Message,CounterUp
from django.core.mail import send_mail, BadHeaderError
from .forms import SubscribeForm,ContactForm
# Create your views here.
def homme(request):
    typeworks=[]
    for item in Work.objects.all():
        if item.type not in typeworks:
            typeworks.append(item.type)
    return render(request, 'index.html',{
        "header":Header.objects.all(),
        "skills":Skill.objects.all(),
        "settings":Setting.objects.first(),
        "services":Service.objects.all(),
        "reviews":Review.objects.all(),
        "recentreviws":Review.objects.all()[:2],
        "team":Team.objects.all(),
        "works":Work.objects.all(),
        "typeworks":typeworks,
        "partners":Partner.objects.all(),
        "counterup":CounterUp.objects.all(),
        "subscribe":SubscribeForm()
    })
def subscribe(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscribeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newsub=Subscribe(email=form.cleaned_data['email'])
            newsub.save()
    return redirect(homme)

def about(request):
    return render(request, 'about.html',{
        "settings":Setting.objects.first(),
        "skills":Skill.objects.all(),
        "team":Team.objects.all(),
        "recentreviws":Review.objects.all()[:2],
        "subscribe":SubscribeForm()
     })
def services(request):
    return render(request, 'services.html',{
        "services":Service.objects.all(),
        "recentreviws":Review.objects.all()[:2],
        "subscribe":SubscribeForm()
     })
def works(request):
    return render(request, 'works.html',{
        "works":Work.objects.all(),
        "recentreviws":Review.objects.all()[:2],
        "subscribe":SubscribeForm()
     })
def prices(request,service):
    prices=Price.objects.filter(service=service).all()
    return render(request, 'prices.html',{
        "prices":prices,
        "recentreviws":Review.objects.all()[:2],
        "subscribe":SubscribeForm()
     })
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject=""
            subject = "Website Inquiry" 
            body ={
			'name': form.cleaned_data['name'], 
			'email': form.cleaned_data['email'], 
			'subject': form.cleaned_data['subject'], 
			'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, None, ['bzquatre@gmail.com']) 
                newmessage=Message(name=form.cleaned_data['name'],
                                    email=form.cleaned_data['email'],
                                    subject=form.cleaned_data['subject'],
                                    message=form.cleaned_data['message'])
                newmessage.save()
                newsub=Subscribe(email=form.cleaned_data['email'])
                newsub.save()
            except BadHeaderError:
                pass
            return redirect (homme)
    return render(request, 'contact.html',{
            "settings":Setting.objects.first(),
            "recentreviws":Review.objects.all()[:2],
            "subscribe":SubscribeForm(),
            "contact":ContactForm(),
     })