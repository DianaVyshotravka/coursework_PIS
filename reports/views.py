from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Report
from .forms import NewReport

@login_required
def new(request):
    if request.method == 'POST':
        form = NewReport(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.created_by = request.user
            report.save()

            return redirect('/reports')
    else:
        form = NewReport

    return render(request, 'new.html', {
        'form': form,
        'title': 'New report',
    })


def index(request):
    items = Report.objects.filter().order_by('-created_at')
    return render(request, 'reports.html', {
        'items': items,
    })