from django.urls import path
from document_reviewer_rest_app.api.views import knowledgeBase_submit, document_submit, kb_status, doc_status, domains, doc_feedback
urlpatterns = [
    path('kb/submit', knowledgeBase_submit, name='knowledgeBase-submit'),
    path('doc/submit', document_submit, name='document-submit'),
    path('kb/status', kb_status, name='kb-status'),
    path('doc/status', doc_status, name='doc-status'),
    path('domains', domains, name='domains'),
    path('doc/feedback', doc_feedback, name='doc-feedback'),
]

