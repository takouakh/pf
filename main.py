import gevent
import sys, traceback
from configuration import Configuration
from insteon import Insteon
from pocket_sphinx_listener import PocketSphinxListener
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
 GPIO.setup(11,GPIO.OUT)
 GPIO.setup(13,GPIO.OUT) 
GPIO.setup(15,GPIO.OUT)

gevent.monkey.patch_all()
pocketSphinxListener = PocketSphinxListener()
 while True:
        try:
            command = pocketSphinxListener.getCommand().lower()

            if commandn  == AVANCE 
                print('marche avant') 
 GPIO.output(7,True) 
GPIO.output(15,True)
 time.sleep(3)
                    
            elif command == RECULE 
print('marche arriere')
 GPIO.output(11,False)
 GPIO.output(13,False)
 time.sleep(3)
elif command == DROITE
GPIO.output(7,False) 
GPIO.output(13,True) 
GPIO.output(11,True)
 GPIO.output(15,False)
 time.sleep(3)
elif command == GAUCHE
print('gauche') GPIO.output(7,True)
 GPIO.output(13,False)
 GPIO.output(11,False) 
GPIO.output(15,True) 
time.sleep(3)
elif command == STOP 
print('stop') 
GPIO.output(7,False)
GPIO.output(13,False)
 GPIO.output(11,False) 
GPIO.output(15,False) 
time.sleep(3)
GPIO.cleanup()

{}
  gevent.sleep(1)

        except (KeyboardInterrupt, SystemExit):
            print 'People sometimes make mistakes, Goodbye.'
            sys.exit()
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback,
                                      limit=2,
                                      file=sys.stdout)
            sys.exit()


if __name__ == '__main__':
    runMain()
