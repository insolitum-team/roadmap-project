#!/bin/bash

# Run pytest with coverage and store the result in a temporary file
pytest --cov > coverage_report.txt

# Extract the coverage percentage from the report
coverage=$(awk '/TOTAL/ {print $NF}' coverage_report.txt)

# Check if coverage is below 90%
if (( $(awk 'BEGIN {print ("'$coverage'" < 80)}') )); then
  echo "Error: Test coverage is below 80% (${coverage})"
  exit 1
else
  echo "Test coverage is acceptable (${coverage})"
  exit 0
fi