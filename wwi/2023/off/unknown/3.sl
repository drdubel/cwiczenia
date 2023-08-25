function swap(a b)
    mem 4 = mem a
    mem a = mem b
    mem b = mem 4
    end


function main
    mem 0 = read int
    mem 1 = read int
    mem 2 = read int

    mem 3 = mem 0 +> mem 1
    if mem 3 call swap(0 1)
    
    mem 3 = mem 1 +> mem 2
    if mem 3 call swap(1 2)
    
    mem 3 = mem 0 +> mem 1
    if mem 3 call swap(0 1)

    write int mem 0
    write char 32
    write int mem 1
    write char 32
    write int mem 2

    end
