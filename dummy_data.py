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
            biography=fake.profile(),
            birth_date=fake.date_of_birth()

        )
    print(f"{n}author was added sucessfully")

def create_book(n):
    faker = Faker()
    for x in range(n):
        Book.objects.create(
            title=faker.name(),
            publish_date=faker.date_time(),
            price=random.randint(50,150),
            author=Author.objects.all().order_by('?')[0],
            

            
        )
    print(f"{n}book was added sucessfully")


def create_review(n):
   faker = Faker()
   for x in range(n):
       Review.objects.create(
           book=Book.objects.all().order_by('?')[0],
           reviewer_name=faker.name(),
           content=faker.sentence(),
           rating=random.randint(1,5),
        )

    


create_author(100)
create_book(1000)
create_review(3000)