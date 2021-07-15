class Solution:
    def interpret(self, command: str) -> str:
        command = list(command)
        n = len(command)
        for i in range(1, n):
            if command[i - 1] == '(' and command[i] == ')':
                command[i - 1] = ''
                command[i] = 'o'

        for i in range(n):
            if command[i] == '(' or command[i] == ')':
                command[i] = ''

        return ''.join(command)


if __name__ == '__main__':
    command = "G()()()()(al)"
    print(Solution().interpret(command))
