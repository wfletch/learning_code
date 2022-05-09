fn main() {
    let array = [0,2,3];
    match array {
        // Must match 0 and then second and third. This is quite nice!
        [0, second, third] => 
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),
        [first, middle @.., last] =>
            println!("array[0] = {}, middle = {:?}, array[2] = {}", first, middle, last)
    }
}