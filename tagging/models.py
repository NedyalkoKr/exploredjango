from django.db import models
from tagulous.models import SingleTagField, TagField, TagModel

# creating a Custom tag model

class Hobbies(TagModel):
    description = models.CharField(max_length=100, default='', blank=True)

    class TagMeta:
        initial = "eating, coding, gaming"
        force_lowercase = True
        #autocomplete_view = 'myapp.views.hobbies_autocomplete'

# automatic creation of tag models 
# if we choose to use tag fileds on a none tag model

class Person(models.Model):
    name = models.CharField(max_length=255)
    
    title = SingleTagField(
        initial='Mr, Mrs, Ms'
    )

    # TagField( is a ManyToMany type of a field)
    skills = TagField(
        # tag_options
        force_lowercase=True,
        # form_items=
        # update=
        # items=
        max_count=5,
    ) 

    hobbies = SingleTagField(to=Hobbies)

    def __str__(self):
        return f'{self.name}'



