function swap(a b)
    mem 2000 = mem a
    mem a = mem b
    mem b = mem 2000
end


function gcd
    mem 2 = 0
    
    label while0
        mem 1001 = mem 0 & 1
        mem 1002 = mem 1 & 1
        mem 1003 = mem 1001 | mem 1002
        mem 1000 = mem 1003 != 0
        if mem 1000
            jump powhile0
        mem 0 = mem 0 >> 1
        mem 1 = mem 1 >> 1
        mem 2 = 1 + mem 2
        jump while0
    
    label powhile0
    mem 0 = mem 0
    
    label while1
        mem 1001 = mem 0 & 1
        mem 1000 = mem 1001 != 0
        if mem 1000
            jump powhile1
        mem 0 = mem 0 >> 1
        jump while1
    
    label powhile1
    mem 0 = mem 0
  
    label while2
        mem 1000 = mem 1 == 0
        if mem 1000
            jump powhile2

        label while3
            mem 1001 = mem 1 & 1
            mem 1000 = mem 1001 != 0
            if mem 1000
                jump powhile3
            mem 1 = mem 1 >> 1
            jump while3
        
        label powhile3
        mem 1000 = mem 0 > mem 1
        if mem 1000
            call swap(0 1)
        mem 1 = mem 1 - mem 0
        jump while2
    
    label powhile2
    res = mem 0 << mem 2
    write int res
end


function main
    mem 0 = read int
    mem 1 = read int
    call gcd
end
