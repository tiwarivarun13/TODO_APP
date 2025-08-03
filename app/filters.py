import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    from_date=django_filters.DateFilter(field_name="due_date",lookup_expr='gte')
    to_date=django_filters.DateFilter(field_name="due_date",lookup_expr='lte')
    status=django_filters.ChoiceFilter(choices=Task.STATUS)

    class Meta:
        model=Task
        fields=['from_date','to_date','status']
        
