import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball_color, ball_num in balls.items():
            for i in range(ball_num):
                self.contents.append(ball_color)
    
    def draw(self, num_balls):
        drawn_balls = []
        if num_balls > len(self.contents):
            return self.contents
        for i in range(num_balls):
            choice = random.choice(self.contents)
            drawn_balls.append(choice)
            self.contents.pop(self.contents.index(choice))
        return drawn_balls
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_possible_outcomes = 0

    for i in range(num_experiments):
        copied_hat = copy.deepcopy(hat)

        drawn_balls = copied_hat.draw(num_balls_drawn)
        drawn_balls_contents = {ball: drawn_balls.count(ball) for ball in set(drawn_balls)}
        result = True
        for key in expected_balls.keys():
            if key not in drawn_balls_contents or drawn_balls_contents[key] < expected_balls[key]:
                result = False
                break

        if result:
            num_possible_outcomes += 1
    
    probability = num_possible_outcomes/num_experiments
    
    return probability
