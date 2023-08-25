function main
    n = 21372137
    mem 1 = 9223372036854775807
    mem 1 = 0 - mem 1
    mem 1 = mem 1 - 1
    mem n = read int
    label nloop
    mem 0 = read int
    w1 = mem 0 +> mem 1
    if w1
        mem 1 = mem 0
    mem n = mem n - 1
    w2 = mem n != 0
    if w2
        jump nloop
    write int mem 1

end
