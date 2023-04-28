import ticketpy

tm_client = ticketpy.ApiClient('1m3jpoAZ65vufnoIEnQ47V5DjEoUGggG')

pages = tm_client.events.find(
    classification_name="Drama", 
    state_code='MA',
    start_date_time='2023-01-19T00:00:00Z',
    end_date_time='2023-07-25T00:00:00Z'
)

event_list = []
for page in pages:
    for event in page:
        event_dict = vars(event)
        event_list.append(event_dict)

print(event_list)
