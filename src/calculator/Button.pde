class Button {
  // Member Variables
  int x, y, w, h; //button dimensions
  char val; //what symbol does the button represent (1, 2, +, -, etc)
  color c1, c2; //static color vs when clicked/hover color
  boolean overButton; //is the mouse over the button?

  // Constructor
  Button(int x, int y, int w, int h, char val, color c1) { //button values
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.val = val;
    this.c1 = c1;
    c1 = color(0);
    c2 = color(2, 87, 154);
    overButton = false;
  }

  void display() {
    if (overButton) {
      fill(c2);
    } else {
      fill(c1);
    }
    //noStroke();
    stroke(28, 98, 172);
    strokeWeight(2);
    rect(x, y, w, h);
    fill(255);
    textAlign(CENTER);
    textSize(23);
    fill(250);
    if (val == 'A') { //exponent
      text("x²", x + w/2, y + h/2 + 7);
    } else if (val == 'B') { //square root
      text("√", x + w/2, y + h/2 + 8);
    } else if (val == '!') { //factorial
      text("x!", x + w/2, y + h/2 + 8);
    } else if (val == 'R') { //x to power of y
      text("xʸ", x + w/2, y + h/2 + 8);
    } else {
      text(val, x + w/2, y + h/2 + 6);
    }
  }

  void hover(int mX, int mY) { //when is mouse over button
    overButton = (mX > x && mX < x+w && mY > y && mY < y+h);
  }
}
