#!/bin/bash
#
# Simulate nsdchat for archiware_p5_jobs.py
# Returns nsdchat job query results
#
# https://ryanstutorials.net/bash-scripting-tutorial/bash-variables.php
# http://www.compciv.org/topics/bash/conditional-branching/
#
# Orignial commands
# /usr/local/aw/bin/nsdchat -c Job warning
# /usr/local/aw/bin/nsdchat -c Job [#####] describe
# /usr/local/aw/bin/nsdchat -c Job [#####] xmlticket
#
# Simulated commands
# sh nsdchat_job_simulator.sh Job warning
# sh nsdchat_job_simulator.sh ##### describe
# sh nsdchat_job_simulator.sh ##### xmlticket
#

if [[ $1 == 'Job' ]] && [[ $2 == 'warning' ]] ; then
  printf '12267 12438 12421 12413'

elif [[ $1 == 'Job' ]] && [[ $2 == '2_warnings' ]]; then
  printf '12267 12421'

elif [[ $1 == 'Job' ]] && [[ $2 == '12267' ]] && [[ $3 == 'describe' ]]; then
  printf 'Sync Plan: Sync Plan 1'

elif [[ $1 == 'Job' ]] && [[ $2 == '12267' ]] && [[ $3 == 'xmlticket' ]]; then
  printf "<jobreport>
    <description>Sync Plan: Sync Plan 1</description>
    <startdate>15.05.2016</startdate>
    <enddate>15.05.2016</enddate>
    <starttime>00:00:00</starttime>
    <endtime>04:24:33</endtime>
    <command>JobMgr sync 10001 -events 0 -cycles 0 -versions 0 -delete 1 -filter {} -hours 0</command>
    <result>exception</result>
    <report>Syncing '/Volumes/Xsan/Production/Server' to '/Volumes/RAID1/P5-Sync/' ...
Finished: copied 1747 files/folders, 171.63 MB.

WARNING: check file access log!</report>
    <files>
        <file>/Volumes/RAID1/P5-Sync//00__/Super-Elements.rtf</file>
        <status>file truncated</status>
    </files>
</jobreport>"

elif [[ $1 == 'Job' ]] && [[ $2 == '12438' ]] && [[ $3 == 'describe' ]]; then
  printf 'Sync Plan: Sync Plan 1'

elif [[ $1 == 'Job' ]] && [[ $2 == '12438' ]] && [[ $3 == 'xmlticket' ]]; then
  printf "<jobreport>
      <description>Sync Plan: Sync Plan 1</description>
      <startdate>19.05.2016</startdate>
      <enddate>31.12.1969</enddate>
      <starttime>08:00:00</starttime>
      <endtime>16:00:00</endtime>
      <command>JobMgr sync 10001 -events 0 -cycles 0 -versions 0 -delete 1 -filter {} -hours 0</command>
      <result>failure</result>
      <report></report>
  </jobreport>"

elif [[ $1 == 'Job' ]] && [[ $2 == '12421' ]] && [[ $3 == 'describe' ]]; then
  printf 'Sync Plan: Sync Plan 2'

elif [[ $1 == 'Job' ]] && [[ $2 == '12421' ]] && [[ $3 == 'xmlticket' ]]; then
  printf "<jobreport>
      <description>Sync Plan: Sync Plan 2</description>
      <startdate>19.05.2016</startdate>
      <enddate>19.05.2016</enddate>
      <starttime>04:00:00</starttime>
      <endtime>06:08:27</endtime>
      <command>JobMgr sync 10001 -events 0 -cycles 0 -versions 0 -delete 1 -filter {} -hours 0</command>
      <result>exception</result>
      <report>Syncing '/Volumes/Xsan/Production/-Server' to '/Volumes/LaCieRAID1/P5-Sync/' ...
  Finished: copied 18150 files/folders, 326.43 MB.

  WARNING: check file access log!</report>
      <files>
          <file>/Volumes/LaCieRAID1/P5-Sync//00__/054 The Cobbler of Konduz/Setups/Scenes - Missing Elements.rtf alias</file>
          <status>file truncated</status>
      </files>
  </jobreport>"
  
elif [[ $1 == 'Job' ]] && [[ $2 == '12413' ]] && [[ $3 == 'describe' ]]; then
  printf 'Sync Plan: Sync Plan 1'
  
elif [[ $1 == 'Job' ]] && [[ $2 == '12413' ]] && [[ $3 == 'xmlticket' ]]; then
  printf "<jobreport>
      <description>Sync Plan: Sync Plan 1</description>
      <startdate>19.05.2016</startdate>
      <enddate>19.05.2016</enddate>
      <starttime>00:00:00</starttime>
      <endtime>02:57:24</endtime>
      <command>JobMgr sync 10001 -events 0 -cycles 0 -versions 0 -delete 1 -filter {} -hours 0</command>
      <result>exception</result>
      <report>Syncing '/Volumes/Xsan/Production/-Server' to '/Volumes/LaCieRAID1/P5-Sync/' ...
  Finished: copied 31686 files/folders, 384.06 MB.

  WARNING: check file access log!</report>
      <files>
          <file>/Volumes/LaCieRAID1/P5-Sync//00__/054 The Cobbler of Konduz/Setups/Scenes - Missing Elements.rtf alias</file>
          <status>file truncated</status>
      </files>
  </jobreport>"

fi
