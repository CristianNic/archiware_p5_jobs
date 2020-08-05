#!/usr/local/munki/python

import os
import sys
import subprocess
import collections
import json

def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]
  
def nsdchat_job_check():

    cmd = ['sh nsdchat_job_simulator.sh Job 2_warnings'] # cmd requires full .sh file path name
    out = []
    proc = subprocess.Popen(cmd, text=True, shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, err = proc.communicate()
    out.append(output)
    out = output.split(' ')
    
    print(out)

    # create new cmds list from output. for each add path + descibe or xmlticket
    cmds = []

    for i in out:
        describe = 'sh nsdchat_job_simulator.sh Job ' + i + ' describe'  # >> 'sh nsdchat_job_simulator.sh Job 12267 descride'
        xmlpath  = 'sh nsdchat_job_simulator.sh Job ' + i + ' xmlticket'  # >> 'sh nsdchat_job_simulator.sh Job 12267 xmlpath'
        cmds.append(describe)
        cmds.append(xmlpath)
    print(cmds) # >> ['sh nsdchat_job_simulator.sh Job 12267 descride', 'sh nsdchat_job_simulator.sh Job 12267 xmlpath',
                #    'sh nsdchat_job_simulator.sh Job 12421 descride', 'sh nsdchat_job_simulator.sh Job 12421 xmlpath']

    # run the new list of commands
    for cmd in cmds:
        proc = subprocess.Popen(cmd, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        print(output) # >> Sync Plan: Sync Plan 1
                      # >> <jobreport>
                      # >>      <description>Sync Plan: Sync Plan 1</description>
                      # >>      <startdate>15.05.2016</startdate>
                      # >>      <enddate>15.05.2016</enddate>
                      # >>      <starttime>00:00:00</starttime>
                      # >> ...
                      # >> Sync Plan: Sync Plan 2
                      # >>      <jobreport>
                      # >> ...
                      
    values = ['12267', '12421']
    
    keys = ['job_number', 'job_number']

    dictionary = collections.OrderedDict(zip(keys,values))

    return(dictionary)                      


def three_dicts():
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
    result = three_dicts()
    #result = nsdchat_job_check()

    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cachedir, 'archiware_p5_jobs.json'), 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    main()
