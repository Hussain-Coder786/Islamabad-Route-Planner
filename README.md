# Islamabad-Route-Planner
This project calculates the shortest distance between various notable locations in Islamabad using the Haversine formula and visualizes the map with markers for these locations.

Table of Contents

Overview
Features
Installation
Usage
Locations
Visualization
License


Overview


Islamabad Route Planner is a Python project that computes the shortest distance between well-known landmarks in Islamabad. It uses the Haversine formula to determine distances between geographic coordinates and plots these locations on a map using Matplotlib.

Features

Calculate the shortest distance between two locations in Islamabad.
Visualize the locations on a map.
Generate a link to explore the map on OpenStreetMap.

Installation

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/IslamabadRoutePlanner.git
cd IslamabadRoutePlanner
Install the required dependencies:
bash
Copy code
pip install matplotlib
Usage
Run the script:
bash
Copy code
python main.py
Follow the prompts to enter the source and destination locations.
The script will output the shortest distance between the two locations and open the corresponding map in your web browser.
Locations
The project includes predefined coordinates for several key locations in Islamabad:

Faisal Mosque
Rawal Lake
Centaurus Mall
Pakistan Monument
Daman-e-Koh
Lok Virsa Museum
Saidpur Village
Pir Sohawa
Visualization
The project uses Matplotlib to plot these locations on a map of Islamabad. Each location is marked with a blue dot, and annotations are provided for better identification.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Example Code
Here's a brief overview of the core components in the project:

python
Copy code
import math
import webbrowser
import matplotlib.pyplot as plt

class Coordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

class Map:
    def __init__(self):
        pass

    def get_coordinates(self, location_name):
        coordinates = {
            "Faisal Mosque": (33.7294, 73.0396),
            "Rawal Lake": (33.6720, 73.0379),
            "Centaurus Mall": (33.6935, 73.0510),
            "Pakistan Monument": (33.6844, 73.0531),
            "Daman-e-Koh": (33.7219, 73.0497),
            "Lok Virsa Museum": (33.6846, 73.0521),
            "Saidpur Village": (33.7261, 73.0667),
            "Pir Sohawa": (33.7396, 73.0921),
        }
        lat, lon = coordinates.get(location_name)
        return Coordinate(lat, lon)

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, source, destination, weight):
        if source not in self.edges:
            self.edges[source] = {}
        if destination not in self.edges:
            self.edges[destination] = {}
        self.edges[source][destination] = weight
        self.edges[destination][source] = weight

    def haversine_distance(self, coord1, coord2):
        lat1, lon1 = coord1.latitude, coord1.longitude
        lat2, lon2 = coord2.latitude, coord2.longitude
        R = 6371.0
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    def shortest_path(self, source, destination):
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

    def get_osm_link(self, locations):
        base_url = "https://www.openstreetmap.org/?mlat={}&mlon={}&zoom=14"
        central_location = locations["Faisal Mosque"]
        link = base_url.format(central_location[0], central_location[1])
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
    osm_link = shortest_distance_calculator.get_osm_link(locations)
    print(f"Explore the map of Islamabad here: {osm_link}")
    webbrowser.open(osm_link)
    def plot_islamabad_map(locations):
        lats = [coord[0] for coord in locations.values()]
        lons = [coord[1] for coord in locations.values()]
        plt.plot(lons, lats, 'bo')
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.title("Islamabad Map")
        plt.xlim(min(lons) - 0.01, max(lons) + 0.01)
        plt.ylim(min(lats) - 0.01, max(lats) + 0.01)
        for location, (lat, lon) in locations.items():
            if location == "Pakistan Monument":
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(10,0), ha='left', fontsize=8)
            elif location == "Lok Virsa Museum":
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(-10,0), ha='right', fontsize=8)
            else:
                plt.annotate(location, (lon, lat), textcoords="offset points", xytext=(0,10), ha='center')
        plt.show()
    plot_islamabad_map(locations)
