from django.urls import reverse
from django.db import models
from django.utils import timezone


class MessageManager(models.Manager):
    def get_queryset(self):
        return super(MessageManager, self).get_queryset().filter(status='published')


class Message(models.Model):

    ANSWER_CHOICES = (
        ('ans_this_wk', 'this_week'),
        ('ans_this_wk<18', 'this_week<18'),
        ('ans_mr_this_wk', 'mr_this_week'),
        ('ans_ms_this_wk', 'ms_this_week'),
        ('ans_next_wk', 'next_week'),
        ('ans_next_wk<18', 'next_week<18'),
        ('ans_mr_next_wk', 'mr_next_week'),
        ('ans_ms_next_wk', 'ms_next_week'),
        ('ans_other_term', 'other_term'),
        ('ans_other_term_mr', 'mr_other_term'),
        ('ans_other_term_ms', 'ms_other_term'),
        ('ans_office', 'office'),
        ('inv_m_orday', 'inv_m'),
        ('inv_m_wknday', 'inv_m_wknd'),
        ('inv_f_orday', 'inv_f'),
        ('inv_f_wknday', 'inv_f_wknd'),
        ('inv_mr_orday', 'inv_mr'),
        ('inv_mr_wknday', 'inv_mr_wknd'),
        ('inv_ms_orday', 'inv_ms'),
        ('inv_ms_wknday', 'inv_ms_wknd'),
        ('inv_scnd', 'inv_rptd'),
        ('inv_mr_scnd', 'inv_mr_rptd'),
        ('inv_ms_scnd', 'inv_ms_rptd'),
        ('ans_blank', 'manual'),  # to discuss
    )

    selected = models.BooleanField(default=False)
    ans_choice = models.TextField(choices=ANSWER_CHOICES, default='ans_this_wk')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    in_body = models.TextField()   # how to display/build  strand
    out_body = models.TextField
    date = models.DateTimeField(default=timezone.now)  # ultimate date of incoming how to?
    date_hierarchy = 'ad_date'
    status = models.CharField(max_length=10, default='incoming')
    objects = models.Manager()
    # incoming = MessageManager()

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
            return self.date


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Answer(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='published')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):  
        return self.title

    def get_absolute_url(self):
        return reverse('ui_app:answer_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])


class TempPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique_for_date='created')
    author = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
            return self.title

