from pocket_sphinx_listener import PocketSphinxListener
import sys

def runMain():
    # Now we set up the voice recognition using Pocketsphinx from CMU Sphinx.
    # We can set debug for the listener here to see messages directly from Pocketsphinx
    pocketSphinxListener = PocketSphinxListener(debug=False)

    while True:
        try:
            # We can set debug here to see what the decoder thinks we are saying as we say it
            command = pocketSphinxListener.getCommand(debug=False).lower()
    
        # Exit when control-c is pressed
        except (KeyboardInterrupt, SystemExit):
            print 'People sometimes make mistakes, Goodbye.'
            sys.exit()    
    
if __name__ == '__main__':
    runMain()
