from django.shortcuts import get_object_or_404, render, redirect
from .models import Gallery


def gallery_list(request):
    images = Gallery.objects.all().order_by("-updated_at")
    return render(request, "gallery/gallery.html", {"images": images})


def add_image_page(request):
    return render(request, "gallery/add-image.html")


def add_image(request):
    if request.method != "POST":
        return redirect("gallery-list")
    uploaded_file = request.FILES.get("upload-image")
    caption = request.POST.get("caption", "")
    excerpt = request.POST.get("excerpt") or ""
    if uploaded_file:
        Gallery.objects.create(image=uploaded_file, caption=caption, excerpt=excerpt or None)
    return redirect("gallery-list")


def image_detail(request, slug):
    image = get_object_or_404(Gallery, image_slug=slug)
    return render(request, "gallery/image-detail.html", {
        "image": image,
        "caption": image.caption,
        "excerpt": image.excerpt,
        "uploaded_at": image.uploaded_at,
        "updated_at": image.updated_at,
    })


def delete_image(request, slug):
    if request.method != "POST":
        return redirect("gallery-list")
    image = get_object_or_404(Gallery, image_slug=slug)
    image.delete()
    return redirect("gallery-list")