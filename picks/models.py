from django.db import models

class Sclass(models.Model):
    class_name = models.CharField(max_length=50)
    display_title = models.CharField(max_length=50)
    enter_school_year = models.IntegerField()
    grade_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'sclasses'

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    sclasses_id = models.IntegerField()
    identity_number = models.CharField(max_length=18, unique=True, blank=False, null=False)
    gender = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'students'

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    gender = models.IntegerField()
    is_head_teacher = models.IntegerField()
    subjects_id = models.IntegerField(null=True)
    display_name = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'teachers'

class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'subjects'

class EvaluateIndex(models.Model):
    index_txt = models.CharField(max_length=50)
    index_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'evaluate_indexs'

class EvaluateItem(models.Model):
    item_txt = models.CharField(max_length=50)
    is_praise = models.CharField(max_length=10, blank=True, null=True)
    sclasses_id = models.IntegerField(null=True)
    score = models.IntegerField()
    evaluate_indexs_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
      db_table = 'evaluate_items'

class EvaluateLog(models.Model):
    students_id = models.IntegerField()
    teachers_id = models.IntegerField()
    evaluate_items_id = models.IntegerField()
    evaluate_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
        
    class Meta:
      db_table = 'evaluate_logs'