from django.db import models

# Create your models here.
class Domain(models.Model):
    domain = models.CharField(max_length=200, primary_key=True)
    doc_domain_description = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=200)
    def __str__(self):
        return self.domain
    
class KbStatus(models.Model):
    kb_job_id = models.CharField(max_length=50,primary_key=True)
    status = models.CharField(max_length=200)
    def __str__(self):
        return str(self.kb_job_id)
    
class DocStatusFeedback(models.Model):
    doc_job_id = models.CharField(max_length=50,primary_key=True)
    status = models.CharField(max_length=200)
    feedback = models.CharField(max_length=500, null= True, blank=True)
    def __str__(self):
        return str(self.doc_job_id)