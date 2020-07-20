<?php

use munkireport\models\MRModel as Eloquent;

class Archiware_p5_jobs_model extends Eloquent
{
    protected $table = 'archiware_p5_jobs';

    protected $hidden = ['id', 'serial_number'];

    protected $fillable = [
      'serial_number',
      'job_number',

    ];
}
