CREATE_ROUTES_TABLE = 'CREATE TABLE mbta_routes(id serial PRIMARY KEY, route_id text, agency_id text, route_short_name text, route_long_name text, route_desc text, route_fare_class text, route_type text, route_url text, route_color text, route_text_color text, route_sort_order text, line_id text, listed_route text, network_id text);'
CREATE_TRIPS_TABLE = 'CREATE TABLE mbta_trips(id serial PRIMARY KEY, route_id text, service_id text, trip_id text, trip_headsign text, trip_short_name text, direction_id text, block_id text, shape_id text, wheelchair_acessible text, trip_route_type text, route_pattern_id text, bikes_allowed text);'
CREATE_STOP_TIMES_TABLE = 'CREATE TABLE mbta_stop_times(id serial PRIMARY KEY, trip_id text, arrival_time text, departure_time text, stop_id text, stop_sequence text, stop_headsign text, pickup_type text, drop_off_type text, timepoint text, checkpoint_id text, continuous_pickup text, continuous_drop_off text);'
CREATE_STOPS_TABLE = 'CREATE TABLE mbta_stops(id serial PRIMARY KEY, stop_id text, stop_code text, stop_name text, stop_desc text, platform_code text, platform_name text, stop_lat text, stop_lon text, zone_id text, stop_address text, stop_url text, level_id text, location_type text, parent_station text, wheelchair_boarding text, municipality text, on_street text, at_street text, vehicle_type text);'

INSERT_ROUTES_STATEMENT = 'INSERT into mbta_routes(route_id, agency_id, route_short_name, route_long_name, route_desc, route_fare_class, route_type, route_url, route_color, route_text_color, route_sort_order, line_id, listed_route, network_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
INSERT_TRIPS_STATEMENT = 'INSERT into mbta_trips(route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, block_id, shape_id, wheelchair_acessible, trip_route_type, route_pattern_id, bikes_allowed) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
INSERT_STOP_TIMES_STATEMENT = 'INSERT into mbta_stop_times(trip_id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, drop_off_type, timepoint, checkpoint_id, continuous_pickup, continuous_drop_off) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
INSERT_STOPS_STATEMENT = 'INSERT into mbta_stops(stop_id, stop_code, stop_name, stop_desc, platform_code, platform_name, stop_lat, stop_lon, zone_id, stop_address, stop_url, level_id, location_type, parent_station, wheelchair_boarding, municipality, on_street, at_street, vehicle_type) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'

FILES_DICT = {
    # 'routes': {
    #     'file': 'routes.txt',
    #     'create_table': CREATE_ROUTES_TABLE,
    #     'drop_table': 'DROP TABLE IF EXISTS mbta_routes;',
    #     'insert_command': INSERT_ROUTES_STATEMENT
    # },
    # 'trips': {
    #     'file': 'trips.txt',
    #     'create_table': CREATE_TRIPS_TABLE,
    #     'drop_table': 'DROP TABLE IF EXISTS mbta_trips;',
    #     'insert_command': INSERT_TRIPS_STATEMENT 
    # },
    # 'stop_times': {
    #     'file': 'stop_times.txt',
    #     'create_table': CREATE_STOP_TIMES_TABLE,
    #     'drop_table': 'DROP TABLE IF EXISTS mbta_stop_times',
    #     'insert_command': INSERT_STOP_TIMES_STATEMENT
    # },
    'stops': {
        'file': 'stops.txt',
        'create_table': CREATE_STOPS_TABLE,
        'drop_table': 'DROP TABLE IF EXISTS mbta_stops',
        'insert_command': INSERT_STOPS_STATEMENT
    }
}
