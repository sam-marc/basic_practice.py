#!/bin/bash

# Check if the file exists
if [ ! -f "data.txt" ]; then
    echo "Error: File data.txt not found."
    exit 1
fi

# Calculate the sum of values in the second column
sum=$(awk -F',' '{sum+=$2} END {print sum}' data.txt)

# Find the maximum value in the third column
max=$(awk -F',' '{if ($3 > max) max=$3} END {print max}' data.txt)

# Determine the average value in the fourth column
average=$(awk -F',' '{sum+=$4; count++} END {print sum/count}' data.txt)

# Display the results
echo "Sum of values in the second column: $sum"
echo "Maximum value in the third column: $max"
echo "Average value in the fourth column: $average"
