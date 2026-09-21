# Structured Programming Adventure Game

Create a text-based adventure game in Python. Your game will use a **state machine** to move the player between different rooms or locations. You may choose any theme you want, such as fantasy, science fiction, mystery, school, survival, comedy, or something completely original.

Whenever the player enters a room, the program should provide a brief description of the location and present the actions that are currently available. The player will interact with the game by entering text commands or selecting from a numbered list of choices.

For example:

```text
You enter a dark storage room. A locked cabinet sits against the wall.

What would you like to do?
1. Search the room
2. Return to the hallway
```

As the player completes actions, the game should remember what has happened and change accordingly.

## Project Requirements Checklist

### Game Structure

* [ ] Your game uses a **state machine** to keep track of the player's current room or location.
* [ ] Your game contains **at least 10 different rooms or locations**.
* [ ] The rooms are connected in a **non-linear layout**. The player must have choices about where to travel rather than simply moving through rooms in one fixed order.
* [ ] Each room provides a clear description when the player enters it.
* [ ] Each room provides the player with appropriate actions or choices.
* [ ] The player can move between rooms using text input.
* [ ] Your game has a clear objective and a clear ending.
* [ ] The player can successfully complete or win the game.

### Tracking Game Information

* [ ] Your program uses **at least 6 variables** to keep track of information about what has happened in the game.
* [ ] These variables affect what the player can see, do, or access later in the game.

Possible information to track could include:

* Whether a door has been unlocked.
* Whether an enemy has been defeated.
* Whether an item has been collected.
* Whether treasure has already been taken.
* Whether a puzzle has been solved.
* Whether the player has discovered important information.

### Changing Choices

* [ ] The available choices in a room change when appropriate based on what has already happened.
* [ ] Actions that can only happen once are removed or changed after they are completed.

For example, if the player chooses to take a key, the game should remember that the key has been taken. Returning to the room should no longer give the player the option to take the same key again.

### Challenge or Obstacle

* [ ] Your game includes **at least one obstacle that requires the player to provide a specific input before they can continue**.
* [ ] The obstacle must require the player to discover, calculate, remember, or determine the correct answer.
* [ ] Successfully completing the obstacle must affect the state of the game.

Examples could include calculating the answer to a problem given by a character, discovering a password in another room, finding a code that opens a locked door, or collecting information needed to answer a question later.

### User Input and Output

* [ ] The program clearly explains what is happening to the player.
* [ ] The player is given clear instructions about what they can enter.
* [ ] The program **validates all user input before using it**.
* [ ] Invalid input does not cause the program to crash.
* [ ] Invalid input provides useful feedback and allows the player to try again.
* [ ] The game should be **error-proof during normal gameplay**.

### Structured Programming

Your program must demonstrate a clear understanding of the three major control structures used in structured programming:

* [ ] **Sequence:** Instructions are organized in a logical order so that actions happen at the correct time.
* [ ] **Selection:** `if`, `elif`, and `else` statements are used to make decisions based on user choices and the current state of the game.
* [ ] **Iteration:** Loops are used appropriately to repeat gameplay and/or validate user input.
* [ ] **Functions:** Functions are used to organize the program into manageable sections and avoid unnecessary repeated code.

## Creativity

The requirements above describe the minimum functionality your game must include. Everything else is up to you.

You are encouraged to create your own setting, characters, story, puzzles, obstacles, items, secrets, and game mechanics. Your game can be serious, funny, strange, challenging, story-focused, or anything else you would enjoy creating, as long as it meets all of the project requirements.

CSE 1110 - Structured Programming 1

| Outcome                                 | Excellent                                                                                                                                                                                            | Proficient                                                                                                                                                       | Developing                                                                                                                                             | Emerging                                                                                                                                             |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input and Output                        | Program uses input and output effectively throughout the game, with clear prompts and highly effective feedback that makes the game easy to understand and navigate.                                 | Program uses user input appropriately and consistently displays clear, relevant output that communicates the state of the game.                                  | Program generally uses user input and output appropriately, but some interactions may be unclear or inconsistent.                                      | Program uses user input or displays output, but input/output may be incomplete, unclear, or inappropriate for the game.                              |
| Variables and Data Types                | Program uses variables and data types deliberately and efficiently, with clear variable names and effective choices for representing different kinds of game information.                            | Program uses appropriate variables and data types to store and process the information needed by the game.                                                       | Program uses variables to store game information, but variable choices, data types, or usage may sometimes be inefficient or unclear.                  | Program uses few variables, or variables are used incorrectly or do not effectively represent game information.                                      |
| Sequence Control Structures             | Program demonstrates strong control over sequence, with functions and instructions organized into a clear, intentional, and easy-to-follow program flow.                                             | Program is effectively structured so instructions execute in a clear and logical sequence.                                                                       | Program generally follows a logical sequence, but some sections could be organized more effectively.                                                   | Program execution is difficult to follow or instructions frequently occur in an inappropriate order.                                                 |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements                    | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the game.                                           | All requirements outlined in the project description are successfully implemented.                                                                               | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently.                                      | Several major requirements from the project description are missing or incomplete.                                                                   |

CSE 1120 - Structured Programming 2

| Outcome                                 | Excellent                                                                                                                                                                                            | Proficient                                                                                                                                                       | Developing                                                                                                                                             | Emerging                                                                                                                                             |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Input Validation                        | Program consistently and efficiently validates input throughout the game, providing clear feedback and allowing the player to recover easily from invalid entries.                                   | Program validates user input before continuing and handles invalid input without crashing or producing unexpected behaviour.                                     | Program validates some user input, but validation may be inconsistent or may not account for all expected invalid inputs.                              | User input is frequently used without validation, and invalid input may cause errors or unexpected behaviour.                                        |
| Selection Control Structures            | Program uses selection control structures deliberately and efficiently to manage complex game decisions and changing game states while keeping the code clear and understandable.                    | Program effectively uses selection control structures to make decisions based on user input and the current state of the game.                                   | Program uses `if`, `elif`, and/or `else` structures appropriately in most situations, but some decisions may be inefficient or unclear.                | Selection structures are missing, frequently incorrect, or do not effectively control program behaviour.                                             |
| Iteration Control Structures            | Program uses iteration control structures deliberately and efficiently, minimizing unnecessary repetition while maintaining clear and predictable program flow.                                      | Program effectively uses iteration control structures to manage repeated gameplay, input validation, and other repeated processes.                               | Program uses loops for some appropriate tasks, but iteration may be inconsistent, inefficient, or unnecessarily repetitive.                            | Loops are missing, frequently incorrect, or do not effectively control repeated program behaviour.                                                   |
| Python Best Practices and Documentation | Code consistently follows Python best practices and is exceptionally clear and maintainable. Type hints, docstrings, naming, formatting, and other documentation are accurate and useful throughout. | Code follows appropriate Python best practices. Functions use appropriate type hints and docstrings, and names and comments make the program easy to understand. | Code follows some Python conventions and includes some useful documentation, but documentation, type hints, docstrings, or naming may be inconsistent. | Code frequently does not follow Python conventions and has little or missing documentation. Type hints and/or docstrings are missing from functions. |
| Project Requirements                    | All project requirements are successfully implemented, with features developed beyond the minimum requirements in ways that meaningfully improve the game.                                           | All requirements outlined in the project description are successfully implemented.                                                                               | Most project requirements are present, but one or more requirements are incomplete or implemented inconsistently.                                      | Several major requirements from the project description are missing or incomplete.                                                                   |

