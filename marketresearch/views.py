# views.py (for Django)
from django.shortcuts import render
from marketresearch.scraper import get_market_data  # Import the scraper function

def generate_report(request):
    if request.method == 'POST':
        url = request.POST.get('url')  # Get URL from form input
        market_data = get_market_data(url)
        
        if market_data:
            # Render template and display market data
            return render(request, 'report.html', {'market_data': market_data})
        else:
            return render(request, 'error.html', {'error': 'Failed to retrieve data'})

    return render(request, 'index.html')
