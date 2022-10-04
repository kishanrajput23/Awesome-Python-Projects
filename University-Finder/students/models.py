from django.db import models

# Create your models here.


class Level(models.Model):
    CATEGORY = (
        ("High School", "High School"),
        ("Under Graduate", "Under Graduate"),
    )

    level_code = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.level_name


class Degree(models.Model):
    degree_code = models.CharField(primary_key=True, max_length=200)
    degree_name = models.CharField(max_length=200, null=True)
    level_code = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.degree_name


class Student(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    student_id = models.CharField(primary_key=True, max_length=200)
    email = models.EmailField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)
    degree_name = models.ForeignKey(
        Degree, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.student_id


class University(models.Model):
    CATEGORY = (
        ("Under Graduate", "Under Graduate"),
        ("Post Graduate", "Post Graduate"),
    )

    CATEGORY1 = (
            ("B.Tech", "B.Tech"),
            ("MA", "MA"),
            ("B.Sc", "B.Sc"),
            ("BS", "BS"),
            ("BA LLB", "BA LLB"),
            ("B.Des.", "B.Des."),
            ("MBA", "MBA"),
            ("MS", "MS"),
            ("MBBS", "MBBS"),
            ("B.Arch", "B.Arch"),
            ("BE", "BE"),
            ("M.Sc", "M.Sc"),
            ("BA", "BA"),
            ("DO", "DO"),
        )

    CATEGORY2 = (
            ("CSE", "CSE"),
            ("English", "English"),
            ("EECS", "EECS"),
            ("ASL", "ASL"),
            ("GD", "GD"),
            ("HRMS", "HRMS"),
            ("AE", "AE"),
            ("CSD", "CSD"),
            ("MBBS", "MBSS"),
            ("UPA", "UPA"),
            ("ENI", "ENI"),
            ("Physics", "Physics"),
            ("AS", "AS"),
            ("ECE", "ECE"),
            ("HCI", "HCI"),
            ("History", "History"),
            ("Economics", "Economics"),
            ("MECS", "MECS"),
            ("IB", "IB"),
            ("EEE", "EEE"),
            ("Liberal Arts", "Liberal Arts"),
            ("FD", "FD"),
            ("ENT", "ENT"),
            ("CE", "CE"),
        )

    CATEGORY3 = (
            ("India", "India"),
            ("USA", "USA"),
            ("Australia", "Australia"),
            ("Japan", "Japan"),
            ("Singapore", "Singapore"),
            ("China", "China"),
            ("UK", "UK"),
        )

    university_id = models.CharField(primary_key=True, max_length=200)
    university_name = models.CharField(max_length=200, null=True)
    degree = models.CharField(max_length=200, null=True, choices=CATEGORY1)
    course = models.CharField(max_length=200, null=True, choices=CATEGORY2)
    level = models.CharField(max_length=200, null=True, choices=CATEGORY)
    location = models.CharField(max_length=200, null=True, choices=CATEGORY3)
    Website = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.university_id

class University_Info(models.Model):
    univ_id = models.CharField(primary_key=True, max_length=200)
    univ_name = models.CharField(max_length=200, null=True)
    research_paper = models.IntegerField(null=True)
    placement_percent = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    courses_available = models.IntegerField(null=True)
    comp_visit = models.IntegerField(null=True)
    avg_place_amt = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    high_place_amt = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    min_place_amt = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    web = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.univ_name


class Suggestion(models.Model):
    suggestion_code = models.IntegerField(primary_key=True)
    topic1 = models.CharField(max_length=200, null=True)
    topic2 = models.CharField(max_length=200, null=True)
    topic3 = models.CharField(max_length=200, null=True)
    student_id = models.ForeignKey(
        Student, null=True, on_delete=models.SET_NULL)
    university_id = models.ManyToManyField(University)
    code = str(suggestion_code)

    def __str__(self):
        return self.code


class univDegree(models.Model):
    univ_deg_id = models.IntegerField(primary_key=True)
    univ_deg_name = models.CharField(max_length=200, null=True)
    university_id = models.ForeignKey(
        University, null=True, on_delete=models.SET_NULL)
    id = str(univ_deg_id)

    def __str__(self):
        return self.univ_deg_name


class Topics(models.Model):
    topic = models.CharField(max_length=200, null=True)
    univ_deg_id = models.ForeignKey(
        univDegree, null=True, on_delete=models.SET_NULL)
    id = str(univ_deg_id)



class Courses(models.Model):
    course = models.CharField(max_length=200, null=True)
    univ_deg_id = models.ForeignKey(
        univDegree, null=True, on_delete=models.SET_NULL)
    id = str(univ_deg_id)

class DonationInfo(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    zip_code = models.IntegerField(null=True)
    city = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    
