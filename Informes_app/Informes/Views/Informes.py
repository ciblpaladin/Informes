from django.views import View
from django.shortcuts import render


class Informes(View):

    def get(request):

        return render(request, "Informes/listado.html")

