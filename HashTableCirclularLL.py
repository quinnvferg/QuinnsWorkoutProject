import random


class WorkoutHashTable:
    def __init__(self):

        #list of Possible Workouts
        self.workouts_hash =  {
            "bicep": ['Seated Dumbbell Curl', 'Preacher Curl', 'Cable Single arm Curl', 'Barbell Curl', 'Concentration Curl' ],
            "tricep": ['Skull Crushers', 'Tricep Pushdowns', ' Overhead Tricep Extensions', 'Tricep Dips' ],
            "shoulders": ['Overhead Press', 'Front Raises', 'Rear Delt Fly'],
            "back_low": ['Back Extensions', ],
            "back_up": ['Lat Pulldowns', 'T-Bar Row', 'Bent Over Row', 'Seated Row', 'Pull-ups( Assisted/ Not)'],
            "chest_up": ['Incline Dumbbell Press', 'Incline Bench Press', 'Smith Machine Incline Press', 'Dips'],
            "chest_med": ['Flat Bench Press', 'Dumbbell Chest Press', 'Chest Flies', 'Push-Ups'],
            "quads": ['Squat', 'Leg Press', 'Leg Extensions', 'Bulgarian Split Squats'],
            "hamstrings": ['Hamstring Curls', 'RDLS', 'Glute-Ham Raises'],
            "glutes": ['Hip Thrusts', 'Lunges', 'Glute Kickbacks'],
            "calves": ['Standing Calf Raises', 'Seated Calf Raises', 'Leg Press Calf Raises'],
            "cardio": ['StairMaster', 'Treadmail', 'Incline Treadmail'],
            "push": ['Flat Bench Press', 'Incline Dumbell Bench', 'Chest Flies', 'Tricep Pushdowns', 'Overhead Tricep Extensions'],
            "pull": ['Lat Pulldowns', 'Seated Row', 'Pull-ups( Assisted/ Not)', 'Seated Dumbbell Curl', 'Preacher Curl'],
            "legs1": ['Squat', 'RDLS', 'Leg Extensions', 'Hamstring Curls', 'Standing Calf Raises'],
            "legs2": ['Hamstring Curls','RDLS', 'Hip Thursts', 'Glute Kickbacks', 'StairMaster'],
            "legs3": ['Leg Press', 'Hip Thursts', 'Glute Kickbacks', 'Leg Extensions', 'Treadmail'],
            "arms": ['Seated Dumbbell Curl', 'Preacher Curl', 'Tricep Pushdowns', 'Overhead Tricep Extensions', 'Overhead Press', 'Front Raises'],
            "chestback": ['Incline Dumbbell Press', 'Chest Press', 'Lat Pulldowns', 'Seated Row', 'Rear Delt Fly'],
            "rest day": ['Relax!']
  
        }
    def get_workouts(self, day):
        return self.workouts_hash.get(day, {})
    

class Node:
    def __init__(self, day):
        self.day = day
        self.next = None


#Adding the Day Cycle for the Rotation of Splits
class CircularLinkedList:        
    def __init__(self):
        self.tail = None

    def add_day(self, day):
        new_node = Node(day)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail #making it circular

        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def next_day(self):
        # Move the tail to its next node and return its value
        if self.tail:
            self.tail = self.tail.next
            return self.tail
        return None
    
    def display_workout_plan(self):
        if not self.tail:
            print("No workout days have been added.")
            return

        # Start from the head (tail.next)
        current = self.tail.next
        print("Your workout plan:")
        while True:
            print(f"- {current.day}")
            current = current.next
            if current == self.tail.next:
                break
 