# Validator for Chilean RUN (better known as RUT) in Python
*Do you speak another language?
[Spanish](README.md) Todo lo que necesitas saber en Español. 
[German](README_DEU.md)* Alles, was Sie wissen müssen, aber auf Deutsch


<img align="right" src="https://media.giphy.com/media/ehOmuAGboX837Dx9LR/giphy.gif" width="300"/>

## Description
Hello, this little code allows you to validate if a Chilean RUT (Run) (Rol Unico Tributario) is valid. 
The validator not only checks the check digit, but also verifies that the number is within a realistic range to rule out obviously fake RUTs.
This is super useful if you want to add it to a project to give it an extra validation. 

## How do I make it work?
The script asks the user to enter a RUT. It then performs two checks:
1. **Format and Range**: Checks that the RUT is properly formatted and that the number is within a realistic range (by default, from 1,000,000 to 25,000,000).
2. **Verification Digit**: Calculates and verifies the verification digit according to the official algorithm for Chilean RUTs.

## Requirements
- Python
- An editor to run it
- Coffee

## No additional library installation is required to run this script. Just clone the repository and run the main script. 
You don't need to give credits, or anything, but if you can leave me a comment to let me know you're using it you'd make me, Sonic and a kitten very happy.
