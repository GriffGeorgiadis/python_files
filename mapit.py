import webbrowser, sys

sys.argv

if len(sys.argv) > 1:
    print('args were passed')
    address = ' '.join(sys.argv[1:])
else:
    

