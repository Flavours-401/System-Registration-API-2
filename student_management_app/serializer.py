from rest_framework import serializers
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs, SessionYearModel


class student_management_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class Admin_HOD_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AdminHOD
        fields = "__all__"


class Staff_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = "__all__"


class Course_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"


class Subject_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = "__all__"


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class SessionYearModel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYearModel
        fields = "__all__"


class Attendance_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class Attendance_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = "__all__"


class Leave_Student_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStudent
        fields = "__all__"


class Leave_Staff_Report_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStaff
        fields = "__all__"


class Feedback_Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStudent
        fields = "__all__"


class Feedback_Staff_Serializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStaffs
        fields = "__all__"


class Notification_Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStudent
        fields = "__all__"


class Notification_Staffs_Serializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStaffs
        fields = "__all__"
