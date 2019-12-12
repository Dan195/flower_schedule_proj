#coding=utf-8
import datetime as dt
from datetime import timedelta
import json
FIDDLE_LEAF = "Fiddle Leaf Fig"
FUTURE_SCHEDULE = "future_schedule"
WATER_AFTER = "water_after"
NAME = "name"
MONDAY = 0
SATURDAY = 5
SUNDAY = 6


class Schedule():
    def __init__(self,file_name="WeGrow_Data.json",weeks=12):
        json_flowers = []
        self.scheduler = {}
        with open(file_name) as file:
            json_flowers = json.load(file)
        for flower in json_flowers:
            self.scheduler[flower[NAME]] = {WATER_AFTER:flower[WATER_AFTER]}
            self.scheduler[flower[NAME]][FUTURE_SCHEDULE] = self.generate_water_schedule(flower, weeks)
            
    def generate_water_schedule(self,flower,weeks):
        schedule_exists = FUTURE_SCHEDULE in flower
        today = self.date_to_str(self.get_next_monday_from_today())
        cur_flower_schedule = flower[FUTURE_SCHEDULE] if schedule_exists else [today]
        days_between_watering = int(self.scheduler[flower[NAME]][WATER_AFTER].split(" ")[0])
        cur_date = cur_flower_schedule[-1] if schedule_exists else cur_flower_schedule[0]
        cur_date = self.str_to_date(cur_date)
        final_date = cur_date + timedelta(weeks=weeks)

        while cur_date + timedelta(days=days_between_watering) < final_date:
            cur_date = self.get_next_weekday(cur_date + timedelta(days=days_between_watering))
            cur_flower_schedule.append(self.date_to_str(cur_date))

        return cur_flower_schedule
            
    def water_flower(self,flower_name):
        date = self.scheduler[flower_name][FUTURE_SCHEDULE][0]
        if date == self.date_to_str(dt.datetime.today()):
            self.scheduler[flower_name][FUTURE_SCHEDULE].pop(0)
            print("You have successfully watered the flower")
        else:
            print("Flower cannot be watered today")

    def get_flowers_to_water_today(self):
        n_flowers_to_water = 0
        for flower_name in self.scheduler:
            date = self.scheduler[flower_name][FUTURE_SCHEDULE][0]
            if date == self.date_to_str(dt.datetime.today()):
                n_flowers_to_water +=1
                print("The {} needs to be watered today".format(flower_name))
        print("A total of {} flowers must be watered today".format(str(n_flowers_to_water)))


    def to_json(self,file_name):
        with open(file_name+'.json', 'w') as file:
            json.dump(self.scheduler,file)

    def str_to_date(self,date):
        return dt.datetime.strptime(date,"%B %d, %Y")

    def date_to_str(self,date):
        return date.strftime("%B %d, %Y")

    def get_next_monday_from_today(self):
        today = dt.datetime.today()
        while today.weekday() != MONDAY:
            today = today + timedelta(days=1)
        return today

    def get_next_weekday(self,date):
        while date.weekday() == SATURDAY or date.weekday() == SUNDAY:
            date = date + timedelta(days=1)

        return date
        
    

    
            

        
