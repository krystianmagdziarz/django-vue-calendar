from django.http import JsonResponse
from django.views import View

from calendar import monthrange
from datetime import datetime, date

from api.helpers import generate_color


class CalendarJSONView(View):
    """
        Nie ma uzasadnienia użycie DRF przy tak określonych wymaganiach.
        Wstawienie go do tak prostej aplikacji byłoby bardzo nadmiarowe.
    """

    def get(self, request):
        n_days = monthrange(datetime.now().year, datetime.now().month)[1]
        days = [str(date(datetime.now().year, datetime.now().month, day)) for day in range(1, n_days+1)]
        used_colors = set()
        gen = generate_color()

        while len(used_colors) < n_days:
            used_colors.add(next(gen))

        return JsonResponse({
            'days': dict(zip(days, list(used_colors))),
            'today': str(datetime.now().date())
        },
            json_dumps_params={'indent': 2}
        )

