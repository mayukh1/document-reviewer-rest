from rest_framework import serializers

class DomainSerializer(serializers.Serializer):
    domain = serializers.CharField()
    doc_domain_description = serializers.CharField()
    doc_type = serializers.CharField()
    
class KbSerializer(serializers.Serializer):
    kb_job_id = serializers.CharField()
    status = serializers.CharField()
    
class DocStatusSerializer(serializers.Serializer):
    doc_job_id = serializers.CharField()
    status = serializers.CharField()
    
    
class DocFeedbackSerializer(serializers.Serializer):
    doc_job_id = serializers.CharField()
    status = serializers.CharField()
    feedback = serializers.CharField()