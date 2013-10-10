from django.db import models


class Course(models.Model):
    num = models.CharField(max_length=100, primary_key=True)
    desc = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s - %s' % (self.num, self.desc)


class Externship(models.Model):

    base_url = 'https://alum.mit.edu/externship/2014/applicant/externship/%d'

    id = models.IntegerField(primary_key=True)
    url = models.URLField(max_length=100)

    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    dates = models.CharField(max_length=100)

    stipend = models.CharField(max_length=200)
    transportation_assistance = models.CharField(max_length=200)
    housing_assistance = models.CharField(max_length=200)

    application_count = models.IntegerField()
    number_of_externs = models.IntegerField()
    extern_level_preference = models.CharField(max_length=100)
    requirements = models.TextField()

    name = models.CharField(max_length=100)
    web_address = models.URLField(max_length=100)
    sponsors_job_title = models.CharField(max_length=100)
    externship_location = models.CharField(max_length=100)

    extern_course_preference = models.ManyToManyField('Course')

    def __unicode__(self):
        return u'%d - %s with %s' % (self.id, self.title, self.name)
    
    def __init__(self, *args, **kwargs):
        self.courses = kwargs.pop('extern_course_preference', '')

        super(Externship, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        # reformat the extern course preference

        courses = filter(bool, self.courses.split('\n'))

        self.url = self.base_url % self.id
        super(Externship, self).save(*args, **kwargs)

        courses = [course.strip() for course in courses]

        for idx, course in enumerate(courses):
            num, desc = course.split('-')
            course_obj, _ = Course.objects.get_or_create(num=num, desc=desc)

            courses[idx] = course_obj

        self.extern_course_preference.add(*courses)

