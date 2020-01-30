import pandas as pd
import random

from src.data.dataset_utils import (
    calc_trip_consumption,
    calc_trip_consumption_2,
    gen_rand_vals,
    get_td,
    get_tf,
    get_car_to,
)

"""
## MODE (From Shideh's Notebook)
# 8(taxi)== 10(shuttel),13(private transit), 9 (rental car), 19(paratansit)
#22 (rail) == 28(other rail), 23 (trolly..), 24(NI commuter rail), 25(ni rail)
# 21(subway) == 27(train), 26 (pastco)
#14(bus) == 17(amtrak bus), 15== transit bus , 20(otherbus)
# 2 (bikE) == 3(wheelchair), 3(other non mot), 7(mope, motor)
"""
modes_key = {
    5: "Private Vehicle",
    8: "Taxi/Shuttle/Private Transit",
    21: "subway/train/pastco",
    14: "bus/amtrak bus/transit bus",
    26: "school bus",
    22: "rail/trolly/pastco",
}
modes_ei = {5: 1.354954955, 8: 1.21, 21: 0.5899, 14: 0.7872, 26: 4.814285714, 22: 0.933}
modes_to = {5: get_car_to(), 8: 3, 21: 75, 14: 55, 26: 26, 22: 120}

modes2_key = {
    0: "Bus",
    1: "Transfer Bus",
    2: "Subway",
    3: "Ferry",
    4: "Commuter Rail",
    5: "Auto",
}
modes2_fe = {0: 0.7872, 1: 0.7872, 2: 0.5899, 3: 1.3747, 4: 0.9331, 5: 1.21}
modes2_speed = {0: 7.64, 1: 7.64, 2: 18.21, 3: 10.46, 4: 34.13, 5: 22.21}
modes = list(modes_key.keys())


def make_dataset_1():
    tfRange = 21
    versRange = 10
    tdRange = 1301  # 0 to 130 in 0.1 increments
    features = ["mode", "ei", "to", "td", "tf", "vers", "consumption"]
    rows = []
    for modeNum in range(
        1, 6
    ):  # skip private vehicle because it has multiple values for to
        mode = modes[modeNum]
        for vers in range(versRange):
            for tf in range(1, tfRange):
                for tdCount in range(1, tdRange):
                    td = tdCount / 10
                    rows.append(
                        [
                            mode,
                            modes_ei[mode],
                            modes_to[mode],
                            td,
                            tf,
                            vers,
                            calc_trip_consumption(
                                tf, td, modes_to[mode], modes_ei[mode], vers=vers
                            ),
                        ]
                    )
    # do private vehicle now
    mode = modes[0]
    for to in range(1, 6):
        for vers in range(versRange):
            for tf in range(1, tfRange):
                for tdCount in range(1, tdRange):
                    td = tdCount / 10
                    rows.append(
                        [
                            mode,
                            modes_ei[mode],
                            to,
                            td,
                            tf,
                            vers,
                            calc_trip_consumption(
                                tf, td, modes_to[mode], modes_ei[mode], vers=vers
                            ),
                        ]
                    )
    print(f"successfully generated dataset | num_rows: {len(rows)}")
    df2 = pd.DataFrame(rows, columns=features)
    return df2


def make_dataset_2():
    ttRange = 12000  # 120 hours in .01 increments
    versRange2 = 7
    features2 = ["mode", "speed", "fe", "tt", "vers", "consumption"]
    rows2 = []
    for mode2 in range(6):
        for vers2 in range(versRange2):
            for ttCount in range(ttRange):
                tt = ttCount * 0.01
                rows2.append(
                    [
                        mode2,
                        modes2_speed[mode2],
                        modes2_fe[mode2],
                        tt,
                        vers2,
                        calc_trip_consumption_2(
                            tt, modes2_speed[mode2], modes2_fe[mode2], vers=vers2
                        ),
                    ]
                )

    print(f"successfully generated dataset | num_rows: {len(rows2)}")
    df3 = pd.DataFrame(rows2, columns=features2)
    return df3
