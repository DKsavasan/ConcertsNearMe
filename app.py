from flask import Flask, render_template, request, redirect
import ticketpy
import json
import geopy.distance


app = Flask(__name__)

tm_client = ticketpy.ApiClient('1m3jpoAZ65vufnoIEnQ47V5DjEoUGggG')

# This tells Flask to serve the static files from the 'static' folder
app.static_folder = 'static'

@app.route('/')
def auth():
    return render_template('auth.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/process-form', methods=['POST'])
def process_form():
    print("Processing form...")
    genre = request.form['genre']
    print("Genre:", genre)
    date_range = request.form['date_range']
    print("Date range:", date_range)
    max_price = request.form['max_price']
    print("Max price:", max_price)
    max_distance = request.form['max_distance']
    print("Max distance:", max_distance)
    state_code = request.form['state_code']
    print("State Code:", state_code)
    
    
    # do something with the variables here, like save them to a database or process them in some way
    
    start = date_range.split(" - ")[0] + "T00:00:00Z"
    finish = date_range.split(" - ")[1] + "T23:59:59Z"
    
    
    
    pages = tm_client.events.find(
    classification_name=genre,
    state_code= state_code,
    start_date_time=start,
    end_date_time=finish)
    

    event_list = []
    for page in pages:
        for event in page:
            event_dict = vars(event)
            event_list.append(event_dict)
            # print(event)
            
    # print("event_list", event_list[0])
    # print("type", type(event_list[0]))
    # print("keys", event_list[0]["json"]["_embedded"]["venues"][0]["location"])
    
    #and float(max_distance)) >= geopy.distance.geodesic(coords_1, coords_2).km
    
    events_data = []
    for i in range(len(event_list)):
        coords_1 = (52.2296756, 21.0122287)
        coords_2 = (float(event_list[i]["json"]["_embedded"]["venues"][0]["location"]["latitude"]), float(event_list[i]["json"]["_embedded"]["venues"][0]["location"]["longitude"]))
        if float(max_price) >= float(event_list[i]["price_ranges"][0]["max"]):
            events_data.append({})
            events_data[i]["name"] = event_list[i]["name"]
            events_data[i]["status"] = event_list[i]["status"]
            events_data[i]["start_date"] = event_list[i]["local_start_date"]
            events_data[i]["start_time"] = event_list[i]["local_start_time"]
            events_data[i]["min_price"] = event_list[i]["price_ranges"][0]["min"]
            events_data[i]["max_price"] = event_list[i]["price_ranges"][0]["max"]
            events_data[i]["longitude"] = event_list[i]["json"]["_embedded"]["venues"][0]["location"]["longitude"]
            events_data[i]["latitude"] = event_list[i]["json"]["_embedded"]["venues"][0]["location"]["latitude"]
        
        
    print(events_data)

    return render_template('index.html', data=events_data)




if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)

