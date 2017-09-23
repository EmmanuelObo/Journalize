from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import JournalForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Journal


class JournalList(ListView):
    model = Journal
    template_name = "subtemplate/journal_entries.html"

def all_entries(request):
    data = {"entries": request.user.entry_set.all()}
    return render(request, 'subtemplate/journal_entries.html', data)

@login_required
def create_entry(request):
    if request.method == "POST":
        form = JournalForm(request.POST)
        print(form)
        if form.is_valid():
            print("This is a valid form.")
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            Journal.objects.create(title=title,text=text,image=image,writer=request.user)
            return HttpResponseRedirect('/entry/')

    form = JournalForm()
    data = {'form':form}
    return render(request, 'subtemplate/new_journal_entry.html', data)

def edit_entry(request, id):
    data = {}
    return render(request, 'subtemplate/edit_journal_entry.html', data)