fn main() {
    let mut count = 0u32;
    loop {
        count +=1;
        if count == 3 {
            println!("Hello!, We are at three");
            continue
        }
        println!("Count: {}", count);
        if count == 5{
            println!("We are done");
            break;
        }
    }
}