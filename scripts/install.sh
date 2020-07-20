#!/bin/bash

# archiware_p5_jobs controller
CTL="${BASEURL}index.php?/module/archiware_p5_jobs/"

# Get the scripts in the proper directories
"${CURL[@]}" "${CTL}get_script/archiware_p5_jobs.py" -o "${MUNKIPATH}preflight.d/archiware_p5_jobs.py"

# Check exit status of curl
if [ $? = 0 ]; then
	# Make executable
	chmod a+x "${MUNKIPATH}preflight.d/archiware_p5_jobs.py"

	# Set preference to include this file in the preflight check
	setreportpref "archiware_p5_jobs" "${CACHEPATH}archiware_p5_jobs.json"

else
	echo "Failed to download all required components!"
	rm -f "${MUNKIPATH}preflight.d/archiware_p5_jobs.py"

	# Signal that we had an error
	ERR=1
fi
