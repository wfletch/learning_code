fn main() {
    println!("{}", fib(42));
}

fn fib(k: i32) -> i64 {
    // Space O(1)
    // Time O(n)
    let mut fib: [i64;2] = [1,1];
    if k == 0 {
        return 0;
    }
    else if k <= 2{
        return 1;
    }
    for _i in 3..=k {
        // TODO: Replace this with XOR to avoid temp Variable
        let temp = fib[0];
        fib[0] = fib[0] + fib[1];
        fib[1] = temp;
    }
    return fib[0]
}
