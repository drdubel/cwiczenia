function add(x)
    mem x = 1
end


function check(x)
    exist = mem x == 1
    if exist
        write int 1

    notexist = mem x == 0
    if notexist
        write int 0
    
    write char 10
end


function remove(x)
    mem x = 0
end


function main
    n = read int
    i = 1000
    mem i = 0
    label loop0
        isend0 = mem i >= n
        if isend0
            jump end0
        op = read int
        arg = read int
        isone = op == 1
        if isone
            call add(arg)

        istwo = op == 2
        if istwo
            call check(arg)
    
        isthree = op == 3
        if isthree
            call remove(arg)

        mem i = mem i + 1
        jump loop0
    
    label end0
    mem 0 = mem 0

end
