from django.db import models


class Emp(models.Model):
    class Meta:
        db_table = "emp"
