# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from .models import Lib
from .models import FoodA
from .models import FoodB
from .models import FoodC

admin.site.register(Lib)
admin.site.register(FoodA)
admin.site.register(FoodB)
admin.site.register(FoodC)

# Register your models here.
