"""Behavior checks for the cleaned bike-share assignment."""

import sqlite3
import unittest
from unittest import mock

import bike_share_stations as app


class StationTests(unittest.TestCase):
    """Use an isolated station table for every test."""

    def setUp(self):
        app.CONNECTION.execute("DELETE FROM stations")

    def test_quoted_name_is_data(self):
        name = "O'Brien'); DROP TABLE stations; --"
        app.add_station(name, 5, 5)
        self.assertEqual(app.full_stations(), [name])
        app.add_station("Still works", 2, 1)

    def test_default_logs_are_independent(self):
        first = app.add_station("One", 2, 1)
        second = app.add_station("Two", 2, 1)
        self.assertEqual(first, ["One"])
        self.assertEqual(second, ["Two"])
        self.assertIsNot(first, second)

    def test_explicit_log_is_preserved(self):
        log = ["Previous"]
        self.assertIs(app.add_station("New", 2, 1, log), log)
        self.assertEqual(log, ["Previous", "New"])

    def test_rent_decrements_and_stops_at_zero(self):
        app.add_station("One", 2, 1)
        station_id = app.CONNECTION.execute(
            "SELECT id FROM stations"
        ).fetchone()[0]
        self.assertTrue(app.rent_bike(station_id))
        self.assertFalse(app.rent_bike(station_id))
        self.assertFalse(app.has_bikes(station_id))

    def test_unknown_station_is_safe(self):
        self.assertFalse(app.rent_bike(-1))
        self.assertFalse(app.has_bikes(-1))
        app.reset_station(-1)

    def test_full_stations(self):
        app.add_station("Full", 3, 3)
        app.add_station("Partial", 3, 2)
        self.assertEqual(app.full_stations(), ["Full"])

    def test_reset_empties_station(self):
        app.add_station("One", 2, 2)
        station_id = app.CONNECTION.execute(
            "SELECT id FROM stations"
        ).fetchone()[0]
        app.reset_station(station_id)
        self.assertFalse(app.has_bikes(station_id))
        self.assertEqual(app.full_stations(), [])

    def test_null_bike_count_is_safe(self):
        cursor = app.CONNECTION.execute(
            "INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)",
            ("Missing count", 3, None),
        )
        self.assertFalse(app.has_bikes(cursor.lastrowid))

    def test_invalid_counts_are_rejected(self):
        for capacity, bikes in [(2, 3), (-1, 0), (2, -1), (2, 1.5),
                                (True, 1), (2, False)]:
            with self.subTest(capacity=capacity, bikes=bikes):
                with self.assertRaises(ValueError):
                    app.add_station("Invalid", capacity, bikes)

    def test_empty_names_are_rejected(self):
        for name in ["", "  ", None]:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    app.add_station(name, 2, 1)

    def test_pin_boundaries(self):
        with mock.patch.object(app.secrets, "randbelow", return_value=0):
            self.assertEqual(app.unlock_pin(), 1000)
        with mock.patch.object(app.secrets, "randbelow", return_value=8999):
            self.assertEqual(app.unlock_pin(), 9999)

    def test_generated_pins_are_four_digits(self):
        for _ in range(100):
            self.assertIn(app.unlock_pin(), range(1000, 10000))

    def test_database_errors_are_not_swallowed(self):
        with mock.patch.object(app, "CONNECTION") as database:
            database.execute.side_effect = sqlite3.OperationalError("test")
            with self.assertRaises(sqlite3.OperationalError):
                app.reset_station(1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
