/*
* CS-499 Milestone Two
* Category: Software design/emgineering, Artifact #1
* Melissa Smith
* Version 1.1
* Created: January 28th, 2024
* Updated: February 11th, 2024
* Purpose: This artifacts purpose was to convert the original Python code into a C++ program. The following program is a text-based 
* adventure game. The player moves through various rooms collecting the item in each room and adding it to their inventory. If the player 
* reaches the room with the Zombie before collecting all 6 items, they lose. If the player reaches the room with the Zombie after
* collecting all 6 items, they win!
*/

// C++ include statements
#include <iostream>
#include <vector>
#include <map>


// The following code creates the function to output the instructions to the player
void showInstructions() {
    std::cout << "Zombie Text Adventure Game" << std::endl;
    std::cout << "Collect 6 items to win the game, or be killed by the zombie." << std::endl;
    std::cout << "Move commands: go South, go North, go East, go West" << std::endl;
    std::cout << "Add to Inventory: get 'item name'" << std::endl;
    std::cout << std::endl;
}

// The following code creates the function to output the players game status
void showStatus(std::string const &cur, std::vector<std::string> &inventory, std::map<std::string, std::map<std::string, std::string>> const &rooms) {

    // Handles valid room inputs
    if (cur == "Bedroom" || cur == "Bathroom" || cur == "Office" || cur == "Entryway" || cur == "Garage" || cur == "Kitchen") {
        const std::string& currentItem = rooms.at(cur).at("item"); // Retrieves the item for the current room
        /*
        * The following code outputs the item in the current room the player is in,
        * as long as it hasn't been retrieved yet, and allows the player to enter
        * input to retrieve the item.
        */
        if (std::find(inventory.begin(), inventory.end(), currentItem) == inventory.end()) {
            std::cout << "You see a " << currentItem << std::endl;
            std::cout << "---------------------------" << std::endl;
            std::cout << "Enter your move:" << std::endl;
            std::string itemInput;
            std::getline(std::cin, itemInput);
            std::vector<std::string> itemInputString;
            size_t pos = 0;
            while ((pos = itemInput.find(' ')) != std::string::npos) {
                itemInputString.push_back(itemInput.substr(0, pos));
                itemInput.erase(0, pos + 1);
            }
            itemInputString.push_back(itemInput);

            // Validates the players input
            if (itemInputString.size() == 2) {
                if (itemInputString[0] == "get") {
                    // Convert the item name to lowercase for case-insensitive comparison
                    std::transform(itemInputString[1].begin(), itemInputString[1].end(), itemInputString[1].begin(), ::tolower);

                    if (itemInputString[1] == currentItem) {
                        inventory.push_back(currentItem);
                        std::cout << currentItem << " retrieved" << std::endl;
                    } else {
                        std::cout << "Invalid input" << std::endl;
                    }
                } else {
                    std::cout << "Invalid input" << std::endl;
                }
            } else {
                std::cout << "Invalid input" << std::endl;
            }
        }
    }
}

/*
* The following code creates the function that validates a players next move
* from the current room they are in.
 */ 
std::string moveRooms(const std::string& curr, const std::string& move) {
    if (curr == "Living Room") {
        if (move == "south") {
            return "Kitchen";
        } else if (move == "north") {
            return "Entryway";
        } else if (move == "east") {
            return "Bedroom";
        } else if (move == "west") {
            return "Office";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Bedroom") {
        if (move == "north") {
            return "Bathroom";
        } else if (move == "west") {
            return "Living Room";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Bathroom") {
        if (move == "south") {
            return "Bedroom";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Office") {
        if (move == "east") {
            return "Living Room";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Entryway") {
        if (move == "south") {
            return "Living Room";
        } else if (move == "east") {
            return "Garage";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Garage") {
        if (move == "west") {
            return "Entryway";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Kitchen") {
        if (move == "north") {
            return "Living Room";
        } else if (move == "east") {
            return "Dining Room";
        } else {
            return "Invalid input";
        }
    } else if (curr == "Dining Room") {
        if (move == "west") {
            return "Kitchen";
        } else {
            return "Invalid input";
        }
    } else {
        return "Invalid";
    }
}

// This is the main function
int main() {
    std::vector<std::string> inventory; // Initial creation of the Inventory vector
    std::map<std::string, std::map<std::string, std::string>> rooms = { // Map of all rooms and their items, along with possible moves and rooms for each
        {"Living Room", {{"south", "Kitchen"}, {"north", "Entryway"}, {"east", "Bedroom"}, {"west", "Office"}}},
        {"Bedroom", {{"north", "Bathroom"}, {"west", "Living Room"}, {"item", "Shield"}}},
        {"Bathroom", {{"south", "Bedroom"}, {"item", "Helmet"}}},
        {"Office", {{"east", "Living Room"}, {"item", "iPad"}}},
        {"Entryway", {{"south", "Living Room"}, {"east", "Garage"}, {"item", "Armor"}}},
        {"Garage", {{"west", "Entryway"}, {"item", "Gun"}}},
        {"Kitchen", {{"north", "Living Room"}, {"east", "Dining Room"}, {"item", "Potion"}}},
        {"Dining Room", {{"west", "Kitchen"}, {"item", "Zombie"}}}
    };

    showInstructions();
    std::string current = "Living Room";

    /*
    * While loop that continuously checks players game status after each move.
    * If player has all 6 items in their inventory and reach the room with the zombie,
    * they win the game.
    * If the player does not have all 6 items and they reach the zombie, they lose.
    * Otherwise, the player continues to enter moves going from room to room
    * collecting items.
    */ 
    while (true) {
        showStatus(current, inventory, rooms);
        // Efficiently uses algorithmic logic to check if the current room is the room containing the zombie
        if (rooms.at(current).at("item") == "Zombie") {
            //Efficiently checking if the player has collected all items is an O(1) operation because it optimizes the stored list length.
            if (inventory.size() == 6) {  // Length check is O(1)
                std::cout << "Congratulations! You have collected all items and defeated the zombie!" << std::endl;
                std::cout << "Thanks for playing the game. Hope you enjoyed it!" << std::endl;
                break;
            } else {
                std::cout << "The zombie got you... GAME OVER!" << std::endl;
                std::cout << "Thanks for playing the game. Hope you enjoyed it!" << std::endl;
                break;
            }
        } else {
            std::string userMove;
            std::cout << "Enter your move:";
            std::getline(std::cin, userMove);
            std::vector<std::string> userMoveSplit;
            size_t pos = 0;
            while ((pos = userMove.find(' ')) != std::string::npos) {
                userMoveSplit.push_back(userMove.substr(0, pos));
                userMove.erase(0, pos + 1);
            }
        }
    }
}