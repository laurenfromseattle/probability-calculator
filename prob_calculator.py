import copy
import random
# Consider using the modules imported above.

class Hat:
    '''Create an instance of the class Hat.'''

    def __init__(self, **kwargs):
        '''Initialize the attributes of the instance.'''
        self.contents = []
        for color, number in kwargs.items():
            self.contents.extend([color] * number)

    def draw(self, draw_count):
        '''Return a list of strings representing balls randomly drawn 
        from a hat, with the `draw_count` parameter determining how many 
        balls to draw.
        '''
        ball_count = len(self.contents)
        balls_left = copy.copy(self.contents)
        balls_drawn = []
        draw = 1
        while draw <= draw_count:
            if draw > ball_count : break
            ball = random.choice(balls_left)
            balls_left.remove(ball)
            balls_drawn.append(ball)
            draw += 1
        return balls_drawn
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # create list with the balls be expect to see
    expectation = []
    for color, number in expected_balls.items():
        expectation.extend([color] * number)
    # run experiment N times to compare expected to actual
    # and keep count of how many times we get expected
    experiment_success_count = 0
    for experiment in range(num_experiments):
        # draw and get list of drawn balls
        result = hat.draw(num_balls_drawn)
        # is each expected ball in the result?
        ballmatch_count = 0
        for ball in expectation:
            if ball in result:
                result.remove(ball)
                ballmatch_count += 1
            else:
                break
        if ballmatch_count == len(expectation):
            experiment_success_count += 1
    # return probability
    return experiment_success_count / num_experiments
