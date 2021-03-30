from django.contrib import admin
# from .models import Question
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Question,Event




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['name','username','score','email','college','mobile','last_updated']
    
    fieldsets = (
        (None, {'fields': ('name','email', 'username','score','college','password','mobile','last_updated')}), )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Event)
