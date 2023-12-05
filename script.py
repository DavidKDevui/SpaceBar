
import time
from func import * 

def main():
    try:
        while True:
            iteration()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nArrêt du programme.")

if __name__ == "__main__":
    main()
 