from django.shortcuts import render, get_object_or_404, redirect
from .models import Etudiant
from .forms import EtudiantForm

def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {'etudiants': etudiants})

def ajouter_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm()
    return render(request, 'etudiants/formulaire.html', {'form': form, 'title': 'Ajouter étudiant'})


def modifier_etudiant(request, cne):
    etudiant = get_object_or_404(Etudiant, cne=cne)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')
    else:
        form = EtudiantForm(instance=etudiant)
    return render(request, 'etudiants/formulaire.html', {'form': form, 'title': 'Modifier étudiant'})


def supprimer_etudiant(request, cne):
    etudiant = get_object_or_404(Etudiant, cne=cne)
    if request.method == "POST":
        etudiant.delete()
        return redirect('liste_etudiants')
    return render(request, 'etudiants/supprimer.html', {'etudiant': etudiant})
