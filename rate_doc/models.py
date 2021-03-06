# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms



# Create your models here.

class Doc(models.Model):
    
    rated = models.BooleanField(default=False)

    ARTICLE_CLASSIFICATION_QUESTIONS = (('yes', 'Yes'), ('no', 'No'))
    PRODUCT_MENTION_CHOICES = (('title', "Article title"), ('subject', 'Subject section'), ('body', "Main body of the text"))
    
    assignedTo = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='assigned_user')
    ratedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    # aboutProductLaunch = models.CharField(blank=True, choices=ARTICLE_CLASSIFICATION_QUESTIONS, verbose_name = "Is this article specifically about a product launch?", max_length= 20)
    # aboutProductApproval = models.CharField(blank=True, choices=ARTICLE_CLASSIFICATION_QUESTIONS, verbose_name = "Is this article about an approval for a product?", max_length= 20)
    # mentionsProduct = models.CharField(blank=True, choices=PRODUCT_MENTION_CHOICES, verbose_name = "If the article mentions the product by name, where is it mentioned?", max_length= 20)
    # ifProductInBodyWhere = models.CharField(blank = True, verbose_name = "If the product is mentioned in the body, approximately where is it mentioned?", max_length= 200)
    # subjectProduct = models.CharField(blank = True, verbose_name = "If the product is mentioned anywhere, what is its name?", max_length= 200)
    # subjectCompany = models.CharField(blank = True, verbose_name = "What company is the article about, if any?", max_length= 200)
    # otherCompany = models.CharField(blank = True, verbose_name = "What other companies are mentioned in the article?", max_length= 200)
    # otherProduct = models.CharField(blank = True, verbose_name = "What other products are mentioned in the article?", max_length= 200)

    ARTICLE_SUBJECT_CHOICES = (('launch', 'Product Launch'), ('fdaApproval', 'FDA Approval'), ('neither','Neither'))

    articleTopic = models.CharField(blank=True, choices=ARTICLE_SUBJECT_CHOICES, 
        verbose_name = "What is this article mainly about?", max_length= 20)
    productName = models.CharField(blank = True, 
        verbose_name = "If the article is about a product launch or FDA approval, what is the name of the product? Please separate multiple answers by commas.", max_length= 200)
    companyName = models.CharField(blank = True, 
        verbose_name = "If the article is about a product launch or FDA approval, what is the name of the company which launched the product or acquired approval?", max_length= 200)
    dateOfApprovalOrLaunch = models.CharField(blank = True, 
        verbose_name = "If the article is about a product launch or FDA approval, what is the date of the launch or approval, if mentioned?", max_length= 200)
    countryOfLaunch = models.CharField(blank = True, 
        verbose_name = "If the article is about a product launch, what is the country in which the launch took place, if mentioned? ", max_length= 200)
    otherCompanies = models.CharField(blank = True, 
        verbose_name = "What other companies are mentioned in the article, if any? Please separate multiple answers by commas.", max_length= 200)
    otherProducts = models.CharField(blank = True, 
        verbose_name = "What other products are mentioned in the article, if any? Please separate multiple answers by commas.", max_length= 200)

    # Other Shit
    article_title = models.TextField()
    subject	= models.TextField()
    company	= models.TextField()
    publication_title = models.TextField()
    publication_date = models.DateField(null=True)
    publication_subject = models.TextField()
    source_type = models.TextField()
    document_type = models.TextField()
    html = models.TextField()
