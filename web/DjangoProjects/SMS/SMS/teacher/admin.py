from django.contrib import admin
from teacher.models import Teacher
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    # 配置展示列表，在Teacher版块下方列表展示
    list_display = ('name','email','class_name','gender','phone')
    # 配置过滤查询字段，在Teacher版块右侧显示过滤框
    list_filter = ('class_name','name')
    # 配置可以搜索的字段，在Teacher版块下方显示搜索框
    search_fields = (['class_name','name'])
    # 定义后台列表显示时每页显示的数量
    list_per_page = 30
    # 定义列表现实的顺序，负号表示降序
    ordering = ('-created_at',)
    # 显示字段
    fieldsets = (
        (None,{
            'fields':('name','email','class_name','gender','phone')
        }),
    )

    def save_model(self, request, obj, form, change):
        user = User.objects.create(
            email = request.POST.get('email'), # 获取邮箱
            username = request.POST.get('email'), # 为防止重名，使用email作为用户登录名
            password = make_password(settings.TEACHER_INIT_PASSWORD), # 密码加密
            is_staff = 1 # 允许作为管理员登录后台
        )
        obj.tid = obj.user_id = user.id # 获取新增用户的id，作为tid和user_id
        super().save_model(request,obj,form,change)
        return

    def delete_queryset(self,request,queryset):
        """
        删除多条记录
        同时删除user表中的数据
        由于使用的是批量删除，所以需要遍历delete_queryset中的queryset
        """
        for obj in queryset:
            obj.user.delete()
        super().delete_model(request,obj)
        return

    def delete_model(self, request, obj):
        """
        删除单条记录
        同时删除user表中数据
        """
        super().delete_model(request,obj)
        if obj.user:
            obj.user.delete()
        return

# 设置后台页面头部显示的内容和页面标题
admin.site.site_header = '智慧星学生管理系统'
admin.site.site_title = '智慧星学生管理系统'
# 绑定Teacher模型到TeacherAdmin管理后台
admin.site.register(Teacher,TeacherAdmin)
