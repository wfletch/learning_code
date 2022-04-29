fn main() {
    let k = 5;
    let n = {
        if k  == 5 {
            10 * 10
        } else {
            50 * 10
        }
    };
    println!("The Value of N is {}, when k is {}", n, k);
}