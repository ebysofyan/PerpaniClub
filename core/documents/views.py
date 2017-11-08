from django.shortcuts import render, redirect
from utils.customview import (
    LoginRequiredGenericView,
    LoginRequiredListView,
    LoginRequiredDetailView,
    LoginRequiredUpdateView,
    LoginRequiredTemplateView,
    LoginRequiredCreateView
)
from django.http import HttpResponse
from .forms import ClubFilesForm
from core.orm.models import ClubFiles
from datetime import datetime
import mimetypes
import os


class DocumentsView(LoginRequiredGenericView):
    template_name = 'core/docs/docs.html'

    def get(self, request):
        data = {
            'menu': 'docs',
            'subtitle': 'Semua Berkas Klub'
        }
        return render(request, self.template_name, data)

    def post(self, request):
        form = ClubFilesForm(request.POST or None, request.FILES)
        if form.is_valid():
            club_file = ClubFiles()
            club_file.club = request.user.member.club
            club_file.file = form.cleaned_data['file']
            club_file.mimetype = mimetypes.guess_type(
                club_file.file.name)[0].split('/')[0]
            club_file.file_ext = mimetypes.guess_type(
                club_file.file.name)[0].split('/')[1]
            club_file.filename = club_file.file.name

            club_file.save()

            return HttpResponse('Success')
        return self.get(request)


class DocumentDelete(LoginRequiredGenericView):

    def get(self, request, pk):
        obj = ClubFiles.objects.get(pk=pk)
        if obj:
            img_url = os.path.join(os.getcwd(), obj.file.url[1:])
            obj.delete()
            if os.path.exists(img_url):
                os.remove(img_url)
                
            return redirect('/documents/')
