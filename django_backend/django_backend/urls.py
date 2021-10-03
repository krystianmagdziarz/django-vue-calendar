from api.views import CalendarJSONView
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/calendar', CalendarJSONView.as_view(), name="calendar-json")
]
