from math import cos, pi
from matplotlib import pyplot

###################
#      PARAMS     #
###################

# this array store the calculated temperatures (final result)
calculated_temperatures = []

# first time predicted
init_time = 0

# last time predicted
end_time = 48

# array of relevant temperatures (max and min)
relevant_temperatures = [15, 30, 12, 37]

# array of relevant hours of relevant_temperatures
relevant_hours = [6, 18, 30, 40]


###################
#    Functions    #
###################

# this function returns the previous relevant duple of the given hour
def get_previous(hour):
    for t in range(0, len(relevant_hours_and_temperatures)):
        if hour <= relevant_hours_and_temperatures[t][0]:
            return relevant_hours_and_temperatures[t-1]


# this function returns the next relevant duple of the given hour
def get_next(hour):
    for t in relevant_hours_and_temperatures:
        if hour <= t[0]:
            return t


# function to sort the duple's array by the first element of the duple
def sort_by_first(val):
    return val[0]


########################
#    Main Algorithm    #
########################

# create a duple's array with hours and temperatures
relevant_hours_and_temperatures = list(zip(relevant_hours, relevant_temperatures))

# get first and last relevant data
first_relevant_hour = relevant_hours_and_temperatures[0][0]
last_relevant_hour = relevant_hours_and_temperatures[len(relevant_hours_and_temperatures)-1][0]

# sorts the array ascending by hour
relevant_hours_and_temperatures.sort(key=sort_by_first)

# loop to predict the temperature of each hour
for current_hour in range(init_time, end_time):
    # get previous and next relevant routes of current hour
    if current_hour <= first_relevant_hour:
        min_hour, min_temperature = relevant_hours_and_temperatures[0]
        max_hour, max_temperature = relevant_hours_and_temperatures[1]
    elif current_hour >= last_relevant_hour:
        min_hour, min_temperature = relevant_hours_and_temperatures[len(relevant_hours_and_temperatures)-2]
        max_hour, max_temperature = relevant_hours_and_temperatures[len(relevant_hours_and_temperatures)-1]
    else:
        min_hour, min_temperature = get_previous(current_hour)
        max_hour, max_temperature = get_next(current_hour)

    # if the hour of the maximum temperature occurs before the hour of the minimum temperature then swap max and min
    if max_hour < min_hour:
        aux = min_hour
        min_hour = max_hour
        max_hour = aux
        aux = min_temperature
        min_temperature = max_temperature
        max_temperature = aux

    # Q-sin calculation
    avg_hour = (min_hour+max_hour)/2
    if current_hour <= avg_hour:
        # temperature from min_hour to lambda
        pre_cos_calculation = (max_temperature - min_temperature) / 2
        cos_calculation = ((current_hour - 2*avg_hour + min_hour) * pi) / (2*(avg_hour - min_hour))
        calculated_temperatures.append(pre_cos_calculation * (cos(cos_calculation) + 1) + min_temperature)
    else:
        # temperature from lambda to max_hour
        pre_cos_calculation = (max_temperature - min_temperature) / 2
        cos_calculation = ((current_hour - max_hour) * pi) / (2 * (max_hour - avg_hour))
        calculated_temperatures.append(pre_cos_calculation * (cos(cos_calculation) + 1) + min_temperature)

# show the plot
pyplot.plot(relevant_hours, relevant_temperatures, 'ro')
pyplot.plot(calculated_temperatures)
pyplot.show()
