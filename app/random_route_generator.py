import osmnx as ox
import networkx as nx
import random
import numpy as np
from rtree import index
import matplotlib.pyplot as plt

#CHECK IF WORKING BY: load in repl to check if it works - create a venv
#defining fuctions for each thing they are doing and export this file and import the functions

#current_location = street + city + zip_code from database

def route_generator(current_location):
    #convert current_location to lat and long using the geocode()
    location = ox.geocode(current_location)
    lat = location.latitude
    long = location.longitude

    # pick a random node from the nearby nodes (want three random nodes)
    node_selected = 0

    while node_selected <= 3:

        random_node = random.choice(nearby_nodes)

        # find the shortest path between the current location and the randomly selected node
        route = nx.shortest_path(G, lat, long, random_node, weight='length')

        # The round trip distance should be twice the length of the shortest path
        round_trip_distance = 2 * nx.shortest_path_length(G, lat, long, random_node, weight='length')
        
        # plot the route on the graph
        fig, ax = ox.plot_graph_route(G, route)

        #increment the node counter
        node_selected += 1

        #return the route 
        return route






###  FUNCTION 1: create a graph with the lat & lng of location ##


# convert miles to meters
mi = 4 #example input
distance = mi * 1,609.344     #the distance is based on weekly recommendation

# get the street network within a buffer of the current location
current_location = ("Seattle") #query into the model location field to get the current location (string) 
G = ox.graph_from_address(current_location, dist=distance, network_type='walk')
G_projected = ox.project_graph(G)
location = ox.geocode(current_location)

### FUNCTION 2: get three x and y coordinates as the nearest nodes for a specific location
# STILL NEED TO FIGURE OUT HOW TO RETURN ONLY NODES THAT ARE AT A SPECIFIC DISTANCE # 

#option 1:
def nearest_node(x, y):
    return list(idx.nearest((x, y, x, y), num_results=3))

idx = index.Index()
for n_id, n in G_projected.nodes(data=True):
    idx.insert(int(n_id), (n['x'], n['y'], n['x'], n['y']))

#option 2:
# find all the nodes within a certain distance from the current location
nearby_node_list = []
for i in range(3):
    nearby_nodes = ox.get_nearest_nodes(G, current_location, return_dist=True)
    #use a conditional to only return nodes within specific distance? 
    nearby_node_list.append(nearby_nodes)


### FUNCTION 3: draws a straight line to the paths in the graph ###

start = location 
nearby_node_list
#adds an edge between the starting location and the current 
#point in the for loop by calling the add_edge method on the G graph object.
for node in nearby_node_list:
    G.add_edge(start, node)

# function to draw the edges of the G graph on a plot. 
# The pos parameter is set to the x-coordinates of the nodes in the graph, 
# obtained using ox.get_node_attributes(G, 'x') 
# and the edge_color is set to blue and width of the lines is 2.
nx.draw_networkx_edges(G, pos=ox.get_node_attributes(G, 'x'), edge_color='b', width=2)
plt.show()


##may not be necessary 
def shortest_path_distance(G, source, target):
    path = nx.shortest_path(G, source=source, target=target)
    source = path[0]
    path = path[1:]
    target = path[0]

    path_length = 0
    while path:
        target = path[0]
        path = path[1:]
        path_length += G[source][target][0]['length']
        source = target
    return path_length    