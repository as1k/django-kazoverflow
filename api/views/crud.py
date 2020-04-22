import json

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from api.models import Category, Discussion


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        categories = Category.objects.create(name=data.get('name'))
        return JsonResponse(categories.to_json())


@csrf_exempt
class CategoryList(View):
    def get(self, request):
        categories = Category.objects.all()
        categories_json = [c.to_json() for c in categories]
        return JsonResponse(categories_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        categories = Category.objects.create(name=data.get('name'))
        return JsonResponse(categories.to_json)


@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(category.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        category.name = data.get('name', category.name)
        category.save()
        return JsonResponse(category.to_json())
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class CategoryDetails(View):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
        JsonResponse(category.to_json())

    def put(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            data = json.loads(request.body)
            category.name = data.get('name', category.name)
            category.save()
            return JsonResponse(category.to_json())
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return JsonResponse({'deleted': True})
        except Category.DoesNotExist as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def category_discussions(request, category_id):
    if request.method == 'GET':
        discussions = Discussion.objects.filter(category_id=category_id)
        discussions_json = [d.to_json() for d in discussions]
        return JsonResponse(discussions_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        discussions = Discussion.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            topics_count=data.get('topics_count'),
            posts_count=data.get('posts_count'),
            category_id=data.get('category_id')
        )
        return JsonResponse(discussions.to_json())


@csrf_exempt
class CategoryDiscussions(View):
    def get(self, request, category_id):
        discussions = Discussion.objects.filter(company_id=category_id)
        discussions_json = [d.to_json() for d in discussions]
        return JsonResponse(discussions_json, safe=False)

    def post(self, request, category_id):
        data = json.loads(request.body)
        discussions = Discussion.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            topics_count=data.get('topics_count'),
            posts_count=data.get('posts_count'),
            category_id=data.get('category_id')
        )
        return JsonResponse(discussions.to_json())


@csrf_exempt
def discussion_list(request):
    if request.method == 'GET':
        discussions = Discussion.objects.all()
        discussions_json = [d.to_json() for d in discussions]
        return JsonResponse(discussions_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        discussions = Discussion.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            topics_count=data.get('topics_count'),
            posts_count=data.get('posts_count'),
            category_id=data.get('category_id')
        )
        return JsonResponse(discussions.to_json())


@csrf_exempt
class DiscussionList(View):
    def get(self, request):
        discussions = Discussion.objects.all()
        discussions_json = [d.to_json() for d in discussions]
        return JsonResponse(discussions_json, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        discussions = DiscussionList.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            topics_count=data.get('topics_count'),
            posts_count=data.get('posts_count'),
            category_id=data.get('category_id')
        )
        return JsonResponse(discussions.to_json())


@csrf_exempt
def discussion_detail(request, discussion_id):
    try:
        discussion = Discussion.objects.get(id=discussion_id)
    except Discussion.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        return JsonResponse(discussion.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        discussion.name = data.get('name', discussion.name)
        discussion.description = data.get('description', discussion.description)
        discussion.topics_count = data.get('topics_count', discussion.topics_count)
        discussion.posts_count = data.get('posts_count', discussion.posts_count)
        discussion.category_id = data.get('category_id', discussion.category_id)
        discussion.save()
        return JsonResponse(discussion.to_json())
    elif request.method == 'DELETE':
        discussion.delete()
        return JsonResponse({'deleted': True})


@csrf_exempt
class DiscussionDetails(View):
    def get(self, request, discussion_id):
        try:
            discussion = Discussion.objects.get(id=discussion_id)
            return JsonResponse(discussion.to_json())
        except Discussion.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def put(self, request, vacancy_id):
        try:
            discussion = Discussion.objects.get(id=vacancy_id)
            data = json.loads(request.body)
            discussion.name = data.get('name', discussion.name)
            discussion.description = data.get('description', discussion.description)
            discussion.topics_count = data.get('topics_count', discussion.topics_count)
            discussion.posts_count = data.get('posts_count', discussion.posts_count)
            discussion.category_id = data.get('category_id', discussion.category_id)
            discussion.save()
            return JsonResponse(discussion.to_json())
        except Discussion.DoesNotExist as e:
            return JsonResponse({'error': str(e)})

    def delete(self, request, discussion_id):
        try:
            discussion = Discussion.objects.get(id=discussion_id)
            discussion.delete()
            return JsonResponse({'deleted': True})
        except Discussion.DoesNotExist as e:
            return JsonResponse({'error': str(e)})
