from callREST import *
from dynamicHyper import *
from swapandpublish import *
from mapfields import *

'''

# todo #
datetime.datetime.utcfromtimestamp(var)?
commenting best practices

'''

def main():
    url = getArguments()
    apikeys = createdict()
    forhyper = getREST(url, apikeys)
    extract_table = build_table(apikeys)
    build_hyper(forhyper, build_table(apikeys), gethypername())
    swap_hyper()
    #publishtoserver()
    print("It is complete.")


# run
if __name__ == '__main__':
    main()