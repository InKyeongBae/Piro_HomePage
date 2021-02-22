from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Season) 
class CustomSeasonAdmin(admin.ModelAdmin):
    list_display = ('season_num', 'doc_screening_start', 'doc_result_start', 'final_result_open', 'get_applicants')
    ordering = ['created_at']
    fieldsets = (
        (
            "기수 기본 정보",
            {"fields":("season_num", "poster", "session_start_date", "session_end_date")}
        ),
        (
            "서류 전형 정보",
            {"fields":("doc_screening_info", "doc_screening_start", "doc_screening_end")}
        ),
        (
            "지원서 문항",
            {"fields":("question1", "question2", "question3", "question4", "question5", "coding_test")}
        ),
        (
            "서류 전형 합격 관련",
            {"fields":("doc_meeting_info", "doc_result_start", "doc_result_end")}
        ),
        (
            "면접 전형 정보",
            {"fields":("meeting_place", "meeting_date1", "meeting_date2", "meeting_date3")}
        ),
        (
            "최종 합격자 발표 관련",
            {"fields":("final_info", "final_result_open", "final_result_close", "workshop_date", "workshop_place")}
        )

    )

    def get_applicants(self, obj):
        return obj.applicants.all().count()
    get_applicants.short_description = '지원자 수'
    get_applicants.admin_order_field = '지원자 수'
@admin.register(models.Image)
class CustomImageAdmin(admin.ModelAdmin):
    list_display = ('get_season_num', 'title')
    ordering = ['created_at']
    list_filter = ('season__season_num',)

    def get_season_num(self, obj):
        return obj.season.season_num
    get_season_num.short_description = '기수'
    get_season_num.admin_order_field = '기수'

@admin.register(models.Applicant)
class CustomImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_season_num', 'school', 'phone_number', 'doc_pass', 'meeting_date_time', 'final_pass')
    list_filter = ('season__season_num', 'doc_pass', 'final_pass', 'school', 'major_grade')
    search_fields = ['name', 'school', 'season__season_num']
    fieldsets = (
        (
            "합/불 처리",
            {"fields":("doc_pass","meeting_date_time", "final_pass")}
        ),
        (
            "개인 정보",
            {"fields":("season", "name", "school", "major", "major_grade", "sub_major", "sub_major_semester", "address", "phone_number", "know_check", "avail_meeting_time")}
        ),
        (
            "지원서",
            {"fields":("answer1", "answer2", "answer3", "answer4", "answer5", "code")}
        ),
        (
            "기본 동의 사항",
            {"fields":("participate_check", "workshop_check", "info_check", "deposit_check")}
        )
    )
    def get_season_num(self, obj):
        return obj.season.season_num
    get_season_num.short_description = '기수'
    get_season_num.admin_order_field = '기수'

