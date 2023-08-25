function divide
    mem 2 = 0
    mem 1000 = mem 0 == 0
    if mem 1000
        write int 0
    if mem 1000
        jump end0

    negdiv = mem 0 +< 0
    negdis = mem 1 +< 0
    if negdiv
        mem 0 = 0 - mem 0
    if negdis
        mem 1 = 0 - mem 1

    label while0
        mem 1000 = mem 0 < mem 1
        if mem 1000
            jump powhile0
        mem 3 = mem 1
        mem 4 = 1

        label while1
            mem 1001 = mem 3 << 1
            mem 1002 = mem 1001 > 0
            mem 1003 = mem 0 >= mem 1001
            mem 1000 = mem 1002 & mem 1003
            mem 1000 = 1 ^ mem 1000
            if mem 1000
                jump powhile1
            mem 3 = mem 3 << 1
            mem 4 = mem 4 << 1
            jump while1
        label powhile1            

        mem 0 = mem 0 - mem 3
        mem 2 = mem 2 + mem 4    
        jump while0
    label powhile0

    mem 1001 = negdis ^ negdiv
    if mem 1001
        mem 2 = 0 - mem 2

    label end0
    write int mem 2
end


function main
    mem 0 = read int
    mem 1 = 10
	call divide
end
