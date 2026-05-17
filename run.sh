#!/bin/bash

echo ""
echo "================================================"
echo "   AI Student Doubt Solver - Quick Start"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8+ first"
    exit 1
fi

echo "[1/3] Checking dependencies..."
if ! pip show flask &> /dev/null; then
    echo "[2/3] Installing required packages..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
else
    echo "[2/3] Dependencies already installed"
fi

echo "[3/3] Starting application..."
echo ""
echo "================================================"
echo "   Server is starting..."
echo "   Open: http://localhost:5000"
echo "================================================"
echo ""

python3 Main.py
