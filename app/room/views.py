from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room

from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


class SearchResultsList(ListView):
    model = Message
    template_name = 'room/search.html'
    context_object_name = 'messages'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Message.objects.filter(
            Q(content__icontains=query)
        )


# Preview
#    def get_queryset(self):
#        query = self.request.GET.get("q")
#        search_vector = SearchVector("name", "quote")
#        search_query = SearchQuery(query)
#        search_headline = SearchHeadline("quote", search_query)
#        return Message.objects.annotate(
#            search=search_vector,
#            rank=SearchRank(search_vector, search_query)
#        ).annotate(headline=search_headline).filter(search=search_query).order_by("-rank")


# Q Search
#    def get_queryset(self):
#        query = self.request.GET.get("q")
#        return Message.objects.filter(
#            Q(name__icontains=query) | Q(quote__icontains=query)
#        )



# Single Field Search
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Message.objects.filter(quote__search=query)


# Multi Field Search
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Message.objects.annotate(search=SearchVector("name", "quote")).filter(
#             search=query
#         )


# Stemming and Ranking
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("name", "quote")
#         search_query = SearchQuery(query)
#         return (
#             Message.objects.annotate(
#                 search=search_vector, rank=SearchRank(search_vector, search_query)
#             )
#             .filter(search=search_query)
#             .order_by("-rank")
#         )


# Weights
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("name", weight="B") + SearchVector(
#             "quote", weight="A"
#         )
#         search_query = SearchQuery(query)
#         return (
#             Message.objects.annotate(rank=SearchRank(search_vector, search_query))
#             .filter(rank__gte=0.3)
#             .order_by("-rank")
#         )
