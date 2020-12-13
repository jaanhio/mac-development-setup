import subprocess

opts = (
            ['brew path', 'cask', 'install', 'command']
            + list()
            + ['current cask']
        )

print(opts)

cmd = [opt for opt in opts if opt]

print(cmd)
# args = [to_bytes(x, errors='surrogate_or_strict') for x in cmd if x is not None]

foo = [1, 2, None, 3]



def addOne(i):
    print(i)
    return i + 1

bar = [addOne(i) for i in foo if i]
print(bar)

commands = ['/usr/local/Homebrew/bin/brew', 'ls']
subprocess.run(commands)

