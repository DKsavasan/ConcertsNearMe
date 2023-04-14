import ticketpy

tm_client = ticketpy.ApiClient('1m3jpoAZ65vufnoIEnQ47V5DjEoUGggG')

pages = tm_client.events.find(
    classification_name=
    state_code='MA',
    start_date_time='2023-05-19T00:00:00Z',
    end_date_time='2023-05-21T20:00:00Z'
)

for page in pages:
    for event in page:
        print(event)
        