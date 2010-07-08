#----- Evolution for actions
from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('Report', 'interest', models.PositiveSmallIntegerField, initial=0),
    AddField('Report', 'by_client', models.BooleanField, initial=False)
]
#----------------------

