import json
from django.core.management.base import BaseCommand
from JanataApp.models import StockMarketData



# For JSON Model
class Command(BaseCommand):
    help = 'Load data from JSON file to SQL Server'

    def handle(self, *args, **kwargs):
        with open('taskfiles/stock_market_data.json', 'r') as file:
            data = json.load(file)
            for entry in data:
                StockMarketData.objects.create(
                    date=entry['date'],
                    trade_code=entry['trade_code'],
                    high=float(entry['high'].replace(',', '')),  # Remove commas before converting to float
                    low=float(entry['low'].replace(',', '')),  # Remove commas before converting to float
                    open=float(entry['open'].replace(',', '')),  # Remove commas before converting to float
                    close=float(entry['close'].replace(',', '')),  # Remove commas before converting to float
                    volume=int(entry['volume'].replace(',', ''))
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))