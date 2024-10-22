class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            if operation == "../":
                if stack:
                    stack.pop()
            elif operation == "./":
                continue
            else:
                print(operation)
                stack.append(operation)
        return len(stack)
