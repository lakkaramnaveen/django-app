from django.db import models  # Import the models module from Django

# Define the DetailsModel class which inherits from models.Model
class DetailsModel(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key field that auto-increments
    name = models.CharField(max_length=100)  # CharField for name with a max length of 100 characters
    age = models.CharField(max_length=100)  # CharField for age with a max length of 100 characters
    city = models.CharField(max_length=100)  # CharField for city with a max length of 100 characters
    country = models.CharField(max_length=100)  # CharField for country with a max length of 100 characters

    def __str__(self):
        # String representation of the model, which returns the name field or an empty string if name is None
        return self.name or '' 
