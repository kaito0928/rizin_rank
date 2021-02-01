from django.contrib import admin
from  .models import BantamPlayer,FeatherPlayer,BantamRank,FeatherRank

admin.site.register(BantamPlayer)
admin.site.register(FeatherPlayer)
admin.site.register(BantamRank)
admin.site.register(FeatherRank)