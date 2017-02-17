#!/usr/bin/env bash

# Convert pdf into png in batch

for filename in *.pdf ; do
	sips -s format png --out "${filename%%.*}.png" "$filename"
done