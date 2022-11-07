import peewee
from db_conection import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Regions(BaseModel):
    region_id = peewee.AutoField()
    region_name = peewee.CharField(50)


class Countries(BaseModel):
    country_id = peewee.AutoField()
    country_name = peewee.CharField(50)
    region_id = peewee.ForeignKeyField(Regions, related_name="countries")


class Locations(BaseModel):
    location_id = peewee.AutoField()
    street_address = peewee.CharField(50)
    postal_code = peewee.CharField(50)
    city = peewee.CharField(50)
    state_province = peewee.CharField(50)
    country_id = peewee.ForeignKeyField(Countries, related_name="locations")


class Departments(BaseModel):
    department_id = peewee.AutoField()
    department_name = peewee.CharField(50)
    manager_id = peewee.CharField(50)
    location_id = peewee.ForeignKeyField(Countries, related_name="dapartments")


class Jobs(BaseModel):
    job_id = peewee.AutoField()
    job_title = peewee.CharField(50)


class Empoloyees(BaseModel):
    employee_id = peewee.AutoField()
    first_name = peewee.CharField(50)
    last_name = peewee.CharField(50)
    email = peewee.CharField(50)
    phone_number = peewee.CharField(50)



