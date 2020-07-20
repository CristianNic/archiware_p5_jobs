<?php
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Capsule\Manager as Capsule;

class ArchiwareP5JobsInit extends Migration
{
    public function up()
    {
        $capsule = new Capsule();
        $capsule::schema()->create('archiware_p5_jobs', function (Blueprint $table) {
            $table->increments('id');
            $table->string('serial_number');
            $table->integer('job_number')->nullable();

            $table->index('serial_number');
            $table->index('job_number');

        });
    }
    
    public function down()
    {
        $capsule = new Capsule();
        $capsule::schema()->dropIfExists('archiware_p5_jobs');
    }
}
