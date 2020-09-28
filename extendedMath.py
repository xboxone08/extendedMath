R"""EXTENDED MATH
This module provides some functions to
quickly provide mathematical functions to do
things that would require time to do normally. Find the mean or gcf with a
simple function call that does all that for you.
Although these are probably in numpy, the numpy library is huge, and filled with
stuff that you probably don't need for quick mathematical calculations. This single filed,
native, Python module is small, and copy-pastable. To suggest more functions, please email
me at choudhuryme123@outlook.com!
"""
try:
    print(R"      \  /                                                _____        |||")
    print(R" ___   \/   ___  ___         _   __   _    |\  /|    /\     |    |   | |||")
    print(R"|___   /\    |  |___  |\ |  | \ |__  | \   | \/ |   /__\    |    |———| |||")
    print(R"|___  /  \   |  |___  | \|  |_/ |__  |_/   |    |  /    \   |    |   | (@)")
    print("\nThank you for using extendedMath 0.0.1!\n")


    def gcf(*args) -> int:
        gcd = 1
        while True:
            if all(i % gcd == 0 for i in args):
                return gcd
            gcd += 1


    def lcm(*args) -> int:
        scm = 1  # Stands for 'smallest common multiple', since I can't name it lcm, which is the function name
        while True:
            if all(scm % i == 0 for i in args):
                return scm
            scm += 1


    def mean(*args):
        num = 0
        for aNum in args:
            num += aNum
        # So that it returns 2 instead of 2.0 and 1.3 instead of just 1
        if type(aNum) == float:
            return num / len(args)
        elif type(aNum) == int:
            return num // len(args)


    def mode(*args):
        highest = -2147483647
        vals = dict()
        for item in args:
            vals.update({item: args.count(item)})
        for num in vals:
            if type(highest) != list and vals.get(num) > highest:
                highest = num
            elif type(highest) != list and vals.get(num) == highest and vals.get(num) != -2147483647:
                highest = [highest, num]
            elif type(highest) != list and vals.get(num) == highest and vals.get(num) == -2147483647:
                highest = [num]
            elif type(highest) == list and all(vals.get(num) >= i for i in highest):
                highest.append(num)
        return highest


    def median(*args, **kwargs):
        args = set(args)
        args = list(args)
        args.sort()
        # If float
        if ".5" not in str(len(args) / 2):
            if kwargs.get("oneval", True):
                num = args[len(args) // 2]
                while True:
                    num += 1
                    if num - args[len(args) // 2] == args[len(args) // 2 + 1] - num:
                        return num
            else:
                return args[len(args) // 2], args[len(args) // 2 + 1]
        # If integer
        else:
            return args[len(args) // 2]


except KeyboardInterrupt:
    raise SystemExit
