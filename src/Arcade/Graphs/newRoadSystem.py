def newRoadSystem(road_register: list) -> bool:
    """
    Extract the routes and check if is one of this is broken.

    :param road_register: Complete map (bi-dimensional array) with all the routes.
    :return: True if there is not any broken route.
    :rtype: bool
    """

    routes = mapping_the_sky(road_register)

    print("Mapping: ", road_register)
    print("routes: ", routes)

    if len(routes) != len(road_register):
        print("Broken! The size is not the same.")
        return False

    is_broken = follow_the_rainbow(routes)
    print("is_broken: ", is_broken)

    print("\n")

    return is_broken


def mapping_the_sky(universe: list) -> dict:
    """
    Convert the list map into a route dictionary.
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


def follow_the_rainbow(map_route: dict) -> bool:
    """
    Follow every route trying to validate that every route is not broken.

    :param map_route: This dictionary contain all the routes.
    :return: True if there's not broken routes.
    :rtype: bool
    """

    for node_index in range(len(map_route)):
        if not following_deeply(map_route, node_index, node_index, 0):
            return False

    print(map_route)
    return True


def following_deeply(map_route, actual_index, match_index, counter):
    counter += 1

    for index in map_route[actual_index]:
        if index == match_index:
            array_index = map_route[actual_index].index(index)
            del map_route[actual_index][array_index]
            return True
        else:
            if counter < len(map_route):
                if following_deeply(map_route, index, match_index, counter):
                    array_index = map_route[actual_index].index(index)
                    del map_route[actual_index][array_index]
                    return True

    if not map_route[actual_index] and counter == 1:
        return True


# assert newRoadSystem(
#     [
#         [False, True, False, False],
#         [False, False, True, False],
#         [True, False, False, True],
#         [False, False, True, False]
#     ]
# ) is True
#
# assert newRoadSystem(
#     [
#         [False, True, False, False, False, False, False],
#         [True, False, False, False, False, False, False],
#         [False, False, False, True, False, False, False],
#         [False, False, True, False, False, False, False],
#         [False, False, False, False, False, False, True],
#         [False, False, False, False, True, False, False],
#         [False, False, False, False, False, True, False]
#     ]
# ) is True
#
# assert newRoadSystem(
#     [
#         [False, True, False],
#         [False, False, False],
#         [True, False, False]
#     ]
# ) is False
#
# assert newRoadSystem(
#     [
#         [False, False, False, False],
#         [False, False, False, False],
#         [False, False, False, False],
#         [False, False, False, False]
#     ]
# ) is True
#
# assert newRoadSystem(
#     [
#         [False]
#     ]
# ) is True

assert newRoadSystem(
    [
        [False, True, True, True, False],
        [True, False, True, True, True],
        [True, True, False, True, False],
        [True, True, True, False, True],
        [True, True, True, True, False]
    ]
) is False

# assert newRoadSystem(
#     [
#         [False, True, True, True, True],
#         [True, False, True, True, True],
#         [True, True, False, True, True],
#         [True, True, True, False, True],
#         [True, True, True, True, False]
#     ]
# ) is True
#
# assert newRoadSystem(
#     [
#         [False, True, False, True, True],
#         [False, False, False, False, True],
#         [True, False, False, True, True],
#         [True, True, True, False, False],
#         [True, True, True, False, False]
#     ]
# ) is False
#
# assert newRoadSystem(
#     [
#         [False, True, True, False, True],
#         [True, False, False, True, False],
#         [False, True, False, True, False],
#         [True, True, True, False, True],
#         [True, True, False, False, False]
#     ]
# ) is False
#
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
