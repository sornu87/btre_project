from django.db import models
from listings.models import Listing

price_choices = Listing.objects.price
