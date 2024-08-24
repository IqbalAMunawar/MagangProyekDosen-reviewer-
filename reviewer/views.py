from django.http import HttpResponse
from django.template import loader

def reviewer(request):
    #(ambil data image dari folder static )
    #(panggil layanan annotasi)
    #(simpan image dan hasil annotasi sebagi konteks)
    #(kirim konteks ke annotations.html)
    template = loader.get_template('index.html')
    return HttpResponse(template.render())