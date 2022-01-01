from rest_framework import serializers
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs


class student_management_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"