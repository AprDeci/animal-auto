import random

import actions as ac

action=[ac.keylong_w,ac.keylong_a,ac.keylong_d,ac.keylong_s,ac.press_j,ac.space,ac.press_simulta_aw,ac.press_simulta_dw,ac.press_simulta_sd,ac.press_simulta_sa,ac.press_simulta_spacea]

    #random.shuffle(action)
    # for func in action:
    #     func()
def doaction(action):
    for i in range(1,3):
        next_action = random.choice(action)
        next_action()
