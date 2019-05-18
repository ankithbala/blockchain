from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from web3 import Web3, HTTPProvider
from ownermanagement.settings import trufSettings
from web3.contract import ConciseContract
from web3 import eth
from django.contrib.auth.mixins import LoginRequiredMixin
from ownerportal.forms import SetOwnerForm, SellLandForm
from baseportal.models import PublicKey
import rsa

web3 = Web3(HTTPProvider(trufSettings["server"]))

Bhoomi=web3.eth.contract(abi=trufSettings["abi"], address=trufSettings["address"])

message="hello"
msgord=list(map(ord,message))


class HomePageView(View):
    def get(self, request):
        return render(request, "ownerportal/homepage.html")

# Create your views here.
class SetOwnerView(LoginRequiredMixin, View):
    def get(self, request):
        context={
            "form":SetOwnerForm(),
        }
        return render(request, "ownerportal/setowner.html", context)
    
    def post(self, request):
        form=SetOwnerForm(request.POST)
        if form.is_valid():
            landno=int(form.cleaned_data["land_number"])
            owner=form.cleaned_data["owner_name"]
            aadhar=int(form.cleaned_data["aadhar_number"])
            panno=form.cleaned_data["land_number"]
            Bhoomi.transact({"from":web3.eth.coinbase}).setOwner(landno, owner, aadhar, panno)
            return render(request, "ownerportal/setown_succ.html")
        context={
            "form":form,
        }  
        return render(request, "ownerportal/setowner.html", context)

class SellLandView(LoginRequiredMixin, View):
    def get(self, request):
        context={
            "form":SellLandForm(),
        }
        return render(request, "ownerportal/setowner.html", context)
    
    def post(self, request):
        form=SellLandForm(request.POST)
        if form.is_valid():
            landno=int(form.cleaned_data["land_number"])
            fromaadahar=int(form.cleaned_data["from_aadhar"])
            owner=form.cleaned_data["owner_name"]
            aadhar=int(form.cleaned_data["aadhar_number"])
            panno=form.cleaned_data["land_number"]
            pubkeyobj=get_object_or_404(PublicKey, aadhar=1)
            pubkey,privatekey=rsa.generate_keypair(pubkeyobj.p_val, pubkeyobj.q_val)
            cipher=rsa.encrypt(privatekey, message)
            print("Params",landno, fromaadahar, aadhar, owner, panno,43, msgord, cipher, pubkeyobj.n_val(), len(message))
            Bhoomi.transact({"from":web3.eth.coinbase}).sellLand(landno, fromaadahar, aadhar, owner, panno, pubkey[0], msgord, cipher, pubkeyobj.n_val(), len(message))
            return render(request, "ownerportal/setown_succ.html")
        context={
            "form":form,
        }  
        return render(request, "ownerportal/setowner.html", context)