from django.shortcuts import render
from django.views.generic.base import View
from baseportal.forms import LandForm

from web3 import Web3, HTTPProvider
from Project.settings import trufSettings
from web3.contract import ConciseContract


web3 = Web3(HTTPProvider(trufSettings["server"]))

Bhoomi=web3.eth.contract(abi=trufSettings["abi"], address=trufSettings["address"])


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, "baseportal/homepage.html")

class LandRecordView(View):
    def get(self, request):
        context={
            "form":LandForm()
        }
        return render(request, "baseportal/landrecord.html", context)
    def post(self, request):
        form=LandForm(request.POST)
        context={
            "form":form,
        }
        if form.is_valid():
            landno=int(form.cleaned_data["land_number"])
            partinfo=form.cleaned_data["gram_panchayat"].id
            print("landno",landno,"partinfo",partinfo)
            lotno=int("{:05d}{:05d}".format(partinfo, landno))
            print("checking",lotno)
            name, aadhar, pan=Bhoomi.call().getOwner(lotno)
            context["result"]={
                "lotno":lotno,
                "name":name,
                "aadhar":aadhar,
                "pan":pan
            }
            
        return render(request, "baseportal/landrecord.html", context)
    
        
