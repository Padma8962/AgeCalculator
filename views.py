from django.shortcuts import render
from datetime import date

def index(request):
    age = None

    if request.method == 'POST':
        day = int(request.POST['day'])
        month = int(request.POST['month'])
        year = int(request.POST['year'])

        try:
            birth_date = date(year, month, day)
            today = date.today()

            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day)
            )

        except ValueError:
            age = "Invalid date"

    return render(request, 'index.html', {'age': age})
