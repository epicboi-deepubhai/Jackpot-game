import random
c = ['@', '?', '#', '$', '!', '1', '2', '3', '4', '5', '00', 'x', ':', '"', '>', '<', '/']
score = 10
ctr = 10
while ctr>0:
    ctr -=1
    score -= 1
    p=input('continue?(y/n)')
    l, m, n = random.choice(c), random.choice(c), random.choice(c)

    if score == 0:
        print('you poor')
        break

    elif p.lower() == 'y':
        print('      ||||      ', l, '|||', m, '|||', n, '      ||||      ')

        if l == '$':
            if m == '$':
                if n == '$':
                    print('|||Mega Jackpot!! |||')
                    score += 1000
                else:
                    print('better luck next time')
        elif l == '$':
            score += 10
            if l == m:
                if l == n:
                    print('jackpot')
                    score += 100
                else:
                    print('cool')
                    score+=30
            elif l == n:
                print('So close :(')

        elif n == '!':
            score += 8
            if n == m:
                if n == l:
                    print('jackpot')
                else:
                    print('nice!')
                    score += 50
            elif n == l:
                print('So close :(')

        elif m == '#':
            score += 6
            if m == l:
                if m == n:
                    print('jackpot')
                else:
                    print('cool')
                    score += 30
            elif m == n:
                print('nice')
                score += 50

        elif l == m:
            if l == n:
                print('jackpot')
                score += 100
            else:
                print('cool')
                score += 30
        elif m == n:
            print('nice!')
            score += 50
        elif n == l:
            print('So close :(')
        else:
            print('better luck next times')

    elif p == 'n':
        break

    else:
        print('Please input a valid option')
        score += 1
    print(score)
