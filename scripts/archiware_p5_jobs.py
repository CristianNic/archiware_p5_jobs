#!/usr/local/munki/python

import os
import sys
import subprocess
import collections
import json

def nsdchat_check():

    cmds = ['sh nsdchat_job_simulator.sh Job warning',
            'sh nsdchat_job_simulator.sh Job 12267 describe',
            'sh nsdchat_job_simulator.sh Job 12438 describe']

    out = []

    for cmd in cmds:
        proc = subprocess.Popen(cmd, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        out.append(output)
        print(output)
        # >> 12267 12284 12294 12438 12421 12413
        # >> Sync Plan: Sync Plan 1
        # >> Sync Plan: Sync Plan 1

    print(out)
        # >> ['12267 12284 12294 12438 12421 12413', 'Sync Plan: Sync Plan 1', 'Sync Plan: Sync Plan 1']


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
    # result = two_dicts()
    result = nsdchat_check()

    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cachedir, 'archiware_p5_jobs.json'), 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    main()
