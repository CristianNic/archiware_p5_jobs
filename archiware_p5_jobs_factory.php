<?php

// Database seeder
// Please visit https://github.com/fzaninotto/Faker for more options

/** @var \Illuminate\Database\Eloquent\Factory $factory */
$factory->define(Archiware_p5_jobs_model::class, function (Faker\Generator $faker) {

    return [
        'job_number' => $faker->randomNumber($nbDigits = 4, $strict = false),
    ];
});
