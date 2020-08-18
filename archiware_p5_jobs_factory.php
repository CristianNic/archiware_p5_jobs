<?php

// Database seeder
// Please visit https://github.com/fzaninotto/Faker for more options

/** @var \Illuminate\Database\Eloquent\Factory $factory */
$factory->define(Archiware_p5_jobs_model::class, function (Faker\Generator $faker) {

    return [
        'job_id' => $faker->numberBetween($min = 10000, $max = 90000),
        'description' => $faker->randomElement(['Sync Plan: Sync Plan 1', 'Sync Plan: Sync Plan 2']),
        'start_date_end_date' => $faker->dateTimeBetween($startDate = '-1 years', $endDate = 'now')->format('U'),
        'result' => $faker->randomElement(['Exception', 'Failure']),
        'status' => $faker->text($maxNbChars = 200),
    ];
});
