from django.contrib import admin
from .models import Department, Division, Section, Staff, BoardMember
from .forms import StaffAdminForm


class DivisionInline(admin.StackedInline):
    model = Division
    extra = 1


class SectionInline(admin.StackedInline):
    model = Section
    extra = 1


class DivisionInline(admin.StackedInline):
    model = Division
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod', 'division_count', 'staff_count')
    inlines = [DivisionInline]

    def division_count(self, obj):
        return obj.divisions.count()

    division_count.short_description = 'Division Count'

    def staff_count(self, obj):
        return Staff.objects.filter(section__division__department=obj).count()

    staff_count.short_description = 'Staff Count'



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod', 'department', 'section_count', 'staff_count')
    inlines = [SectionInline]

    def staff_count(self, obj):
        return Staff.objects.filter(section__division=obj).count()

    def section_count(self, obj):
        return obj.sections.count()

    staff_count.short_description = 'Staff Count'
    section_count.short_description = 'Section Count'





class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'hod', 'division', 'staff_count')

    def staff_count(self, obj):
        return obj.staff_members.count()

    staff_count.short_description = 'Staff Count'




@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user_first_name', 'user_last_name', 'position', 'section', 'division', 'department')
    list_filter = ('section', 'section__division__department')
    form = StaffAdminForm

    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = 'First Name'

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = 'Last Name'

    def division(self, obj):
        return obj.section.division.department.name
    division.short_description = 'Division'

    def department(self, obj):
        return obj.section.division.department.name
    department.short_description = 'Department'

    def section(self, obj):
        return f"{obj.section.name} ({obj.section.division.name}, {obj.section.division.department.name})"
    section.short_description = 'Section'






@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
