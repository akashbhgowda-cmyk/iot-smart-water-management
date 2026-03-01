
# IoT-Based Smart Water Management System

## Overview
A full-stack IoT-based monitoring system designed to track real-time water usage in apartments.

## Features
- Real-time water usage data collection
- MySQL database integration
- REST API using Flask
- React-based dashboard for analytics
- Automated billing calculation

## Tech Stack
Backend:
- Python (Flask)
- MySQL

Frontend:
- React.js

## Database Table Structure

CREATE TABLE water_usage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    apartment_no INT,
    usage_liters FLOAT,
    timestamp DATETIME
);

## How to Run

Backend:
pip install -r requirements.txt
python backend/app.py

Frontend:
npm install
npm start
