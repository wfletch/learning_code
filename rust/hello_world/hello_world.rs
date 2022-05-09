fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    
    let name = "Warren";
    let age = 27;
    println!("{}" , "Hello World!");
    println!("{} {}" , "My Name is", name);
    println!("{} {} {}" , "I am" , age, "years old");
    println!("{} {} {}" , "I am turning", add_one(age), "on the 23rd of July");
}

fn add_one(k: i32) -> i32{
    return k+1;
}

