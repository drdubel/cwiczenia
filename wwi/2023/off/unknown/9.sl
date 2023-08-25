function dfs(k)
    v = 40000200000 + k
    mem v = 1
    n = 200001 * k
    i = mem 0 + 40000400001
    mem 0 = mem 0 + 1
    mem i = 1
    label while1
        w = mem i > mem n
        if w
            jump powhile1
        ni = n + mem i
        x = mem ni
        write int ni
        write char 10
        v2 = 40000200000 + x
        v3 = mem v2
        ww = v3 ^ 1
        if ww
            call dfs(x)
        mem i = mem i + 1

        jump while1
    label powhile1
    mem 0 = mem 0
end


function msg(x)
    w1 = x == 0
    if w1
        write char 78
    if w1
        write char 73
    if w1
        write char 69
    w2 = x == 1
    if w2
        write char 84
    if w2
        write char 65
    if w2
        write char 75
    write char 10
end


function main
    mem 0 = 1
    n = read int
    m = read int

    label while0
        w = mem 0 > m
        if w
            jump powhile0
        x1 = read int
        x2 = read int
        x3 = x1 * 200001
        mem x3 = mem x3 + 1
        x = x3 + mem x3
        mem x = x2
        mem 0 = mem 0 + 1
        jump while0

    label powhile0
    mem 0 = 0
    call dfs(1)
    mem 0 = 1
    
    label while2
        ww = mem 0 > n
        if ww
            jump powhile2
        v = 40000200000 + mem 0
        call msg(mem v)
        mem 0 = mem 0 + 1
        jump while2

    label powhile2

    mem 0 = mem 0
end
