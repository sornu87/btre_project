from django.shortcuts import get_object_or_404, render
from listings.models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listing_list = paginator.get_page(page)
    context = {
        'listings': paged_listing_list,
    }

    return render (request,'listings/listings.html',context)

# Vista detalhada de realstates
def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        'listing':listing
    }
    return render (request,'listings/listing.html',context)

def search(request):
    return render (request,'listings/search.html')
