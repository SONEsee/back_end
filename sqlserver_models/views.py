from django.views.generic import ListView
from .models import EnterpriseInfo2

class EnterpriseInfoListView(ListView):
    model = EnterpriseInfo2
    template_name = 'enterprise_list.html'
