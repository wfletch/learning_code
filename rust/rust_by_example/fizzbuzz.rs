fn main() {
    let mut n = 1;
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz!");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 ==0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
        n+=1;
    }
    for n in 1..101 {
        if n % 15 == 0 {
            println!("Fizzbuzz!");
        } else if n % 3 == 0 {
            println!("Fizz");
        } else if n % 5 == 0 {
            println!("Buzz");
        } else {
            println!("{}", n);
        }
    }
}