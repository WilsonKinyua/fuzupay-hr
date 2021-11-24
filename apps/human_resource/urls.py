from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('api/employees/', views.EmployeeView.as_view(),name="employees"),  # list of employees
    path('api/employees/<str:employee_id>/', views.EmployeeDetail.as_view(),name="employee-detail"), # single employee
    path('api/leaves/', views.LeaveView.as_view(),name="leaves"), # list of leaves
    path('api/leaves/on_leave/', views.OnLeaveEmployees.as_view(),name="on-leave"), # on leave employees
    path('api/leaves/active-staffs/', views.ActiveEmployees.as_view(),name="on-leave"), # active employees
    path('api/departments/', views.DepartmentView.as_view(),name="departments"), # list departments
    path('api/employment_types/', views.EmploymentTypeView.as_view(),name="employment_types"), # list employment types
    path('api/bank_details/', views.BankDetailsView.as_view(),name="bank_details"), # list bank details
    path('api/leaves/<str:id>/update-status/', views.ApproveLeave.as_view(),name="leave-approve"), # approve leave
    path('api/jobs/', views.JobListingView.as_view(),name="jobs"), # list jobs
    path('api/jobs/active/', views.ActiveJobListingView.as_view(),name="active-jobs"), # active job listings
    path('api/jobs/past/', views.ActiveJobListingView.as_view(),name="active-jobs"), # past job listings
    path('api/applications/', views.ApplicationView.as_view(),name="applications"), # list applications
    path('api/applications/new/', views.NewApplicationView.as_view(),name="new-application"), # new application
    path('api/applications/past/', views.PastApplicationView.as_view(),name="past-applications"), # past applications
    path('api/applications/<str:application_id>/', views.ApplicationDetail.as_view(),name="application-detail"),
]