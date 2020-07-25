<?php

use munkireport\processors\Processor;

class Archiware_p5_jobs_processor extends Processor
{
    public function run($json)
    {
        // Check if data was uploaded
        if (! $json ) {
            throw new Exception("Error Processing Request: No JSON file found", 1);
        }
        // Process json into object thingy
        $data = json_decode($json, true);
        $data['serial_number'] = $this->serial_number;
        Archiware_p5_jobs_model::where('serial_number', $this->serial_number)->delete();
        foreach($data as $key => $job ) {
            $data[$key]['serial_number'] = $this->serial_number;
        }
        Archiware_p5_jobs_model::insertChunked($data);
    }
}


