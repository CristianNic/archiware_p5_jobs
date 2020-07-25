#!/usr/local/munki/python

import os
import sys
import subprocess
import collections
import json

def two_dicts():
    out = []
    job1 = {"job_number" : "12685 \n Success"}
    job2 = {"job_number" : "12267 \n Pass"}
    job3 = {"job_number" : "12235" + '\n' + "Success"}
    out.append(job1)
    out.append(job2)
    out.append(job3)
    return out

def main():

    """Main"""
    # Check if Archiware P5 Jobs is installed
    if  not os.path.isfile('/usr/local/aw/bin/nsdchat'):
        print ("ERROR: Archiware P5 is not installed")
        exit(0)

    # Get information about Archiware P5 Jobs
    result = dict()
    result = two_dicts()

    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cachedir, 'archiware_p5_jobs.json'), 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    main()
