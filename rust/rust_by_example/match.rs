fn main() {
for number in 1..101 {
    println!("Let's Do This!");
    match number {
        1 => println!("One!"),
        2 | 3 | 5 | 7 | 11 => println!("Prime Number!"),
        13..=19 => println!("Teens!"),
        _ => println!("Ain't Nothing Special! But this kind of match is intersting!"),
    }
}   
let condition = true;
let k = match condition {
    true => 1,
    false => 0,
    _ => -1,
};
    println!("{}", k);
}