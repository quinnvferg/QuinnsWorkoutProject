
class CalorieProtein:
    @staticmethod
    def calculate_calories(user_weight, user_height, user_age, user_gender, n, goal="maintain"):

        # Calculate BMR (Mifflin-St Jeor equation)
        if user_gender.lower() == 'male':
            bmr = 10 * user_weight + 6.25 * (user_height * 2.54) - 5 * user_age + 5
        else:
            bmr = 10 * user_weight + 6.25 * (user_height * 2.54) - 5 * user_age - 161

        if n == 3:
            daily_calories = bmr * 1.375

        if n == 5:
            daily_calories = bmr * 1.2

        # Adjust based on goal
        if goal.lower() == "gain":
            daily_calories += 500  
        elif goal.lower() == "lose":
            daily_calories -= 500  

        # PROTEIN INTAKE (in KG you should eat 1.6x your body weight)
        if goal.lower() == 'maintain':
            protein_intake = user_weight * 1.6

        if goal.lower() == 'lose':
            protein_intake = user_weight * 1.8

        if goal.lower() == 'gain':
            protein_intake = user_weight * 2.0

        return {
            "protein_intake": round(protein_intake),
            "daily_calories": round(daily_calories)
        }

class StrengthEnduranceTree:

    def __init__(self):
        self.root= {'Strength': {} , 'Endurance': {} }

        #Creating The Roots to Store the data
        self.root['Strength']['Upper Body'] = {'Max Bench Press': None}
        self.root['Strength']['Lower Body'] = {'Max Squat': None, 'Max Deadlift': None}
        self.root['Endurance']['Upper Body'] = {'Endurance Bench': None}
        self.root['Endurance']['Lower Body'] = {'Endurance Squat': None, 'Endurance Deadlift': None}

    def calculate_max_lifts(self, body_weight, body_fat_percent, user_height, user_age, user_gender):
        #Lean Body Mass Calculator
        lbm = body_weight * (1 - body_fat_percent / 100)

        #USER IMPUT ADJUSTMENT
        adjusted_height = 1.0
        if user_height > 70 :    #6ft in inches
            adjusted_height = 0.9
        
        adjusted_age = 1.0
        if user_age >= 35 and user_age <= 45: #For ages between 35 and 45 90% 
            adjusted_age = 0.9
        elif user_age > 45: #if they are older than 45 75% 
            adjusted_age = 0.75

        adjusted_gender = 1.0
        if user_gender.lower() == 'female': #If they are female 70%
            adjusted_gender = 0.7

        adjusted_lbm = lbm * adjusted_height * adjusted_age * adjusted_gender
        
        # Calculating Max Lifts (Number is the MULTIPLIER)
        max_bench = adjusted_lbm * 0.8  
        max_squat = adjusted_lbm * 1.2  
        max_deadlift = adjusted_lbm * 1.3  
        
        #Storing The values (Strength)
        self.root['Strength']['Upper Body']['Max Bench Press'] = max_bench
        self.root['Strength']['Lower Body']['Max Squat'] = max_squat
        self.root['Strength']['Lower Body']['Max Deadlift'] = max_deadlift
    
    def calculate_endurance_lifts(self, body_weight, body_fat_percent, user_height, user_age, user_gender):
        #Lean Body Mass Calculator
        lbm = body_weight * (1 - body_fat_percent / 100)

                #USER IMPUT ADJUSTMENT
        adjusted_height = 1.0
        if user_height > 70 :    #6ft in inches
            adjusted_height = 0.9
        
        adjusted_age = 1.0
        if user_age >= 35 and user_age <= 45: #For ages between 35 and 45 90% 
            adjusted_age = 0.9
        elif user_age > 45: #if they are older than 45 75% 
            adjusted_age = 0.75

        adjusted_gender = 1.0
        if user_gender.lower() == 'female': #If they are female 70%
            adjusted_gender = 0.7

        adjusted_lbm = lbm * adjusted_height * adjusted_age * adjusted_gender
        
        #Calculating Endurance Weight (10-15 reps)
        endurance_bench = adjusted_lbm * 0.4 
        endurance_squat = adjusted_lbm * 0.6  
        endurance_deadlift = adjusted_lbm * 0.65  
        
        #Storing the Values (Endurance)
        self.root['Endurance']['Upper Body']['Endurance Bench'] = endurance_bench
        self.root['Endurance']['Lower Body']['Endurance Squat'] = endurance_squat
        self.root['Endurance']['Lower Body']['Endurance Deadlift'] = endurance_deadlift
        
#/////////////////////////////////////////////////////
#ADD GRAPH WITH VISUAL OF TREE AND PROGRESSION

class ProgressionGraph:
    def __init__(self):
        self.graph = {}

    def new_edge(self, from_node, to_node):
        if from_node in self.graph:
            self.graph[from_node].append(to_node)
        else:
            self.graph[from_node] = [to_node]

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def update_progression(self, current_node, weight_increment):
        current_weight = float(current_node.split(" ")[-2])
        new_weight = current_weight + weight_increment
        next_node = f"{current_node.split(':')[0]}: {new_weight} kg"
        self.add_node(next_node)
        self.new_edge(current_node, next_node)
        return next_node
    #///////////////////////////////////////////////////////////


