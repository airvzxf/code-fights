def newRoadSystem(road_register: list) -> bool:
    """
    Extract the routes and check if one of these are broken.

    :param road_register: Complete map (bi-dimensional array) with all the routes.
    :return: True if there is not any broken route.
    :rtype: bool
    """

    routes = mapping_the_sky(road_register)
    map_route_connected = []

    print("\n-------------------------------------------------------------------------------------------------\n")
    print("Mapping:   ", road_register)
    print("Routes:    ", routes)

    follow_the_rainbow(routes, map_route_connected)
    is_connected = not broken_routes(routes)

    print("")
    print("map_route_connected: ", map_route_connected)
    print("routes:              ", routes)
    print("")
    print("is_connected: ", is_connected)

    return is_connected


def broken_routes(routes: list) -> bool:
    """
    Check if the routes are broken; looking for an empty list.

    :param routes: List of the connected nodes.
    :return: True if the routes are broken otherwise false
    :rtype: bool
    """

    for node in routes:
        if routes[node]:
            return True

    return False


def mapping_the_sky(universe: list) -> dict:
    """
    Convert the boolean route map into a dictionary route map.
    It converts all the true values in a map, relating the bi-dimensional array with the nodes and connections.

    :param universe: The bi-dimensional array with Tru and False values which represent the connections between nodes.
    :return: Create a simple dictionary with all the routes.
    :rtype: dict
    """

    mapping_the_rainbow = {}
    total_nodes = len(universe)

    for node_index in range(total_nodes):
        total_connections = len(universe[node_index])
        mapping_the_rainbow[node_index] = []

        for connection_index in range(total_connections):

            if universe[node_index][connection_index]:
                mapping_the_rainbow[node_index].append(connection_index)

    return mapping_the_rainbow


def follow_the_rainbow(map_route: dict, map_route_connected: list):
    """
    Follow all the nodes and extract the connected routes from the map route.

    :param map_route: This dictionary contains all the routes.
    :param map_route_connected: After the deeply extraction this list contains all the connected routes.
    """

    for node_index in range(len(map_route)):
        following_deeply(map_route, node_index, node_index, True, map_route_connected)


def following_deeply(map_route, node, target_node, is_root, connected_nodes):
    for actual_node in map_route[node].copy():
        if actual_node == target_node:
            connected_nodes.append([node])
            array_index = map_route[node].index(actual_node)
            del map_route[node][array_index]
            return True
        else:

            if following_deeply(map_route, actual_node, target_node, False, connected_nodes):
                connected_nodes[-1].append(node)
                array_index = map_route[node].index(actual_node)
                del map_route[node][array_index]

                if is_root:
                    connected_nodes[-1].reverse()
                else:
                    return True

    return False


assert newRoadSystem(
    [
        [False, True, False, False],
        [False, False, True, False],
        [True, False, False, True],
        [False, False, True, False]
    ]
) is True

assert newRoadSystem(
    [
        [False, True, False, False, False, False, False],
        [True, False, False, False, False, False, False],
        [False, False, False, True, False, False, False],
        [False, False, True, False, False, False, False],
        [False, False, False, False, False, False, True],
        [False, False, False, False, True, False, False],
        [False, False, False, False, False, True, False]
    ]
) is True

assert newRoadSystem(
    [
        [False, True, False],
        [False, False, False],
        [True, False, False]
    ]
) is False

assert newRoadSystem(
    [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ]
) is True

assert newRoadSystem(
    [
        [False]
    ]
) is True

assert newRoadSystem(
    [
        [False, True, True, True, False],
        [True, False, True, True, True],
        [True, True, False, True, False],
        [True, True, True, False, True],
        [True, True, True, True, False]
    ]
) is False

assert newRoadSystem(
    [
        [False, True, True, True, True],
        [True, False, True, True, True],
        [True, True, False, True, True],
        [True, True, True, False, True],
        [True, True, True, True, False]
    ]
) is True

assert newRoadSystem(
    [
        [False, True, False, True, True],
        [False, False, False, False, True],
        [True, False, False, True, True],
        [True, True, True, False, False],
        [True, True, True, False, False]
    ]
) is False

assert newRoadSystem(
    [
        [False, True, True, False, True],
        [True, False, False, True, False],
        [False, True, False, True, False],
        [True, True, True, False, True],
        [True, True, False, False, False]
    ]
) is False

# assert newRoadSystem(
#     [
#         [False, True, False, True, True],
#         [True, False, True, True, True],
#         [False, False, False, False, True],
#         [False, False, True, False, True],
#         [True, False, True, True, False]
#     ]
# ) is False
#
# assert newRoadSystem(
#     [
#         [False, False, False, False, True, True, False, True, False, True],
#         [False, False, True, False, False, False, True, False, False, True],
#         [False, False, False, True, False, False, False, True, False, True],
#         [False, True, False, False, True, False, False, True, False, False],
#         [False, True, False, True, False, False, False, True, False, False],
#         [True, True, True, True, True, False, True, False, True, True],
#         [False, False, True, True, True, True, False, False, False, True],
#         [True, True, True, False, False, False, False, False, False, False],
#         [False, False, False, True, False, True, True, True, False, False],
#         [False, True, True, True, True, False, True, False, True, False]
#     ]
# ) is False
#
# assert newRoadSystem(
#     [
#         [False, False, False, False, True, True, True, True, True, True, False, True, True, True],
#         [True, False, True, True, False, True, True, True, True, False, False, True, False, False],
#         [False, False, False, True, False, False, True, True, False, True, False, True, True, False],
#         [True, True, False, False, True, True, False, False, False, True, True, True, False, True],
#         [False, True, True, True, False, True, True, True, False, False, True, False, True, False],
#         [True, True, False, True, True, False, True, False, True, True, True, True, True, True],
#         [True, False, True, True, False, True, False, False, False, False, True, True, True, True],
#         [False, True, False, True, True, False, True, False, True, True, True, True, False, False],
#         [True, True, False, False, False, True, True, True, False, False, True, True, True, True],
#         [True, False, True, False, False, True, False, True, True, False, True, False, True, True],
#         [True, True, True, True, True, True, False, True, True, True, False, True, False, False],
#         [True, True, False, False, True, True, False, False, True, True, True, False, True, True],
#         [True, True, False, False, True, True, True, True, True, False, True, False, False, False],
#         [False, False, True, True, True, True, False, False, True, True, True, False, False, False]
#     ]
# ) is True
