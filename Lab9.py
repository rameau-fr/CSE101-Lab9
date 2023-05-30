# Import your dependencies
import matplotlib.pyplot as plt
import random
import landscape

# Define a Sled class
class Sled:
    def __init__(self, name, speed):
        """
        Initialize a new sled with a name and speed.
        Args:
            name (str): The name of the sled.
            speed (float): The speed of the sled.
        """
        # TODO: Implement this function
        ...
    
    def move(self):
        """
        Move the sled according to the gradient of the landscape and its speed.
        Here you have to use your function slope from your module landspace!
        """
        # TODO: Implement this function
        ...
    
    def found_treasure(self, treasure_position, threshold):
        """
        Check if the sled has found the treasure.
        Args:
            treasure_position (float): The position of the treasure.
            threshold (float): The distance within which the sled is considered to have found the treasure.   
        Returns:
            bool: True if the sled found the treasure, False otherwise.
        """
        # TODO: Implement this function 
        ...

def main():
    # Plot the landsapce
    x = [i/10 for i in range(-100, 100)] 
    y = [landscape.elevation(i) for i in x]
    plt.plot(x, y, label='Landscape')
    plt.xlabel("position")
    plt.ylabel("elevation")
    
    # Instantiate 3 sleds with different speeds
    Joe = Sled("Joe", 0.05)
    Jack = Sled("Jack", 0.1)  
    John = Sled("John", 0.08)

    # Define threshold and treasure_position
    thresh_treas = 0.05
    treasure_position = -1.3

    # Make the sleds race for maximum 60 "minutes"
    winner = "nobody"
    for _ in range(60):
        # Move each sled
        # TODO: Move all the sled once!

        # Plot the position of all the sled
        plt.plot(Joe.position, landscape.elevation(Joe.position), "og")
        plt.plot(Jack.position, landscape.elevation(Jack.position), "ob")
        plt.plot(John.position, landscape.elevation(John.position), "or")

        # Check if a sled found the treasure
        # TODO: CHECK IF THE SLED FOUND THE TREASURE GIVEN THE THREHSOLD!!

    # Print the winner
    print(winner, "is winning")

    # Show the final result
    plt.legend()
    plt.show()

# Execute the main function
if __name__ == "__main__":
    main()
