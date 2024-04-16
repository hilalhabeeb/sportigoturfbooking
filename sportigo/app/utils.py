

from geopy.distance import geodesic

def find_turfs_sorted_by_distance(user_latitude, user_longitude, turf_locations):
    """
    Finds all turfs sorted by their distance from the given user coordinates.

    Args:
    - user_latitude (float): Latitude of the user's location.
    - user_longitude (float): Longitude of the user's location.
    - turf_locations (list): List of tuples containing turf names, latitude, and longitude.

    Returns:
    - sorted_turfs (list): List of turfs sorted by their distance from the user.
    """
    turfs_with_distance = []

    for venue, turf_latitude, turf_longitude in turf_locations:
        turf_location = (turf_latitude, turf_longitude)
        user_location = (user_latitude, user_longitude)
        distance = geodesic(user_location, turf_location).kilometers
        turfs_with_distance.append((venue, turf_location, distance))

    # Sort turfs by distance
    sorted_turfs = sorted(turfs_with_distance, key=lambda x: x[2])

    return sorted_turfs
