#!/usr/local/munki/python
# Archiware P5 Jobs script for MunkiReport
# by Cristian Niculescu

import os
import subprocess
import collections
import json

nsdchat_path = '/usr/local/aw/bin/nsdchat'
# nsdchat_path = '/users/cristian/dev/github/cristiannic/archiware_p5_draft/archiware_p5_jobs_scripts/nsdchat_job_simulator.sh'
# nsdchat_path = '/users/cristian/dev/github/cristiannic/archiware_p5_draft/archiware_p5_jobs_scripts/nsdchat_job_simulator_empty.sh'

def find_between(str, start, end):
  return (str.split(start))[1].split(end)[0]

def subprocess_output(cmd):
    proc = subprocess.Popen(cmd, text=True, shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, err = proc.communicate()
    return(output)   

def dictionary(i):
    dict = {}
    keys = ['job_id', 'description', 'start_date_end_date', 'result', 'status']

    cmd = nsdchat_path + ' -c Job ' + i + ' xmlticket'     
    output = subprocess_output(cmd)    
    
    job_id = int(i)
    description = find_between(output, '<description>', '</description>')
    start_date = find_between(output, '<startdate>', '</startdate>')
    end_date = find_between(output, '<enddate>', '</enddate>')
    start_date_end_date = start_date + ' - ' + end_date
    result = find_between(output, '<result>', '</result>').capitalize()
    status = find_between(output, '<report>', '</report>') 
    if status  == '':
        status = 'No Report'
    else:
        status
    
    values = [job_id, description, start_date_end_date, result, status] 
    
    dictionary = collections.OrderedDict(zip(keys,values))  
    
    return(dictionary)
        
def nsdchat_job_check():
    # Retrieve all jobs with warnings
    jobs = []
    cmd = nsdchat_path + ' -c Job failed 5'
    output = subprocess_output(cmd)
    
    # If there are no jobs with warnings output 'none'
    if output == '<empty>\n':
        list = []
        dict = {'job_id': 0,
                'description': 'none',
                'start_date_end_date': 'none',
                'result': 'none',
                'status': 'none'}
        list.append(dict) 
        return(list)
        
    # If there are jobs check details and fill in a dictionary for each
    else:    
        jobs.append(output)
        jobs = output.split(' ')                                                         
        list = []
        for i in jobs:
            dict = dictionary(i)
            list.append(dict)     
        return(list)            
        
def main():
    
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