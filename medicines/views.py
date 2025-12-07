from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, MedicineForm
from .models import Medicine
from django.contrib import messages
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome!!")
            return redirect('medicines:dashboard')
    else: 
        form=SignUpForm()
    return render(request, 'medicines/signup.html', {'form': form})

@login_required
def dashboard(request):
    medicines=Medicine.objects.filter(owner=request.user)
    return render(request, 'medicines/dashboard.html', {'medicines': medicines})

@login_required
def medicine_create(request):
    if request.method=='POST':
        form=MedicineForm(request.POST)
        if form.is_valid():
            med=form.save(commit=False)
            med.owner=request.user
            med.save()
            messages.success(request, "Medicine Added!!")
            return redirect('medicines:dashboard')
    else:
        form= MedicineForm()
    return render(request, 'medicines/medicine_form.html', {'form': form, 'title': 'Add Medicine'})

@login_required
def medicine_update(request, pk):
    med=get_object_or_404(Medicine, pk=pk, owner=request.user)
    if request.method=='POST':
        form=MedicineForm(request.POST, instance=med)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine updated!!")
            return redirect('medicines:dashboard')
    else: 
        form=MedicineForm(instance=med)
    return render(request, 'medicines/medicine_form.html', {'form': form, 'title': 'Edit Medicine'})

@login_required
def medicine_delete(request, pk):
    med=get_object_or_404(Medicine, pk=pk, owner=request.user)
    if(request.method)=='POST':
        med.delete()
        messages.success(request, "Medicine Deleted!!")
        return redirect('medicines:dashboard')
    return render(request, 'medicines/confirm_delete.html', {'medicine': med})
