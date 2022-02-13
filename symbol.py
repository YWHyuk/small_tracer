import time
import argparse
from subprocess import check_output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--pid', required=True)
    parser.add_argument('--addr1', required=True)
    parser.add_argument('--addr2', required=True)
    args = parser.parse_args()

    pid = args.pid
    with open('/proc/{0}/maps'.format(pid), "rb") as f:
        lines = f.readlines()
        text_section = lines[0].split(b" ")[0]
        start, end = text_section.split(b"-")[0:2]

        start, end = int(start, 16), int(end, 16)
        addr1 = int(args.addr1,16)
        addr2 = int(args.addr2,16)

        #print(pid, hex(start), hex(end))
        #print(hex(addr1), hex(addr2))

        result1 = check_output(["addr2line", "-f", "-e", "/proc/{0}/exe".format(pid), "-a", (hex(addr1-start))]).split(b"\n")[1]
        result2 = check_output(["addr2line", "-f", "-e", "/proc/{0}/exe".format(pid), "-a", (hex(addr2-start))]).split(b"\n")[1]
        print("[{0}] {1}[{2}] <= {3}[{4}]".format(time.time_ns(), result1.decode(), hex(addr1), result2.decode(), hex(addr2)))
