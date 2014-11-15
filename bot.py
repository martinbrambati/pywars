# Example responses:
#
# Move forwards:
#   return {'ACTION': 'MOVE', 'WHERE': 1}
#
# Move backwards:
#   return {'ACTION': 'MOVE', 'WHERE': -1}
#
# Shooting projectile:
#   return {'ACTION': 'SHOOT', 'VEL': 100, 'ANGLE': 35}
# 'VEL' should be a value x, 0 < x < 150
# 'ANGLE' should be an x, 10 <= x < 90
#
#
# Do nothing:
#   return None
#
# For full API description and usage please visit the Rules section


class EnemyBot(object):

    def __init__(self):
        self.life = 100
        self.position = None


class Bot(object):

    def __init__(self):
        self.next_play = self.shoooot
        self.last_play = None
        self.life, self.prev_life = (100, 100)
        self.feedback = None
        self.enemy = EnemyBot()
        self.vel, self.angle = (100, 35)
        self.increment_angle = {'HOT': 1,
                                'WARM': 2,
                                'MISSING': 3,
                                'COLD': 4
                                }
        self.increment_angle_default = 5

    def moveon(self):
        return {'ACTION': 'MOVE', 'WHERE': 1}

    def move_back(self):
        return {'ACTION': 'MOVE', 'WHERE': -1}

    def shoooot(self):
        return {'ACTION': 'SHOOT', 'VEL': self.vel, 'ANGLE': self.angle}

    def do_nothing(self):
        return None

    def dying(self, life):
        return self.life < self.prev_life

    def get_next_shoot(self, feedback):
        self.angle = self.angle + self.increment_angle.get(feedback['MISSING'],
                                                           self.increment_angle_default)
        self.next_play = self.shoooot

    def get_next_move(self, feedback):
        if feedback['RESULT'] == 'SUCCESS':
            self.enemy.life = self.enemy.life - 1
            self.enemy.position = feedback['POSITION']
            self.next_play = self.last_play
        else:
            self.get_next_shoot(feedback)

    def evaluate_turn(self, feedback, life):
        '''
        :param feedback: (dict) the result of the previous turn,
            ie: for the move action 'SUCCESS' is returned when the enemy
            received a hit, or 'FAILED' when missed the shot.
        {'RESULT': 'SUCCESS' | 'FAILED', Result of the action
         'POSITION': (x, y) | None, In case of move success, or at start
         'MISSING': 'HOT' | 'WARM' | 'COLD' | None, Depending how close the last
         impact was, if applicable }
        :param life: Current life level, An integer between between 0-100.
        :return: see the comments above
        '''
        self.feedback = feedback
        self.life = life

        self.get_next_move(feedback)

        if self.dying(life):
            self.next_play = self.moveon

        self.last_play = self.next_play

        return self.next_play()
