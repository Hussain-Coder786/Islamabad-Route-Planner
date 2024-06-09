import math
import webbrowser
from typing import Dict
import math
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Map:
    def __init__(self):
        # Initialize any map-related data or APIs here
        pass
    
    def get_coordinates(self, location_name):
        # For demonstration purposes, let's assume some hardcoded coordinates for known locations
        coordinates = {
            "Faisal Mosque": (33.7294, 73.0396),
            "Rawal Lake": (33.6720, 73.0379),
            "Centaurus Mall": (33.6935, 73.0510),
            "Pakistan Monument": (33.6844, 73.0531),
            "Daman-e-Koh": (33.7219, 73.0497),
            "Lok Virsa Museum": (33.6846, 73.0521),
            "Saidpur Village": (33.7261, 73.0667),
            "Pir Sohawa": (33.7396, 73.0921),
            
            # Add more coordinates for other locations as needed
        }
        lat, lon = coordinates.get(location_name)
        return Coordinate(lat, lon)

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_edge(self, source, destination, weight):
        # Add an edge between two coordinates with a certain weight (distance)
        if source not in self.edges:
            self.edges[source] = {}
        if destination not in self.edges:
            self.edges[destination] = {}
        self.edges[source][destination] = weight
        self.edges[destination][source] = weight
    
    def haversine_distance(self, coord1, coord2):
        # Calculate the Haversine distance between two coordinates
        lat1, lon1 = coord1.latitude, coord1.longitude
        lat2, lon2 = coord2.latitude, coord2.longitude

        # Radius of the Earth in kilometers
        R = 6371.0 

        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Haversine formula
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance
    
    def shortest_path(self, source, destination):
        # Calculate the Haversine distance between source and destination
        distance = self.haversine_distance(source, destination)
        return distance

class ShortestDistanceCalculator:
    def __init__(self):
        self.map = Map()
        self.graph = Graph()

    def calculate_shortest_distance(self, source_name, destination_name):
        source = self.map.get_coordinates(source_name)
        destination = self.map.get_coordinates(destination_name)
        shortest_path = self.graph.shortest_path(source, destination)
        return shortest_path
    def get_osm_link(self, source_name, destination_name, locations):
        base_url = "https://www.openstreetmap.org/?mlat={}&mlon={}&zoom=14"
        source_coords = locations[source_name]
        destination_coords = locations[destination_name]
        link = base_url.format(source_coords[0], source_coords[1])
        
        # Add markers for source and destination
        link += f"&mlat={source_coords[0]}&mlon={source_coords[1]}&marker"
        link += f"&mlat={destination_coords[0]}&mlon={destination_coords[1]}&marker"

        # Add markers for other locations
        for location_name, location_coords in locations.items():
            # Skip adding markers for source and destination again
            if location_name != source_name and location_name != destination_name:
                link += f"&mlat={location_coords[0]}&mlon={location_coords[1]}&marker"
            link += f"&mlat={location_coords[0]}&mlon={location_coords[1]}&marker"
    
        return link


if __name__ == "__main__":
    shortest_distance_calculator = ShortestDistanceCalculator()
    source_name = input("Enter the source location: ")
    destination_name = input("Enter the destination location: ")
    shortest_distance = shortest_distance_calculator.calculate_shortest_distance(source_name, destination_name)
    print(f"The shortest distance between {source_name} and {destination_name} is {shortest_distance:.2f} km.")

    locations = {
        "Faisal Mosque": (33.7294, 73.0396),
        "Rawal Lake": (33.6720, 73.0379),
        "Centaurus Mall": (33.6935, 73.0510),
        "Pakistan Monument": (33.6844, 73.0531),
        "Daman-e-Koh": (33.7219, 73.0497),
        "Lok Virsa Museum": (33.6846, 73.0521),
        "Saidpur Village": (33.7261, 73.0667),
        "Pir Sohawa": (33.7396, 73.0921),
    }
    
    osm_link = shortest_distance_calculator.get_osm_link(source_name, destination_name, locations)
    print(f"Explore the map of Islamabad here: {osm_link}")
    webbrowser.open(osm_link)




    # Plot the map
    def plot_islamabad_map(locations):
        # Extract latitude and longitude coordinates
        lats = [coord[0] for coord in locations.values()]
        lons = [coord[1] for coord in locations.values()]

        # Plot the locations on the map
        plt.plot(lons, lats, 'bo')  # Blue dots for locations
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Islamabad Map")

        # Automatically adjust axes limits to fit all locations
        plt.xlim(min(lons) - 0.01, max(lons) + 0.01)
        plt.ylim(min(lats) - 0.01, max(lats) + 0.01)

        # Annotate each location
        for location, (lat, lon) in locations.items():
            if location == "Pakistan Monument":
                # Position "Pakistan Monument" annotation to the right of the point
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(10,0), ha='left', fontsize=8)
            elif location == "Lok Virsa Museum":
                # Position "Lok Virsa Museum" annotation to the left of the point but closer
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(-10,0), ha='right', fontsize=8)
            else:
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(0,10), ha='center')

        plt.show()

    plot_islamabad_map(locations)
