from django.shortcuts import render

def home(request):
    # Example posts data
    posts = [
        {"pk": 1, "title": "First Post", "created_at": "2025-09-21"},
        {"pk": 2, "title": "Second Post", "created_at": "2025-09-20"},
    ]
    return render(request, "Reserves/home.html", {"posts": posts})

# Sample detail view
def detail(request, pk):
    # Example post lookup
    post = {"pk": pk, "title": f"Post {pk}", "created_at": "2025-09-21"}
    return render(request, "Reserves/detail.html", {"post": post})