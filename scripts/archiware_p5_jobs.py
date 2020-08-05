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
    out = []
    proc = subprocess.Popen(cmd, text=True, shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    output, err = proc.communicate()
    out.append(output)
    out = output.split(' ') # >>> ['12267', '12284', '12294', '12438', '12421', '12413']
    #print(out)
            
    def description():
        for i in out:
            describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' describe'
            proc = subprocess.Popen(describe, text=True, shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            output, err = proc.communicate()
            return(output)                    
    
    def start_date_end_date():
        for i in out:
            between =[]
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
    
    def result():
        for i in out:
            result = []
            describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' xmlticket'
            proc = subprocess.Popen(describe, text=True, shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            output, err = proc.communicate()
            result = find_between(output, '<result>', '</result>')
            return(result)                                   

    def report():
        for i in out:
            report = []
            describe = '/users/cristian/dev/munki/archiware_p5_draft/archiware_p5_jobs/nsdchat_job_simulator.sh Job ' + i + ' xmlticket'
            proc = subprocess.Popen(describe, text=True, shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
            output, err = proc.communicate()
            report = find_between(output, '<report>', '</report>')
            return(report)   
                                                              
    dict = []
    for i in out:
        info = {
            'job_number':           i,
            #'description':          'desctiption.find_between(s, start, end)',
            'description':          description(),  # function for obtaining description
                                                          # def obtain_description
                                                          #     for i in out:           # for each job number run it though the describe command
                                                          #         return(description) # don't append to anything, just return it
                                                          # place this function seperate? bellow. 
            'start_date_end_date':  start_date_end_date(),
            'result':               result(),
            'status':               report(),
            }
        dict.append(info)
        #print(dict)
        #return(dict)
    return(dict)




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
