from django.shortcuts import render

# use 
# Person.skills.tag_model == Tagulous_Person_skills

# Get a list of all tags
tags = Person.skills.tag_model.objects.all()

# Assign a list of tags
instance.skills = ['jump', 'kung fu']

instance = Person.skills.tag_model()