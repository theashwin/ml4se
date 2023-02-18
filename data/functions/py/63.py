def free_memory(self):
        """Free memory signal."""
        self.main.free_memory()
        QTimer.singleShot(self.INITIAL_FREE_MEMORY_TIME_TRIGGER,
                          lambda: self.main.free_memory())
        QTimer.singleShot(self.SECONDARY_FREE_MEMORY_TIME_TRIGGER,
                          lambda: self.main.free_memory())