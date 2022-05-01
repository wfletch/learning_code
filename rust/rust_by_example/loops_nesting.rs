#![allow(unreachable_code)]
#![allow(unused_labels)]
fn main(){
    let mut count = 0u32;
    println!("Starting Here!");
    count = 'outer : loop {
        count+=1;
        'inner: loop {
            break 'outer count * 10;
            println!("We will never get here!");
        }
    };
    println!("Done! {}", count);
}