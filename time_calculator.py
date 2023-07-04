#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 17:43:17 2023

@author: Jeremy
"""


def add_time(start_time, duration, start_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Convert start_hour to 24-hour format
    if period == "PM":
        start_hour += 12

    # Calculate the total minutes
    start_total_minutes = start_hour * 60 + start_minute
    duration_total_minutes = duration_hour * 60 + duration_minute
    end_total_minutes = start_total_minutes + duration_total_minutes

    # Calculate the number of days later
    num_days_later = end_total_minutes // (24 * 60)
    remaining_minutes = end_total_minutes % (24 * 60)

    # Calculate the hour and minute for the final time
    end_hour = remaining_minutes // 60
    end_minute = remaining_minutes % 60

    # Determine the period (AM or PM)
    if end_hour < 12:
        period = "AM"
    else:
        period = "PM"
        end_hour -= 12

    # Convert the hour to 12-hour format
    if end_hour == 0:
        end_hour = 12

    # Create the final time string
    new_time = f"{end_hour}:{end_minute:02} {period}"

    # Add the day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        start_day_index = days_of_week.index(start_day)
        end_day_index = (start_day_index + num_days_later) % 7
        new_time += f", {days_of_week[end_day_index]}"

    # Add "next day" or "n days later" if applicable
    if num_days_later == 1:
        new_time += " (next day)"
    elif num_days_later > 1:
        new_time += f" ({num_days_later} days later)"

   



    return new_time