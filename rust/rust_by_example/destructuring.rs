fn main() {
    let triple = (1,2,3);
    println!("Tell me about {:?}", triple);
    match triple {
        (1, y, z) => println!("First is 1, then {:?}, followed by {:?}", y, z),
        (0, ..) => println!("First is 0, the rest don't matter"),
        _ => println!("It does not matter!"),
    }
}