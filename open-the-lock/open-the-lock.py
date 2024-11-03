from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = deque([("0000",0)]) #status and turns
        visited = set("0000")
        while queue:
            curr_status,turns = queue.popleft()
            if curr_status == target:
                return turns
            for i in range(4):
                for move in (-1,1):
                    new_wheel = (int(curr_status[i])+move)%10
                    new_status = curr_status[:i]+str(new_wheel)+curr_status[i+1:]
                    if new_status not in deadends and new_status not in visited:
                        visited.add(new_status)
                        queue.append((new_status,turns+1))
        return -1
                    