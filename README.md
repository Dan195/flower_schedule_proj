The project requires Python 3.x

To run the project, go into the command line, and type python3.

To access the scheduler ...
from flower_scheduler import Scheduler

The following methods are useful to setting your schedule. 

__init__(file_name,weeks)
The file_name should be a path to a JSON file of flowers. The default is WeGrow_Data.json
The weeks should be an integer for how many weeks for which the schedule should be created. The default is 12
Upon construction, the schedule will be initialized in a field, scheduler.

water_flower(flower_name)
To water a specific flower, pass in the flower as a name to the water_flower method.
If it can be watered, it will water and the schedule will update. Otherwise, it will tell you the flower is not to be watered today.

get_flowers_to_water_today()
Retreives each flower that can be watered today, along with the total # of flowers to water today. 

to_json(file_name):
exports the current watering schedule to a json file with name file_name.