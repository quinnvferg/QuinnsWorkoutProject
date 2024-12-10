from HashTableCirclularLL import WorkoutHashTable
from HashTableCirclularLL import CircularLinkedList
from CALPROTCALC import CalorieProtein
from CALPROTCALC import StrengthEnduranceTree
from CALPROTCALC import ProgressionGraph


#///////////////////////////////////////////////////////////
def main():
    # INTRO
    print('Welcome to Your Personalized Workout Experience!')

    # GOAL
    while True:
        goal = input("What is your goal with working out? Losing weight, gaining muscle or maintaining muscle? ('lose', 'gain', 'maintain'): ").strip().lower()
        if goal in ['lose', 'gain', 'maintain']: 
            break
        print("Invalid input. Please type: 'lose', 'gain', or 'maintain'.")

    # WORKOUT TYPE
    while True:
        workout_type = input("Enter your workout preference ('ppl', arnold, 3(3 day split), 5(5 day split), or glutes, legs, and upper): ").strip().lower()
        if workout_type in ['ppl', 'arnold', 'glutes, legs, and upper', '3', '5']:
            break
        print("Invalid input. Please choose from: '3', '5', 'ppl', 'arnold', 'glutes, legs, and upper' ")

    while True:
        training_type = input("Are you Training for Strength or for Endurance (strength, endurance): ").strip().lower()
        if training_type in ['strength', 'endurance']:
            break
        print("Invalid input. Please choose from: 'strength' or 'endurance'.")

    # Getting user INPUT
    try:
        user_weight = float(input("Enter your weight (in KG): "))
        user_height = float(input("Enter your height (in inches): "))
        user_age = int(input("Enter your age (number only): "))
        user_gender = input("Enter your gender (male/female): ").lower()
        if user_gender not in ["male", "female"]:
            raise ValueError("Invalid gender.")
        body_fat_percent = float(input("Enter your body fat percentage (e.g., 20 for 20%): "))
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

#///////////////////////////////////////////////////////////

    # INITIZALIZING CIRCULAR LINKED LIST AND WORKOUT HASH
    workout_table = WorkoutHashTable()
    workout_days = CircularLinkedList()
    progression_graph = ProgressionGraph()
    strength_tree = StrengthEnduranceTree()

    n = None

    # SETTING WORKOUT PLANS
    if workout_type == 'ppl':
        n = 3
        workout_days.add_day("push")
        workout_days.add_day("pull")
        workout_days.add_day("legs1")
    elif workout_type == '3':
        n = 3
        workout_days.add_day("push")
        workout_days.add_day("pull")
        workout_days.add_day("legs1")
    elif workout_type == '5':
        n = 5
        workout_days.add_day("push")
        workout_days.add_day("pull")
        workout_days.add_day("legs1")
        workout_days.add_day("push")
        workout_days.add_day("pull")
    elif workout_type == 'arnold':
        n = 5
        workout_days.add_day("push")
        workout_days.add_day("pull")
        workout_days.add_day("legs1")
        workout_days.add_day("arms")
        workout_days.add_day("chestback")
    elif workout_type == 'glutes, legs, and upper':
        n = 5
        workout_days.add_day('legs1')
        workout_days.add_day('legs2')
        workout_days.add_day('push')
        workout_days.add_day('legs3')
        workout_days.add_day('pull')
    else: 
        print("Workout Not available. Please choose from the following: 'ppl', '5', '3', 'arnold', 'glutes, legs, and upper' ")
        return workout_days.display_workout_plan()
    

    #Creating the Strngth VS Endurance Pathing
    if training_type == "strength":
        strength_tree.calculate_max_lifts(user_weight, body_fat_percent, user_height, user_age, user_gender)
        bench = strength_tree.root['Strength']['Upper Body']['Max Bench Press']
        squat = strength_tree.root['Strength']['Lower Body']['Max Squat']
        deadlift = strength_tree.root['Strength']['Lower Body']['Max Deadlift']
    elif training_type == "endurance":
        strength_tree.calculate_endurance_lifts(user_weight, body_fat_percent, user_height, user_age, user_gender)
        bench = strength_tree.root['Endurance']['Upper Body']['Endurance Bench']
        squat = strength_tree.root['Endurance']['Lower Body']['Endurance Squat']
        deadlift = strength_tree.root['Endurance']['Lower Body']['Endurance Deadlift']
    else:
        print("Invalid Response, Defaulting to Strength Training")
        strength_tree.calculate_max_lifts(user_weight, body_fat_percent, user_height, user_age, user_gender)
        bench = strength_tree.root['Strength']['Upper Body']['Max Bench Press']
        squat = strength_tree.root['Strength']['Lower Body']['Max Squat']
        deadlift = strength_tree.root['Strength']['Lower Body']['Max Deadlift']
    #Establishing Prgression Nodes
    bench_node = f"Bench Press: {round(bench)} kg"
    squat_node = f"Squat: {round(squat)} kg"
    deadlift_node = f"Deadlift: {round(deadlift)} kg"
    progression_graph.add_node(bench_node)
    progression_graph.add_node(squat_node)
    progression_graph.add_node(deadlift_node)

    # Calories and Protein intake
    try:
        results = CalorieProtein.calculate_calories(user_weight, user_height, user_age, user_gender, n=n, goal=goal)
        print(f"Based on your goal, ({goal}):")
        print(f"Daily Calories: {results['daily_calories']} kcal")
        print(f"Protein Intake: {results['protein_intake']} grams")
    except ValueError as e:
        print(f"Error in calculation: {e}")
        return

    # Stack for undo functionality
    undo_stack = []
    day_count = 1


#///////////////////////////////////////////////////////////
#Starting the Cycle

    print("\nLet's start your workout cycle!")
    while True:
        current_day = workout_days.tail  # Get the current day from tail
        day_name = current_day.day
        workouts = workout_table.get_workouts(day_name)

        print(f"\nDay {day_count}: {day_name.capitalize()} Day")
        print("\nHere are your workouts for the day:")
        for exercise in workouts:
            print(f" - {exercise}")
        
        completed = input("\nHave you completed this workout? (yes/no/undo): ").lower()

        #YES
        if completed == "yes":
            print("Great job completing your workout!")
            undo_stack.append({"day_name": day_name, "workouts": workouts})  # Save current state
            day_count += 1
            workout_days.next_day()  # Move to the next day

            # VIEW STRENGTH PROGRESSION
            view_progression = input("\nDo you want to see your Progression? (yes/no): ").lower()
            if view_progression == "yes":
                print("\nYour Max Lifts:")
                print(f"- Bench Press: {bench_node.split(':')[1].strip()}")
                print(f"- Squat: {squat_node.split(':')[1].strip()}")
                print(f"- Deadlift: {deadlift_node.split(':')[1].strip()}")
                
                progression_choice = input("\nWould you like to progress any of your lifts? (yes/no): ").lower()
                if progression_choice == "yes":
                    weight_increment = 4.5
                    while True:
                        choice = input("Which lift do you want to progress? (bench, squat, deadlift, no): ").lower()
                        if choice == 'no':
                            print("Exiting Progression Tracking.")
                            break

                        # Determine the lift and corresponding node
                        if choice == 'bench':
                            current_node = bench_node
                        elif choice == 'squat':
                            current_node = squat_node
                        elif choice == 'deadlift':
                            current_node = deadlift_node
                        else:
                            print("Invalid choice. Try again.")
                            continue

                        # Show current goal and ask if completed
                        print(f"\nCurrent Goal: {current_node}")
                        completed_goal = input("Have you completed this goal? (yes/no): ").lower()
                        if completed_goal == "yes":
                            next_node = progression_graph.update_progression(current_node, weight_increment)
                            print(f"Great job! Your next goal is: {next_node}")
                            # Update the Nodes (lifts)
                            if choice == 'bench':
                                bench_node = next_node
                            elif choice == 'squat':
                                squat_node = next_node
                            elif choice == 'deadlift':
                                deadlift_node = next_node
                        elif completed_goal == "no":
                            print("Take your time. Progression isn't always linear.")
                        else:
                            print("Invalid input. Please type 'yes' or 'no'.")
                else:
                    print("No progression changes made.")
            else:
                print("No Worries, you can always check tomorrow!")

        #UNDO
        elif completed == "undo":
            if undo_stack:
                last_action = undo_stack.pop()
                print(f"\nUndoing...")
                print("\nHere are your workouts for the day:")
                for exercise in last_action["workouts"]:
                    print(f" - {exercise}")
                day_count -= 1
            else:
                print("Nothing to undo!")

        #NO
        elif completed == "no":
            print("Take your time and complete your workout when ready.")

        else:
            print("Invalid input. Please type 'yes', 'no', or 'undo'.")

        # CONTINUE OR END
        continue_workout = input("\nDo you want to continue to the next day? (yes/no): ").lower()
        if continue_workout != "yes":
            print("Workout Routine Ending. Come back soon!")
            break


#///////////////////////////////////////////////////////////


if __name__ == "__main__":
    main()