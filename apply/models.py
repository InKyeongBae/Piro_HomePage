from django.db import models

# Create your models here.

class Season(models.Model):
    season_num = models.IntegerField()
    poster = models.ImageField(upload_to="season/poster")

    doc_screening_info = models.TextField()
    doc_screening_start = models.DateTimeField()
    doc_screening_end = models.DateTimeField()
    
    doc_meeting_info = models.TextField()
    doc_result_start = models.DateTimeField()
    doc_result_end = models.DateTimeField()

    meeting_date1 = models.DateField(null=True, blank=True)
    meeting_date2 = models.DateField(null=True, blank=True)
    meeting_date3 = models.DateField(null=True, blank=True)

    final_result_open = models.DateTimeField()
    final_result_close = models.DateTimeField()

    workshop_date = models.DateTimeField()
    workshop_place = models.CharField(max_length=50)

    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    question5 = models.TextField()
    coding_test = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.season_num

class Image(models.Model):
    img = models.ImageField(upload_to="image")

    season = models.ForeignKey(Season, related_name="images", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.img.created_at

class Applicant(models.Model):

    season = models.ForeignKey(Season, related_name="applicants", on_delete=models.CASCADE)
    if season is not None:
        date1 = season.meeting_date1
        



    GRADE = (
        ("1학년", "1학년"),
        ("2학년", "2학년"),
        ("3학년", "3학년"),
        ("4학년", "4학년"),
        ("5학년 이상", "5학년 이상"),
        ("졸업생", "졸업생"),
        ("대학원생", "대학원생"),
    )

    SEMESTER = (
        (1, "1학기"),
        (2, "2학기"),
        (3, "3학기"),
        (4, "4학기"),
        (5, "5학기"),
        (6, "6학기"),
    )

    if season is not None:
        AVAIL_TIME = (
            (f"{season.meeting_date1.month}월 {season.meeting_date1.day}일 {season.meeting_date1.strftime('%A')} 오전", f"{season.meeting_date1.month}월 {season.meeting_date1.day}일 {season.meeting_date1.strftime('%A')} 오전")
            (f"{season.meeting_date1.month}월 {season.meeting_date1.day}일 {season.meeting_date1.strftime('%A')} 오후", f"{season.meeting_date1.month}월 {season.meeting_date1.day}일 {season.meeting_date1.strftime('%A')} 오후"),
            (f"{season.meeting_date2.month}월 {season.meeting_date2.day}일 {season.meeting_date2.strftime('%A')} 오전", f"{season.meeting_date2.month}월 {season.meeting_date2.day}일 {season.meeting_date2.strftime('%A')} 오전"),
            (f"{season.meeting_date2.month}월 {season.meeting_date2.day}일 {season.meeting_date2.strftime('%A')} 오후", f"{season.meeting_date2.month}월 {season.meeting_date2.day}일 {season.meeting_date2.strftime('%A')} 오후"),
        )

    name = models.CharField(max_length=20)
    school = models.CharField(max_length=20)
    major = models.CharField(max_length=20)
    major_grade = models.CharField(max_length=10, choices=GRADE)
    sub_major = models.CharField(max_length=20, null=True, blank=True)
    sub_major_semester = models.IntegerField(null=True, blank=True, choices=SEMESTER)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    avail_meeting_time = models.CharField(max_length=30, choices=AVAIL_TIME)

    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    answer5 = models.TextField()
    code = models.TextField()

    participate_check = models.BooleanField()
    workshop_check = models.BooleanField()
    info_check = models.BooleanField()
    deposit_check = models.BooleanField()
    know_check = models.CharField(max_length=50, choices=KNOW_ROOT)

    doc_pass=models.BooleanField(default=False)
    final_pass=models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


