from time import sleep
from random import randrange, choice
from sys import stderr, stdout

def main():
    options = 2 * ['good'] + ['bad']
    #with open('log.txt', 'w') as f:
    print("print test !!")
    for i in range(10):
        sleep(randrange(1, 3))
        option = choice(options)
        if option == 'good':
            #stdout.write('good\n')
            #stdout.write("테스트")
            print("오 정말 되나되나?")
            stdout.flush()
        else:
            stderr.write('bad\n')
            stderr.flush()
          # f.write(option + '\n')
      #   f.flush()

if __name__ == '__main__':
    main()