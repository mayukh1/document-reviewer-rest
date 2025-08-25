from rest_framework.response import Response
from rest_framework.decorators import api_view
from document_reviewer_rest_app.models import Domain, KbStatus, DocStatusFeedback
from document_reviewer_rest_app.api.serializers import DomainSerializer, KbSerializer, DocStatusSerializer, DocFeedbackSerializer
from document_reviewer_rest_app.pub import publish_data_on_redis
from document_reviewer_rest_app.utils.common import generate_id
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='POST',
    request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'agent_call': openapi.Schema(type=openapi.TYPE_STRING, description='agent_call'),
                'kb_url': openapi.Schema(type=openapi.TYPE_STRING, description='kb_url'),
                'domain': openapi.Schema(type=openapi.TYPE_STRING, description='domain'),
                'doc_type': openapi.Schema(type=openapi.TYPE_STRING, description='doc_type')
            },
            required=['agent_call', 'kb_url', 'domain', 'doc_type']
        )
    ),
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'kb_job_id': openapi.Schema(type=openapi.TYPE_STRING, description='kb_job_id'),
                                'agent_call': openapi.Schema(type=openapi.TYPE_STRING, description='agent_call'),
                                'kb_url': openapi.Schema(type=openapi.TYPE_STRING, description='kb_url'),
                                'domain': openapi.Schema(type=openapi.TYPE_STRING, description='domain'),
                                'doc_type': openapi.Schema(type=openapi.TYPE_STRING, description='doc_type')
                            },
                            required=['kb_job_id', 'agent_call',
                                      'kb_url', 'domain', 'doc_type']
                        )
            )
        )
    }
)
@api_view(['POST'])
def knowledgeBase_submit(request):
    if request.method == 'POST':
        kbList = []
        for kb in request.data:
            kb['kb_job_id'] = generate_id('KB')
            publish_data_on_redis(kb, 'kb-topic')
            kbList.append(kb)
        return Response(kbList, status=201)


@swagger_auto_schema(
    method='POST',
    request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'agent_call': openapi.Schema(type=openapi.TYPE_STRING, description='agent_call'),
                'doc_url': openapi.Schema(type=openapi.TYPE_STRING, description='doc_url'),
                'domain': openapi.Schema(type=openapi.TYPE_STRING, description='domain'),
                'doc_type': openapi.Schema(type=openapi.TYPE_STRING, description='doc_type')
            },
            required=['agent_call', 'doc_url', 'domain', 'doc_type']
        )
    ),
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'doc_job_id': openapi.Schema(type=openapi.TYPE_STRING, description='doc_job_id'),
                                'agent_call': openapi.Schema(type=openapi.TYPE_STRING, description='agent_call'),
                                'doc_url': openapi.Schema(type=openapi.TYPE_STRING, description='doc_url'),
                                'domain': openapi.Schema(type=openapi.TYPE_STRING, description='domain'),
                                'doc_type': openapi.Schema(type=openapi.TYPE_STRING, description='doc_type')
                            },
                            required=['doc_job_id', 'agent_call',
                                      'kb_url', 'domain', 'doc_type']
                        )
            )
        )
    }


)
@api_view(['POST'])
def document_submit(request):
    if request.method == 'POST':
        docList = []
        for doc in request.data:
            doc['doc_job_id'] = generate_id('DOC')
            publish_data_on_redis(doc, 'doc-topic')
            docList.append(doc)
        return Response(docList, status=201)


@swagger_auto_schema(
    method='GET',
    manual_parameters=[
            openapi.Parameter(
                'kb_job_id', 
                openapi.IN_QUERY, 
                description="A description for your query parameter.", 
                type=openapi.TYPE_STRING, 
            )
        ],
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'kb_job_id': openapi.Schema(type=openapi.TYPE_STRING, description='kb_job_id'),
                            'status': openapi.Schema(type=openapi.TYPE_STRING, description='status'),
                        },
                required=['kb_job_id', 'status']

            )
        )
    }
)
@api_view(['GET'])
def kb_status(request):
    if request.method == 'GET':
        kbStatus = KbStatus.objects.get(kb_job_id=request.GET.get('kb_job_id'))
        serializer = KbSerializer(kbStatus)
        return Response(serializer.data)

@swagger_auto_schema(
    method='GET',
    manual_parameters=[
            openapi.Parameter(
                'doc_job_id', 
                openapi.IN_QUERY, 
                description="A description for your query parameter.", 
                type=openapi.TYPE_STRING, 
            )
        ],
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'doc_job_id': openapi.Schema(type=openapi.TYPE_STRING, description='doc_job_id'),
                            'status': openapi.Schema(type=openapi.TYPE_STRING, description='status'),
                        },
                required=['doc_job_id', 'status']

            )
        )
    }
)
@api_view(['GET'])
def doc_status(request):
    if request.method == 'GET':
        docStatus = DocStatusFeedback.objects.get(
            doc_job_id=request.GET.get('doc_job_id'))
        serializer = DocStatusSerializer(docStatus)
        return Response(serializer.data)


@swagger_auto_schema(
    method='GET',
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'domain': openapi.Schema(type=openapi.TYPE_STRING, description='domain'),
                            'doc_domain_description': openapi.Schema(type=openapi.TYPE_STRING, description='doc_domain_description'),
                            'doc_type': openapi.Schema(type=openapi.TYPE_STRING, description='doc_type'),
                        },
                required=['domain', 'doc_type']

            )
        )
    }
)
@api_view(['GET'])
def domains(request):
    if request.method == 'GET':
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return Response(serializer.data)


@swagger_auto_schema(
    method='GET',
    manual_parameters=[
            openapi.Parameter(
                'doc_job_id', 
                openapi.IN_QUERY, 
                description="A description for your query parameter.", 
                type=openapi.TYPE_STRING, 
            )
        ],
    responses={
        200: openapi.Response(
            description='200 Response',
            schema=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'doc_job_id': openapi.Schema(type=openapi.TYPE_STRING, description='doc_job_id'),
                            'status': openapi.Schema(type=openapi.TYPE_STRING, description='status'),
                            'feedback': openapi.Schema(type=openapi.TYPE_STRING, description='feedback'),
                        },
                required=['doc_job_id', 'status','feedback']

            )
        )
    }
)
@api_view(['GET'])
def doc_feedback(request):
    if request.method == 'GET':
        docFeedback = DocStatusFeedback.objects.get(
            doc_job_id=request.GET.get('doc_job_id'))
        serializer = DocFeedbackSerializer(docFeedback)
        return Response(serializer.data)
