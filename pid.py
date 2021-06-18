class PIDController:
    def __init__(self, kp, ki, kd, min_out, max_out, scale=1):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.ep = 0
        self.ed = 0
        self.ei = 0

        self.min = min_out
        self.max = max_out

        self.scale = scale

        self.first_cycle = True

    def get_effort(self, target, current, dt):
        if self.first_cycle:
            self.ep = self.scale * (target - current)
            self.first_cycle = False

        error = self.scale * (target - current)

        self.ed = (error - self.ep) / dt
        self.ep = error
        self.ei += error * dt

        effort = self.kp * self.ep + self.ki * self.ei + self.kd * self.ed

        if effort > self.max:
            effort = self.max

        elif effort < self.min:
            effort = self.min

        return effort


