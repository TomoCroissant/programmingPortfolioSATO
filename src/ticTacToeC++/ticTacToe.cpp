//Tic-Tac-Toe | May 22 2023 | Tomo Sato
#include <iostream>
#include <cctype>
using namespace std;

char squares[9] = {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '};
char markSpot; //the placement that the player selects. Value later moved to squares[] after checked that it is valid

//draws board board grid and fills in X's and O's based on squares[]
void drawGameBoard(){
  cout << "\n";
  cout << squares[0] << " | " << squares[1] << " | " << squares[2] << "     1 | 2 | 3\n";
  cout << "---------     ---------\n";
  cout << squares[3] << " | " << squares[4] << " | " << squares[5] << "     4 | 5 | 6\n";
  cout << "---------     ---------\n";
  cout << squares[6] << " | " << squares[7] << " | " << squares[8] << "     7 | 8 | 9\n";
}

//checks if a square is empty: ' '
bool isEmpty(){
  if(squares[(markSpot-'0') - 1] == ' '){
    return true;
  } else {
    return false;
  }
}

bool isWinning(char player){ //player is either "X" or "O". Returns true when a player has a winning pattern
  if(squares[0] == player && squares[1] == player && squares[2] == player) { //top row
    return true;
  } else if(squares[3] == player && squares[4] == player && squares[5] == player) { //middle row
    return true;
  } else if (squares[6] == player && squares[7] == player && squares[8] == player) { //bottom row
    return true;
  } else if (squares[0] == player && squares[3] == player && squares[6] == player) { //left column
    return true;
  } else if (squares[1] == player && squares[4] == player && squares[7] == player) { //middle column
    return true;
  } else if (squares[2] == player && squares[5] == player && squares[8] == player) { //right column
    return true;
  } else if (squares[0] == player && squares[4] == player && squares[8] == player) { // \ diagonal
    return true;
  } else if (squares[2] == player && squares[4] == player && squares[6] == player) { // / diagonal
    return true;
  } else {
    return false;
  }
}

bool isDraw(){
  if(squares[0] != ' ' && squares[1] != ' ' && squares[2] != ' ' && squares[3] != ' ' && squares[4] != ' ' && squares[5] != ' ' && squares[6] != ' ' && squares[7] != ' ' && squares[8] != ' ') {
    return true;
  } else {
    return false;
  }
}


bool inChoiceLoop = true;
bool playing = true;
bool xPlayerTurn = true; //true = X's turn, false = O's turn
bool clear = false;


int main() {
  cout << "Each number on the right-side board correlates to a square on the left-side board. Choose where to place your marks by typing in the corresponding number.\n";

  while(playing == true){
    drawGameBoard();


    //loop that takes in input, checks if valid, updates board values
    while(inChoiceLoop == true) {
      if(xPlayerTurn == true) {
        cout << "\nPlayer 1 (X), pick a square to place your mark: ";
        cin >> markSpot;
      } else {
        cout << "\nPlayer 2 (O), pick a square to place your mark: ";
        cin >> markSpot;
      }

      //checks if a valid input
      if(isdigit(markSpot) != 1) { //checks if number
        cout << "\nInvalid input (not number).\nPlease enter a digit from 1 to 9 that is an empty square.\n";
      } else if(markSpot-'0' > 9 || markSpot-'0' < 1 || isEmpty() == false) { //checks if empty square and number 1-9
        cout << "\nInvalid input (can't place in square).\nPlease enter a digit from 1 to 9 that is an empty square.\n";
      } else {
          inChoiceLoop = false;
      }    
    }
    inChoiceLoop = true; //makes it go into loop next round

    
    //switches whose turn it is and fills in appropriate box
    if(xPlayerTurn == true) {
      squares[(markSpot-'0') - 1] = 'X';
      xPlayerTurn = false;
    } else {
      squares[(markSpot-'0') - 1] = 'O';
      xPlayerTurn = true;
    }

    
    //checks if a player has won, if there is not winner/tie it will clear the console every other turn
    if(isWinning('X')) { //X wins
      playing = false;
      cout << "\n";
      drawGameBoard();
      cout << "\nX wins!\n";
    } else if(isWinning('O')) { //0 wins
      playing = false;
      cout << "\n";
      drawGameBoard();
      cout << "\nO wins!\n";
    } else if(isDraw()) { //draw
      playing = false;
      cout << "\n";
      drawGameBoard();
      cout << "\nIt's a draw!\n";
    } else if(clear == true) { //clears console every other turn
      system("clear");
      clear = false;
    } else {
      clear = true;
    }
  }
  return 0;
}
