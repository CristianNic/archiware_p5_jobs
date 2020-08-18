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
            $table->integer('job_id')->nullable();
            $table->string('description')->nullable();
            $table->string('start_date_end_date')->nullable();
            $table->string('result')->nullable();
            $table->string('status')->nullable();

            $table->index('job_id');
            $table->index('description');
            $table->index('start_date_end_date');
            $table->index('result');
            $table->index('status');

        });
    }

    public function down()
    {
        $capsule = new Capsule();
        $capsule::schema()->dropIfExists('archiware_p5_jobs');
    }
}
