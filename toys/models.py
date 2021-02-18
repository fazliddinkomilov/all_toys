from django.db import models


class ActiveobjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True, blank=True)

    objects = models.Manager()
    active_objects = ActiveobjectsManager()


class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)


class Toy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name="toys", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="toys")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AdminUser(User):
    is_admin = models.BooleanField(default=True)


class ToyWithLongName(Toy):
    class Meta:
        proxy = True

    def __str__(self):
        return f"Toy with name {self.name}"
