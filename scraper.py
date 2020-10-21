import datetime
from pytz import timezone
import pandas as pd
import csv

csv_file = 'AlbertaEnergy/data.csv'
ab_power_address_base = 'http://ets.aeso.ca/ets_web/ip/Market/Reports/'
report_type = 'ActualForecastWMRQHReportServlet'

# Generate timestamp
calgary = timezone('Canada/Mountain')
now = datetime.datetime.now(calgary)
#myTest = datetime.datetime(2019,1,1)

START_YEAR, START_MONTH, START_DAY = 2010, 1, 1

END_YEAR, END_MONTH, END_DAY = now.year, now.month, now.day


for year in range(START_YEAR, END_YEAR+1):
    for month in range(1,12+1):
        if year == END_YEAR and month == END_MONTH + 1:
            break
        begin_date_string = "{}01{}".format(f"{month:02d}",year)

        end_date_string = "{}01{}".format(f"{month+1:02d}",year)

        url = ab_power_address_base + report_type + "?beginDate=" + begin_date_string + "&endDate=" + end_date_string
        #start_time = datetime.datetime(year = START_YEAR,month = START_MONTH,day = START_DAY)
        url_data = pd.read_html(io = url)[1]

        combined_csv = pd.concat([url_data])

        #print(url_data)
combined_csv.to_csv('myData.csv')