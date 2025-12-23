#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def merge_profiles(*profiles, **defaults):
    result = {}

    for profile in profiles:
        for key, value in profile.items():
            result[key] = value

    for key, value in defaults.items():
        if key not in result:
            result[key] = value

    return result

if __name__ == "__main__":
    merged = merge_profiles(
        {"name": "Alice", "city": "Paris"},
        {"age": 25},
        country="France"
    )
    print("Тест 1:")
    print(merged)

    merged2 = merge_profiles(
        {"name": "Bob", "age": 30},
        {"name": "Robert", "city": "London"},
        {"age": 35},
        country="UK",
        city="Manchester"
    )
    print("\nТест 2 (проверка приоритетов):")
    print(merged2)

    merged3 = merge_profiles(
        name="John",
        age=40,
        city="New York"
    )
    print("\nТест 3:")
    print(merged3)