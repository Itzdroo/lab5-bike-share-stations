"""Manage an in-memory bike-share network and demonstrate its operations."""

import secrets
import sqlite3

CONNECTION = sqlite3.connect(":memory:")
CONNECTION.execute(
    "CREATE TABLE stations (id INTEGER PRIMARY KEY, name TEXT, "
    "capacity INTEGER, bikes INTEGER)"
)


def add_station(name, capacity, bikes, log=None):
    """Register a station and return its supplied or newly created name log."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Station name must be a non-empty string")
    if (
        not isinstance(capacity, int) or isinstance(capacity, bool)
        or not isinstance(bikes, int) or isinstance(bikes, bool)
    ):
        raise ValueError("Capacity and bikes must be integers")
    if not 0 <= bikes <= capacity:
        raise ValueError("Require 0 <= bikes <= capacity")
    CONNECTION.execute(
        "INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)",
        (name, capacity, bikes),
    )
    if log is None:
        log = []
    log.append(name)
    return log


def rent_bike(station_id):
    """Rent one bike, returning False for an empty or unknown station."""
    cursor = CONNECTION.execute(
        "UPDATE stations SET bikes = bikes - 1 WHERE id = ? AND bikes > 0",
        (station_id,),
    )
    return cursor.rowcount == 1


def unlock_pin():
    """Return a cryptographically generated four-digit unlock PIN."""
    return 1000 + secrets.randbelow(9000)


def full_stations():
    """Return the names of stations whose bikes equal their capacity."""
    stations = CONNECTION.execute(
        "SELECT name FROM stations WHERE bikes = capacity"
    ).fetchall()
    return [station[0] for station in stations]


def reset_station(station_id):
    """Empty a station; allow database errors to reach the caller."""
    CONNECTION.execute(
        "UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,)
    )


def has_bikes(station_id):
    """Return False for an unknown station or a missing/zero bike count."""
    row = CONNECTION.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()
    return row is not None and row[0] is not None and row[0] > 0


def main():
    """Run a short demonstration of station operations."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)
    print(rent_bike(2), rent_bike(9) is False)
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    try:
        main()
    finally:
        CONNECTION.close()
