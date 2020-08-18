<?php

/**
 * archiware_p5_jobs class
 *
 * @package munkireport
 * @author
 **/
class Archiware_p5_jobs_controller extends Module_controller
{
	    function __construct()
    {
        // Store module path
        $this->module_path = dirname(__FILE__);
    }

    /**
     * Get archiware_p5_jobs information for serial_number
     *
     * @param string $serial serial number
     **/
    public function get_data($serial_number = '')
    {
				$string = (string) conf('job_id');
				
        jsonView(
            Archiware_p5_jobs_model::select('archiware_p5_jobs.*')
            ->whereSerialNumber($serial_number)
						->set(REPLACE(count, ',', CHAR(10)))
            ->filter()
						->replace($string, ',', CHAR(10))
            ->limit(1)
            ->first()
            ->toArray()
        );
    }

    public function get_list($column = '')
    {
				$string = (string) conf('job_id');
				
        jsonView(
						Archiware_p5_jobs_model::select("archiware_p5_jobs.$column AS label")
                ->selectRaw('count(*) AS count')
                ->filter()
								->replace($string, ',', CHAR(10))
                ->groupBy($column)
                ->orderBy('count', 'desc')
                ->get()
                ->toArray()
        );
    }
}
