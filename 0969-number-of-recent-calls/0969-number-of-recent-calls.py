class RecentCounter:

    def __init__(self):
        self.req_time_queue = []

    def ping(self, t: int) -> int:
        self.req_time_queue.append(t)
        count = 1
        for r in self.req_time_queue:
            if t-3000<=r<t:
                count+=1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)