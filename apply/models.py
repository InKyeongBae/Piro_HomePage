from django.db import models

# Create your models here.

class Season(models.Model):
    season_num = models.IntegerField(verbose_name="모집 기수")
    poster = models.ImageField(upload_to="season/poster", verbose_name="모집 포스터", help_text="포스터는 가로 3.2 세로 1의 비율로 제작해주시기 바랍니다")

    session_start_date = models.DateField(verbose_name="세션 시작일")
    session_end_date = models.DateField(verbose_name="세션 종료일")

    meeting_place = models.CharField(max_length=50, null=True, blank=True)
    meeting_date1 = models.DateField(null=True, blank=True, verbose_name="면접 후보일 1")
    meeting_date2 = models.DateField(null=True, blank=True, verbose_name="면접 후보일 2")
    meeting_date3 = models.DateField(null=True, blank=True, verbose_name="면접 후보일 3")

    doc_screening_info = models.TextField(verbose_name="서류전형 관련 추가 안내", null=True, blank=True, help_text="join us 페이지 메인 포스터 밑에 배치됩니다. 서류전형 추가 전달 사항을 한 줄로 짧게 입력해주세요. 긴급 전달 사항도 가능!")
    doc_screening_start = models.DateTimeField(verbose_name="서류전형 지원 시작일시")
    doc_screening_end = models.DateTimeField(verbose_name="서류전형 지원 마감일시")

    question1 = models.TextField(verbose_name="서류전형 문제1")
    question2 = models.TextField(verbose_name="서류전형 문제2")
    question3 = models.TextField(verbose_name="서류전형 문제3")
    question4 = models.TextField(verbose_name="서류전형 문제4")
    question5 = models.TextField(verbose_name="서류전형 문제5")
    coding_test = models.TextField(verbose_name="코딩테스트 문제", help_text="코딩테스트 보조 사진들은 apply-images 모델에 보여질 순서대로 추가해주세요")
    
    doc_meeting_info = models.TextField(verbose_name="면접전형 관련 추가 안내", null=True, blank=True, help_text="서류전형 결과 발표 페이지 하단에 들어갑니다. 면접관련 추가 전달 사항을 입력해주세요")
    doc_result_start = models.DateTimeField(verbose_name="서류전형 결과 발표 시작일시")
    doc_result_end = models.DateTimeField(verbose_name="서류전형 결과 발표 마감일시")

    final_info = models.TextField(null=True, blank=True, verbose_name="최종발표 관련 추가 안내", help_text="최종 결과 발표 페이지 하단에 들어갑니다. 최종 합격자 합격 등록 절차 등 전달 사항을 입력해주세요")
    final_result_open = models.DateTimeField(verbose_name="최종발표 시작일시")
    final_result_close = models.DateTimeField(verbose_name="최종발표 마감일시")

    workshop_date = models.DateTimeField(verbose_name="워크샵 요일")
    workshop_place = models.CharField(max_length=50, verbose_name="워크샵 장소")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, verbose_name="공개")

    def __str__(self):
        return f'{self.season_num}기 모집'

class Image(models.Model):
    img = models.ImageField(upload_to="image", verbose_name="코딩테스트 문제 관련 이미지", help_text="사진은 등록 순서대로 지원서 페이지에 올라갑니다")
    title = models.CharField(max_length=100, verbose_name="사진 제목", help_text="지원서에서 사진 위에 보여집니다 ex)코딩테스트 조건 / 출력 결과")

    season = models.ForeignKey(Season, related_name="images", on_delete=models.CASCADE, verbose_name="모집 기수")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.season.season_num}-코딩테스트 문제 사진'

class Applicant(models.Model):

    GRADE = (
        ("1학년", "1학년"),
        ("2학년", "2학년"),
        ("3학년", "3학년"),
        ("4학년", "4학년"),
        ("5학년 이상", "5학년 이상"),
        ("졸업생", "졸업생"),
        ("대학원생", "대학원생"),
    )



    YES_NO = (
        ("예", "예"),
        ("아니오", "아니오"),
    )

    AGREE_NOR = (
        ("동의", "동의"),
        ("비동의", "비동의"),
    )

    KNOW_ROOT = (
        ("sns", "피로그래밍 공식 SNS(예 - 페이스북, 인스타그램)"),
        ("cafe community", "네이버 카페/동아리 관련 커뮤니티(예 - 스펙업, 링커리어, 캠퍼스픽)"),
        ("everytime", "에브리타임"),
        ("friends", "지인의 소개"),
        ("others", "기타"),
    )

    name = models.CharField(max_length=20, verbose_name="이름")

    doc_pass=models.BooleanField(default=False, verbose_name="서류전형 합격")
    meeting_date_time = models.DateTimeField(null=True, blank=True, verbose_name="지원자 면접시간")

    final_pass=models.BooleanField(default=False, verbose_name="최종 합격")

    school = models.CharField(max_length=20, verbose_name="학교")
    major = models.CharField(max_length=20, verbose_name="전공")
    major_grade = models.CharField(max_length=10, choices=GRADE, verbose_name="전공 학년")
    sub_major = models.CharField(max_length=20, null=True, blank=True, default="없음", verbose_name="부전공")
    sub_major_semester = models.IntegerField(null=True, blank=True, verbose_name="부전공 이수 학기")
    address = models.CharField(max_length=100, verbose_name="거주지")
    phone_number = models.CharField(max_length=15, verbose_name="전화번호")

    avail_meeting_time = models.CharField(max_length=300, verbose_name="면접 가능 일자")

    answer1 = models.TextField(verbose_name="서류전형 문제1 답안")
    answer2 = models.TextField(verbose_name="서류전형 문제2 답안")
    answer3 = models.TextField(verbose_name="서류전형 문제3 답안")
    answer4 = models.TextField(verbose_name="서류전형 문제4 답안")
    answer5 = models.TextField(verbose_name="서류전형 문제5 답안")
    code = models.TextField(verbose_name="코딩테스트 답안")

    participate_check = models.CharField(max_length=10, choices=YES_NO, verbose_name="모든 일정 참석 여부")
    workshop_check = models.CharField(max_length=10, choices=YES_NO, verbose_name="워크샵 참석 여부")
    info_check = models.CharField(max_length=10, choices=AGREE_NOR, verbose_name="개인정보 이용 동의")
    deposit_check = models.CharField(max_length=10, choices=AGREE_NOR, verbose_name="보증금 납부 동의")
    know_check = models.CharField(max_length=50, choices=KNOW_ROOT, verbose_name="피로그래밍 알게 된 경로")

    season = models.ForeignKey(Season, related_name="applicants", on_delete=models.CASCADE, verbose_name="모집기수")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def add_meeting_date(self, date1, date2):
        if date1 is not None:
            t1 = (f"{date1.month}월 {date1.day}일 {date1.strftime('%A')} 오전", f"{date1.month}월 {date1.day}일 {date1.strftime('%A')} 오전")
            t2 = (f"{date1.month}월 {date1.day}일 {date1.strftime('%A')} 오후", f"{date1.month}월 {date1.day}일 {date1.strftime('%A')} 오후")
            # self.AVAIL_TIME += t1
            # self.AVAIL_TIME += t2
        if date2 is not None:
            t3 = (f"{date2.month}월 {date2.day}일 {date2.strftime('%A')} 오전", f"{date2.month}월 {date2.day}일 {date2.strftime('%A')} 오전")
            t4 = (f"{date2.month}월 {date2.day}일 {date2.strftime('%A')} 오후", f"{date2.month}월 {date2.day}일 {date2.strftime('%A')} 오후")
            # self.AVAIL_TIME += t3
            # self.AVAIL_TIME += t4
