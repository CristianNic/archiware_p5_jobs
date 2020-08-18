<?php

use munkireport\processors\Processor;

class Archiware_p5_jobs_processor extends Processor
{
    public function run($json)
    {
        if (! $json ) {
            throw new Exception("Error Processing Request: No JSON file found", 1);
        }
        $data = json_decode($json, true);
        Archiware_p5_jobs_model::where('serial_number', $this->serial_number)->delete();
        foreach($data as $key => $job ) {
            $data[$key]['serial_number'] = $this->serial_number;
        }
        Archiware_p5_jobs_model::insertChunked($data);
    }
}
