'''
1. Заполнить таблицы с помощью Peewee.
'''

import datetime
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
    country_id = peewee.ForeignKeyField(Countries, related_name="locations")


class Departments(BaseModel):
    department_id = peewee.AutoField()
    department_name = peewee.CharField(50)
    manager_id = peewee.IntegerField()
    location_id = peewee.ForeignKeyField(Locations, related_name="dapartments")


class Jobs(BaseModel):
    job_id = peewee.AutoField()
    job_title = peewee.CharField(50)


class Job_history(BaseModel):
    start_date = peewee.DateField()
    end_date = peewee.DateField()
    department_id = peewee.ForeignKeyField(Departments, related_name="job_history")


class Empoloyees(BaseModel):
    first_name = peewee.CharField(50)
    last_name = peewee.CharField(50)
    employee_id = peewee.AutoField()
    job_id = peewee.ForeignKeyField(Jobs, related_name="employees")
    manager_id = peewee.IntegerField()
    department_id = peewee.ForeignKeyField(Departments, related_name="employees")


Empoloyees.drop_table()
Job_history.drop_table()
Jobs.drop_table()
Departments.drop_table()
Locations.drop_table()
Countries.drop_table()
Regions.drop_table()

Regions.create_table()
Countries.create_table()
Locations.create_table()
Departments.create_table()
Jobs.create_table()
Job_history.create_table()
Empoloyees.create_table()

# Regions
reg_cent_america = Regions.create(region_name="Central America")
reg_east_asia = Regions.create(region_name="East Asia")
reg_east_europe = Regions.create(region_name="East Europe")
reg_south_africa = Regions.create(region_name="South Africa")

# Countries
bel_country = Countries.create(country_name="Belarus",
                               region_id=reg_east_europe
                               )
lesotho_country = Countries.create(country_name="Lesotho",
                                   region_id=reg_south_africa
                                   )
mexico_country = Countries.create(country_name="Mexico",
                                  region_id=reg_cent_america
                                  )
japan_country = Countries.create(country_name="Japan",
                                 region_id=reg_east_asia
                                 )

# Locations
loc_tijuana = Locations.create(street_address="Paseo de Los Heroes str.",
                               postal_code="501234",
                               city="Tijuana",
                               country_id=mexico_country
                               )
loc_maseru = Locations.create(street_address="Kingsway str.",
                              postal_code="782340",
                              city="Maseru",
                              country_id=lesotho_country
                              )
loc_minsk = Locations.create(street_address="Kirova str.",
                             postal_code="220016",
                             city="Minsk",
                             country_id=bel_country
                             )
loc_tokio = Locations.create(street_addres="Omotesando str.",
                             postal_code="467032",
                             city="Tokio",
                             country_id=japan_country
                             )

# Departments
depart_administration = Departments.create(department_name="Adminstration",
                                           manager_id=114,
                                           location_id=loc_tokio
                                           )
depart_marketing = Departments.create(department_name="Marketing",
                                      manager_id=234,
                                      location_id=loc_tijuana
                                      )
depart_it = Departments.create(department_name="IT",
                               manager_id=311,
                               location_id=loc_minsk
                               )
depart_shipping = Departments.create(departmet_name="Shipping",
                                     manager_id=465,
                                     location_id=loc_maseru
                                     )

# Jobs
job_programmer = Jobs.create(job_title="Programmer")
job_marketing_manager = Jobs.create(job_title="Marketing Manager")
job_administration_president = Jobs.create(job_title="Administration President")
job_shipping = Jobs.create(job_title="Sales Manager")

# JobHistory
job_history_dep_marketing = Job_history.create(start_date="2021,02,01",
                                               end_date=datetime.date.today(),
                                               department_id=depart_marketing
                                               )
job_history_dep_shipping = Job_history.create(start_date="1998-02-10",
                                              end_date=datetime.date.today(),
                                              department_id=depart_shipping
                                              )
job_history_dep_it = Job_history.create(start_date="2021,02,26",
                                        end_date=datetime.date.today(),
                                        department_id=depart_it
                                        )
job_history_dep_admin = Job_history.create(start_date="1996,12,04",
                                           end_date=datetime.date.today(),
                                           department_id=depart_administration
                                           )

# Employees
employee_administration = Empoloyees.create(first_name="David",
                                            last_name="Cooper",
                                            job_id=job_administration_president,
                                            manager_id=375,
                                            department_id=depart_administration
                                            )
employee_shipping = Empoloyees.create(first_name="Ron",
                                      last_name="Weasley",
                                      job_id=job_shipping,
                                      manager_id=467,
                                      department_id=depart_shipping
                                      )
employee_programmer = Empoloyees.create(first_name="Alex",
                                        last_name="Bush",
                                        job_id=job_programmer,
                                        manager_id=786,
                                        department_id=depart_it
                                        )
employee_marketing = Empoloyees.create(first_name="Jimmy",
                                       last_name="Hendrix",
                                       job_id=job_marketing_manager,
                                       manager_id=111,
                                       department_id=depart_marketing
                                       )






