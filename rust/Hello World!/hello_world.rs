fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    
    let name = "Warren";
    println!("{}" , "Hello World!");
    println!("{} {}" , "My Name is", name);
    println!("{} {} {}" , "I am" , 27, "years old");
    println!("{} {} {}" , "I am turning", add_one(27), "on the 23rd of July");
}

fn add_one(k: i32) -> i32{
    return k+1;
}

