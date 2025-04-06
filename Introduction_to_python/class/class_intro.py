class A:
    def __init__(self, value):
        value = 3
        self.value = value

    def change(self):
        self.value = 12

ans = []
a = A(13)
ans.append(a.value)    # value = 13
a.change()             # value changes to 12
ans.append(a.value)    # value = 12
print(ans)
