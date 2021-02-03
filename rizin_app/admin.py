from django.contrib import admin
from  .models import BantamPlayer,FeatherPlayer,RightPlayer,BantamRank,FeatherRank,RightRank

admin.site.register(BantamPlayer)
admin.site.register(FeatherPlayer)
admin.site.register(RightPlayer)
admin.site.register(BantamRank)
admin.site.register(FeatherRank)
admin.site.register(RightRank)