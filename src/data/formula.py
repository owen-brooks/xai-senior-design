from scipy.stats import truncnorm


def calc_trip_consumption(tf, td, to, ei, vers=0):
    """Modify input variables to match varations

    Uses different variations of the formula
    :param tf: Trip Frequency
    :param td: Trip Distance
    :param to: Transportation Occupancy
    :param ei: Energy Intensity
    :param vers: version of forumla, defaults to actual formula
    """
    if vers == 0:
        #(tf * (td / to)) * ei  # default
        return tf, td, to, ei
    elif vers == 1:
        #((tf * 2) * (td / to * 3)) * ei
        return tf * 2, td, to * 3, ei
    elif vers == 2:
        #(tf * (td / to)) * (ei ** 0.5)
        return tf, td, to, ei ** 0.5
    elif vers == 3:
        #((tf ** 0.5) * (td / to)) * ei
        return tf ** 0.5, td, to, ei
    elif vers == 4:
        #tf * (td / (to)) * (ei ** 2)
        return tf, td, to, ei ** 2
    elif vers == 5:
        #tf * (2 * td / (to)) * (ei)
        return tf, 2 * td, to, ei   
    elif vers == 6:
        #(tf * (td / to ** 2)) * ei
        return tf, td, to ** 2, ei
    elif vers == 7:
        #((tf ** 0.5) * (td / to)) * (ei ** 2)
        return tf ** 0.5, td, to, ei ** 2
    elif vers == 8:
        #((tf * 3) * (td / to)) * (ei ** 0.5)
        return tf * 3, td, to, ei ** 0.5
    elif vers == 9:
        #(tf * (td / (to ** 0.5))) * ei
        return tf, td, to ** 0.5, ei


def calc_trip_consumption_2(tt, speed, fe, vers=0):
    """Modify input variables to match varations

    Uses different variation of the formula
    :param tt: travel time (hrs)
    :param speed: average speed for mode (mph)
    :param fe: fuel economy for mode (kWh per passenger mile)
    :param vers: version of formula, defaults to actual formula
    """

    if vers == 0:
        #tt * speed * fe  # default
        return tt, speed, fe  # default
    elif vers == 1:
        #(tt ** 2) * speed * fe
        return tt ** 2, speed, fe
    elif vers == 2:
        #tt * (speed ** 2) * fe
        return tt, speed ** 2, fe
    elif vers == 3:
        #tt * speed * (fe ** 2)
        return tt, speed, fe ** 2
    elif vers == 4:
        #(tt ** 0.5) * speed * fe
        return tt ** 0.5, speed, fe
    elif vers == 5:
        #tt * (speed ** 0.5) * fe
        return tt, speed ** 0.5, fe
    elif vers == 6:
        #tt * speed * (fe ** 0.5)
        return tt, speed, fe ** 0.5


def gen_rand_vals(mu, sigma, lower, upper, N):
    """Uses truncated normal dist to find rand vals"""
    a, b = (lower - mu) / sigma, (upper - mu) / sigma
    return truncnorm.rvs(a, b, mu, sigma, size=N)


def get_td():
    return gen_rand_vals(7.772449, 10.648316, 0.004418, 130.474121, 1)[0]


def get_tf():
    # num trips needs to be an int
    return round(gen_rand_vals(2.787475, 2.082404, 1, 20, 1)[0])


def get_car_to():
    # num of occupants needs to be an int
    return round(gen_rand_vals(2.196296, 12.488912, 1, 23, 1)[0])
