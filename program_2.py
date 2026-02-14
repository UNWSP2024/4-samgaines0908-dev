# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    total_tickets = 0
    while True:
        movie_name = input("Enter movie name(or type 'done' when finished): ")
        if movie_name == 'done':
            break
        try:
           tickets = input(f"how many tickets for {movie_name}? ")
           total_tickets=total_tickets+int(tickets)
        except ValueError:
            print("Please enter a correct number of tickets")
    print(f"total number of tickets desired {total_tickets}: ")

    ######################


if __name__ == '__main__':
    main()
