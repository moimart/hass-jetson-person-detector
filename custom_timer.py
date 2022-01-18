class Timer:
    def __init__(self, time, delegate):
        self.delegate = delegate
        self.time = time
        self.elapsed = 0
        self.active = True
        self.payload = None
        self.name = ""

    def step(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.time:
            if self.active:
                self.delegate.on_timer(self, self.elapsed)
            self.elapsed = 0
            self.active = False

    def reset(self):
        self.elapsed = 0
