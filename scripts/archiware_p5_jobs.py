#!/usr/local/munki/python
# Archiware P5 Jobs script for MunkiReport
# by Cristian Niculescu

import os
import subprocess
import json

nsdchat_path = '/usr/local/aw/bin/nsdchat'
# nsdchat_path = '/users/cristian/dev/github/cristiannic/archiware_p5_draft/archiware_p5_jobs_scripts/nsdchat_job_simulator.sh' 

def find_between(str, start, end):
  return (str.split(start))[1].split(end)[0]

def subprocess_output(cmd):
    proc = subprocess.Popen(cmd, text=True, shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, err = proc.communicate()
    return(output)   
        
def description(i):
    cmd = nsdchat_path + ' Job ' + i + ' describe'
    output = subprocess_output(cmd)
    return(output)
    
def start_date_end_date(i):
    between = []
    cmd = nsdchat_path + ' Job ' + i + ' xmlticket'
    output = subprocess_output(cmd)
    start_date = find_between(output, '<startdate>', '</startdate>')
    end_date = find_between(output, '<enddate>', '</enddate>')
    between.append(start_date)
    between.append(end_date)
    between = ' - '.join(between) 
    return(between)
    
def result(i):
    result = []
    cmd = nsdchat_path + ' Job ' + i + ' xmlticket'
    output = subprocess_output(cmd)
    result = find_between(output, '<result>', '</result>').capitalize()
    return(result)                                   

def report(i):
    report = []
    cmd = nsdchat_path + ' Job ' + i + ' xmlticket'
    output = subprocess_output(cmd)
    report = find_between(output, '<report>', '</report>')
    return(report)   
 
def nsdchat_job_check():

    # Retrieve all jobs with warnings
    jobs = []
    cmd = nsdchat_path + ' Job ' + ' warning'
    output = subprocess_output(cmd)
    jobs.append(output)
    jobs = output.split(' ')
    
    # Check details for each job filling in a dictionary for each                                                          
    list = []
    for i in jobs:
        dict = {'job_id': int(i),  
                'description': description(i),
                'start_date_end_date': start_date_end_date(i),
                'result': result(i),
                'status': report(i)}
        list.append(dict)     
    return(list)
    
def main():

    """Main"""
    # Check if Archiware P5 Jobs is installed
    if  not os.path.isfile('/usr/local/aw/bin/nsdchat'):
        print ("ERROR: Archiware P5 is not installed")
        exit(0)

    # Get information about Archiware P5 Jobs
    result = nsdchat_job_check()
    
    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cachedir, 'archiware_p5_jobs.json'), 'w') as fp:
        json.dump(result, fp, indent=4)

if __name__ == '__main__':
    main()

