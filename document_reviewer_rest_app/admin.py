from django.contrib import admin
from document_reviewer_rest_app.models import Domain, KbStatus, DocStatusFeedback

admin.site.register(Domain)
admin.site.register(KbStatus)
admin.site.register(DocStatusFeedback)