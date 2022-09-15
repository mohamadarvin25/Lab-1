from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html",context)

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Mohamad Arvin Fadriansyah'
}
def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), content_type="application/json")

data = BarangWishlist.objects.filter(pk=1)

def show_json_by_id(request,id):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
