# This problem is found at URL: https://brilliant.org/daily-problems/two-trains-fly/
# Beginning date: 2019.02.13
# Finished date: 2019.02.13

if __name__ == '__main__':

    """ Defining the speeds of train 1, train 2 and the fly in km per hour"""
    train_1_speed_km_per_hour = 50
    train_2_speed_km_per_hour = 50
    fly_speed_km_per_hour = 75

    """ Define the time before trains collied in seconds """
    hours_to_train_collision = 1
    minutes_to_train_collision = hours_to_train_collision * 60
    seconds_to_train_collision = minutes_to_train_collision * 60

    """ Define the speeds of train 1, train 2 and the fly in km per seconds """
    train_1_speed_km_per_sec = round(train_1_speed_km_per_hour / seconds_to_train_collision, 10)
    train_2_speed_km_per_sec = round(train_2_speed_km_per_hour / seconds_to_train_collision, 10)
    fly_speed_km_per_sec = round(fly_speed_km_per_hour / seconds_to_train_collision, 10)

    """ 
    Define variables for keeping track of the distance covered by the fly and 
    the position of train 1, train 2 and the fly    
    """
    fly_total_distance_km = 0
    fly_train_collisions = 0

    train_1_cur_position = 0
    train_2_cur_position = 100
    fly_cur_position = 100

    flying_towards_train_1 = True

    for time in range(0, seconds_to_train_collision):

        """ In case the fly collide with train 2 """
        if round(fly_cur_position, 3) == round(train_2_cur_position, 3) and time != 0:
            print("After " + str(round(time / 60, 1)) + " mins the fly collided with train 2 at the " + str(round(fly_cur_position)) + " km mark")
            print("Train 1 position: " + str(round(train_1_cur_position)))
            print("Train 2 position: " + str(round(train_2_cur_position)))
            print()
            flying_towards_train_1 = True
            fly_train_collisions += 1

        """ In case the fly collide with train 1 """
        if round(fly_cur_position, 3) == round(train_1_cur_position, 3) and time != 0:
            print("After " + str(round(time / 60, 1)) + " mins the fly collided with train 1 at the " + str(round(fly_cur_position))  + " km mark")
            print("Train 1 position: " + str(round(train_1_cur_position)))
            print("Train 2 position: " + str(round(train_2_cur_position)))
            print()
            flying_towards_train_1 = False
            fly_train_collisions += 1

        """ Update the total distance covered by the fly and the current position of train 1, train 2 and the fly """
        fly_total_distance_km += fly_speed_km_per_sec
        train_1_cur_position += train_1_speed_km_per_sec
        train_2_cur_position -= train_2_speed_km_per_sec

        if flying_towards_train_1:
            fly_cur_position -= fly_speed_km_per_sec
        else:
            fly_cur_position += fly_speed_km_per_sec

    """ Print the final result """
    print("Number of collision: " + str(fly_train_collisions))
    print("Total distance covered by fly before train collision: " + str(round(fly_total_distance_km)))