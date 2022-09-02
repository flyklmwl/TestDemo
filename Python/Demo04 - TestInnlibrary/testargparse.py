import argparse


def test():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--timer_name", help="timer name")
    parser.add_argument("-p", "--project", help="project name")
    args = parser.parse_args()

    print("-t:%s" % args.timer_name)
    print('-p:%s' % args.project)


if __name__ == '__main__':
	test()