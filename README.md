# gt_weather

## Description 

Using this repo, you can run a container containing script that will look for the current weather using https://openweathermap.org/ public API, based on the defined criteria.

## Summary

In order to scrape and filter https://openweathermap.org/ public API, you need to have registration and subscription for using the forecast API.
You must have docker installed prior using this repo.
This script expects accept at least one command line argument with two options: `rain`,`shine`
When starting the container, you need to define multiple environment variables, which include https://openweathermap.org/ API key, timezone for the schedule, latitude/longitude for the weather location as follows:
```
-e api_key=<openweathermap_API_key> 
-e TZ=<timezone_location> 
-e lat=<latitude_value> 
-e lon=<longitude_value>
```

## How to use repo

1. Clone this repo via Github UI, API or CLI and navigate in to the downloaded folder:

```
gh repo clone georgitsvetkov/gt_weather
cd gt_weather
```

2. Build local docker image
   
`docker build -t weather -f Dokerfile .`

3. Run docker container, using the local build image and pass required container environment variables, together with the line argument (`rain` | `shine`):
   
`docker run -e api_key=<api_key> -e TZ=<timezone_location> -e lat=<latitude_value> -e lon=<longitude_value> weather <command_line_argument>`

Example:
```
docker run -e api_key=<api_key> -e TZ=Europe/Amsterdam -e lat=52.377 -e lon=4.8970  weather shine
```

4. Stop container and clean environment

Stop container using `Ctrl + C` 
Remove created docker image `docker image remove -f weather`

