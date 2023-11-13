import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random 
from book.models import Author,Book,Review



def create_author(n):
    fake = Faker()
    for x in range(n):
        Author.objects.create(
            name=fake.name(),
            biography=fake.text(),
            birth_date=fake.date_of_birth()

        )
    print(f"{n}author was added sucessfully")

def create_book(n):
    faker = Faker()
    for x in range(n):
        Book.objects.create(
            title=faker.book(),
            publish_date=faker.url(),
            subtitle=faker.text(),
            email=faker.email(),

        )
    print(f"{n}book was added sucessfully")


def create_review(n):
   
   faker = Faker()
   job_type=['full time','part time','remote','freelance']

   for x in range(n):
       Review.objects.create(
           title=faker.name(),
           description=faker.sentence(),
           company=Company.objects.all().order_by('?')[0],
           vacancy=random.randint(1,5),
           salary_start=random.randint(2000,2500),
           salary_end=random.randint(2300,2800),
           experince=random.randint(1,10),
           category=Category.objects.all().order_by('?')[0],
           job_type=job_type[random.randint(0,3)]

        )
    #print(f"{n}job was added sucessfully")

    


create_category(5)
create_company(100)
create_job(1000)