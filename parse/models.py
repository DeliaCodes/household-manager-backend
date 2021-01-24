from django.db import models

# Create your models here.


class EmailReceiptSendgrid(models.Model):
    headers = models.TextField()
    dkim = models.CharField(max_length=none)
    content_ids = models.CharField(max_length=none)
    to = models.CharField(max_length=none)
    text = models.TextField()
    # @todo is JSONField right?
    html = models.JSONField()
    from = models.CharField(max_length=none)
    sender_ip = models.CharField(max_length=none)
    spam_report = models.TextField()
    envelope = JSONField()
    attachments = models.IntegerField()
    subject = models.CharField(max_length=none)
    spam_score = models.CharField(max_length=none)
    attachment_info = models.JSONField()
    charsets = models.CharField(max_length=none)
    spf = models.CharField(max_length=none)

    def __str__(self):
        return self.subject


class User(models.Model):
    name = models.CharField(max_length=2000)
    email_address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name