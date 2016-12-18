from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class PostsConfig(AppConfig):
    name = 'posts'

    def ready(self):
    	model = self.get_model("admission")
    	watson.register(model,fields=('title','tags','content'))
    	model2 = self.get_model("placement")
    	watson.register(model2,fields=('title','tags','content'))
    	model3 = self.get_model("hostel")
    	watson.register(model3,fields=('title','tags','content'))
    	model4 = self.get_model("acad")
    	watson.register(model4,fields=('title','tags','content'))
    	model5 = self.get_model("other")
    	watson.register(model5,fields=('title','tags','content'))
    	model6 = self.get_model("soc")
    	watson.register(model6,fields=('title','tags','content'))
