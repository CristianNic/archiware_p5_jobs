#!/bin/bash

# Remove archiware_jobs script
rm -f "${MUNKIPATH}preflight.d/archiware_p5_jobs.py"

# Remove archiware_jobs.txt file
rm -f "${MUNKIPATH}preflight.d/cache/archiware_p5_jobs.json"
