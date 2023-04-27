from django.db import models
from users.models import CustomUser


class Department(models.Model):
    name = models.CharField(max_length=100)
    hod = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='hod_department')
    mandate = models.TextField(blank=True)
    charter = models.FileField(upload_to='charters/', null=True, blank=True)
    vision = models.ImageField(upload_to='visions/', null=True, blank=True)
    strategy = models.ImageField(upload_to='strategies/', null=True, blank=True)
    description = models.TextField(blank=True)
    performance_score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def staff_count(self):
        sections = Section.objects.filter(division__department=self)
        return sections.aggregate(total_staff_count=models.Count('staff_members'))['total_staff_count']
    
    staff_count.short_description = 'Staff Count'


    
class Division(models.Model):
    name = models.CharField(max_length=100)
    hod = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='hod_division')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='divisions')
    mandate = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def staff_count(self):
        return self.sections.aggregate(total_staff_count=models.Count('staff'))['total_staff_count']
    staff_count.short_description = 'Staff Count'
    
class Section(models.Model):
    name = models.CharField(max_length=100)
    hod = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='hod_section')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='sections')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    def staff_count(self):
        return self.staff.count()
    staff_count.short_description = 'Staff Count'
    
    
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_started = models.DateField(null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    professional_associations = models.TextField(null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    personal_interest = models.TextField(null=True, blank=True)
    work_history = models.TextField(null=True, blank=True)
    career_statement = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    awards = models.TextField(null=True, blank=True)

    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, related_name='staff_members')

    def __str__(self):
        return self.user.username




class BoardMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='board_members/')
    role = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.name
