import json
from django.http import JsonResponse
from django.db import connection
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_GET
def daily_track_list(request):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, date, title, descrpition, created_at, updated_at "
            "FROM daily_track ORDER BY date DESC"
        )
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    data = [
        dict(zip(columns, row))
        for row in rows
    ]
    # Serialize dates and expose description key (column is descrpition)
    for item in data:
        item["description"] = item.pop("descrpition", item.get("descrpition", ""))
        for key in ("date", "created_at", "updated_at"):
            if item.get(key) is not None:
                item[key] = str(item[key])
    return JsonResponse(data, safe=False)


@require_POST
@csrf_exempt
def create_daily_track(request):
    try:
        body = json.loads(request.body)
        date = body.get("date")
        title = body.get("title")
        description = body.get("description", "")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    if not date or not title:
        return JsonResponse({"error": "date and title required"}, status=400)
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO daily_track (date, title, descrpition, created_at, updated_at) "
            "VALUES (%s, %s, %s, NOW(), NOW())",
            [date, title, description],
        )
    return JsonResponse({"status": "ok"}, status=201)

@require_POST
@csrf_exempt
def update_daily_track(request, id):
    try:
        body = json.loads(request.body)
        date = body.get("date")
        title = body.get("title")
        description = body.get("description", "")
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    if not date or not title:
        return JsonResponse({"error": "date and title required"}, status=400)
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE daily_track SET date = %s, title = %s, descrpition = %s, updated_at = NOW() "
            "WHERE id = %s",
            [date, title, description, id],
        )
        if cursor.rowcount == 0:
            return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse({"status": "ok"})


@require_http_methods(["DELETE"])
@csrf_exempt
def delete_daily_track(request, id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM daily_track WHERE id = %s",
            [id],
        )
        if cursor.rowcount == 0:
            return JsonResponse({"error": "Not found"}, status=404)
    return JsonResponse({"status": "ok"})

