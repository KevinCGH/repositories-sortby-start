# util function
import os
import sys


def printProgress(iteration, total, prefix='Progress', suffix='Complete', decimals=1, barLength=100):
    """
    Call in a loop to create a terminal progress bar

    Args:
        iteration ([Int]): [current iteration]
        total ([Int]): [total iterations]
        prefix (str, optional): [prefix string]. Defaults to ''.
        suffix (str, optional): [suffix string]. Defaults to ''.
        decimals (int, optional): [positive number of decimals in percent complete]. Defaults to 1.
        barLength (int, optional): [character length of bar]. Defaults to 100.
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration/float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix))
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def import_env():
    if os.path.exists('.env'):
        print('Importing environment from .env...')
    with open('.env') as f:
        for line in f.readlines():
            var = line.strip().split('=')
            if len(var) == 2:
                key, value = var[0].strip(), var[1].strip()
                os.environ[key] = value
    # print(os.environ.get(''))
