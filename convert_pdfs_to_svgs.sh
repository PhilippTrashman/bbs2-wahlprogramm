#!/bin/bash

# Get the directory where the script is located
script_dir=$(dirname "$(realpath "$0")")

# Directory containing the PDF files, relative to the script's location
input_dir="$script_dir/assets/images/plakate"

# Loop through all PDF files in the directory
for pdf_file in "$input_dir"/*.pdf; do
  # Check if the file exists and is readable
  if [ ! -r "$pdf_file" ]; then
    echo "Cannot read $pdf_file"
    continue
  fi

  # Get the base name of the file (without extension)
  base_name=$(basename "$pdf_file" .pdf)
  
  # Define the output SVG file path
  svg_file="$input_dir/$base_name.svg"
  
  # Convert the PDF to SVG using pdf2svg
  if pdf2svg "$pdf_file" "$svg_file"; then
    echo "Converted $pdf_file to $svg_file"
  else
    echo "Failed to convert $pdf_file"
  fi
done