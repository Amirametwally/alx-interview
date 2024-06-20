#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics"""

if __name__ == "__main__":

    def printer(file_size, status):
        """Print logs"""

        print("File size: {:d}".format(file_size))
        for i in sorted(status.keys()):
            if status[i] != 0:
                print("{}: {}".format(i, status[i]))

    file_size = 0
    status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    count = 0
    try:
        with open(0) as f:
            for line in f:
                count += 1
                data = line.split()

                try:
                    file_size += int(data[-1])
                except Exception:
                    pass

                try:
                    st = data[-2]
                    if st in status:
                        status[st] += 1

                except Exception:
                    pass
                if count % 10 == 0:
                    printer(file_size, status)
            printer(file_size, status)
    except KeyboardInterrupt:
        printer(file_size, status)
        raise
