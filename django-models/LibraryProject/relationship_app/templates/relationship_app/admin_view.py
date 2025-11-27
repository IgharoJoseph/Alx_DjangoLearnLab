from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden

@login_required
def admin_view(request):
    # Must check role = "Admin"
    if not hasattr(request.user, "role") or request.user.role != "Admin":
        return HttpResponseForbidden("You are not authorized to view this page.")

    # No dashboard needed — plain text response is okay
    return HttpResponse("Welcome to the Admin Page")
