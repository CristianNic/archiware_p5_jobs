#!/usr/local/munki/python

import os
import sys
import subprocess
import collections
import json

def find_between(s, start, end):
  return (s.split(start))[1].split(end)[0]
  
def nsdchat_job_check():

    ### Retrieve all jobs with warnings
    cmd = ['/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job warning']
    jobs = []
    proc = subprocess.Popen(cmd, text=True, shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, err = proc.communicate()
    jobs.append(output)
    jobs = output.split(' ') # >>> ['12267', '12438', '12421', '12413']
    print(jobs)
    
    # take each item one by one and do all these functions to it 
    # jobs[0] do description and save answer to new list 
    # jobs[1] de start_date_end_date and save answer to new list
    # description(jobs[0])
    # description(jobs[1])  
    # add a parameter --> description(jobs)
    # then loop through the jobs list each time passing a job to the description function
    
    def description(i):
        describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' describe'
        proc = subprocess.Popen(describe, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        return(output)
    
    def start_date_end_date(i):
        between = []
        describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' xmlticket'
        proc = subprocess.Popen(describe, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        start_date = find_between(output, '<startdate>', '</startdate>')
        end_date = find_between(output, '<endtime>', '</endtime>')
        between.append(start_date)
        between.append(end_date)
        between = ' - '.join(between) 
        return(between)
    
    def result(i):
        result = []
        describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' xmlticket'
        proc = subprocess.Popen(describe, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        result = find_between(output, '<result>', '</result>')
        return(result)                                   

    def report(i):
        report = []
        describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' xmlticket'
        proc = subprocess.Popen(describe, text=True, shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        output, err = proc.communicate()
        report = find_between(output, '<report>', '</report>')
        return(report)   
                                                              
    def dictionary():
        list = []
        for i in jobs:
            dict = {'job_number': i, 
                    'desctription': description(i),
                    'start_date_end_date': start_date_end_date(i),
                    'result': result(i),
                    'status': report(i),}
            list.append(dict)     
        return(list)
    
    return(dictionary())




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
