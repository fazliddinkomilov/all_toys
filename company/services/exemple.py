from django.db import transaction

from company.models import Company, Employee


def rc():
    with transaction.atomic():
        company = Company.objects.get(id=1)
        company.name = "Apple"
        company.description = "Big and famous companyaaaaaa"
        company.save()
        try:
            with transaction.atomic():
                Employee.salary + (Employee.salary / 100 * 10)
                raise Exception('ERROR!')
        except Exception:
            pass
    print("done")
