// Tomo Sato | Nov 2022 | Calculator Project //<>//
Button[] numButtons = new Button[10]; //number buttons
Button[] opButtons = new Button[12]; //others

//for calculations
String dVal = "0.0"; //display value (default 0)
boolean left = true;
float l, r, result;
char op = ' ';

//for colors
color numbers = color(21, 127, 139); //default color for numbers
color basicOperators = color(3, 130, 208); //default color for +, -, X, ÷
color others = color(28, 146, 199); //the rest
color displayColor = color(54, 128, 190);
color numbers2, basicOperator2, others2; //when hover (may or may not implement)

//for factorial
int minusCount; //tracks how many times and what numbers were multiplied before getting to 0
boolean factFinish = false; //boolean that says when to break the while loop (calculation finished)


String displayOp = " ";


void setup() {
  size(360, 310);
  //number buttons
  numButtons[0] = new Button(60, 250, 60, 60, '0', numbers);
  numButtons[1] = new Button(60, 190, 60, 60, '1', numbers);
  numButtons[2] = new Button(120, 190, 60, 60, '2', numbers);
  numButtons[3] = new Button(180, 190, 60, 60, '3', numbers);
  numButtons[4] = new Button(60, 130, 60, 60, '4', numbers);
  numButtons[5] = new Button(120, 130, 60, 60, '5', numbers);
  numButtons[6] = new Button(180, 130, 60, 60, '6', numbers);
  numButtons[7] = new Button(60, 70, 60, 60, '7', numbers);
  numButtons[8] = new Button(120, 70, 60, 60, '8', numbers);
  numButtons[9] = new Button(180, 70, 60, 60, '9', numbers);

  //special and op buttons
  opButtons[0] = new Button(300, 190, 60, 120, '=', others);
  opButtons[1] = new Button(240, 250, 60, 60, '+', basicOperators);
  opButtons[2] = new Button(240, 190, 60, 60, '-', basicOperators);
  opButtons[3] = new Button(240, 130, 60, 60, 'x', basicOperators);
  opButtons[4] = new Button(300, 130, 60, 60, '÷', basicOperators);
  opButtons[5] = new Button(240, 70, 120, 60, 'C', others);
  opButtons[6] = new Button(120, 250, 60, 60, '.', others);
  opButtons[7] = new Button(180, 250, 60, 60, '±', others);
  opButtons[8] = new Button(0, 70, 60, 60, 'A', others); //exponent
  opButtons[9] = new Button(0, 130, 60, 60, 'B', others); //square root
  opButtons[10] = new Button(0, 190, 60, 60, 'R', others); //to power
  opButtons[11] = new Button(0, 250, 60, 60, '!', others); //factorial
}

void draw() {
  background(displayColor); //color of display
  for (int i = 0; i < numButtons.length; i++) {
    numButtons[i].display();
    numButtons[i].hover(mouseX, mouseY);
  }

  for (int i = 0; i < opButtons.length; i++) {
    opButtons[i].display();
    opButtons[i].hover(mouseX, mouseY);
  }

  updateDisplay();

  textSize(23);
  textAlign(LEFT);
  text(displayOp, 5, 21); //shows operator selected in top right
}


void keyPressed() {
  println("key: " + key);
  println("keyCode:" + keyCode);
  if (keyCode == 49 || keyCode == 97) {
    handleEvent("1", true);
  } else if  (keyCode == 50 || keyCode == 98) {
    handleEvent("2", true);
  } else if  (keyCode == 51 || keyCode == 99) {
    handleEvent("3", true);
  } else if  (keyCode == 52 || keyCode == 100) {
    handleEvent("4", true);
  } else if  (keyCode == 53 || keyCode == 101) {
    handleEvent("5", true);
  } else if  (keyCode == 54 || keyCode == 102) {
    handleEvent("6", true);
  } else if  (keyCode == 55 || keyCode == 103) {
    handleEvent("7", true);
  } else if  (keyCode == 56 || keyCode == 104) {
    handleEvent("8", true);
  } else if  (keyCode == 57 || keyCode == 105) {
    handleEvent("9", true);
  } else if  (keyCode == 48 || keyCode == 96) {
    handleEvent("0", true);
  } else if (keyCode == 46 || keyCode == 110) {
    handleEvent(".", false);
  } else if (keyCode == 67 || keyCode == 12 || keyCode == 8) { //c, clear, delete
    handleEvent("C", false);
  } else if (keyCode == 61 || keyCode == 107) {
    handleEvent("+", false);
  } else if (keyCode == 10) { //enter
    handleEvent("=", false);
  } else if (keyCode == 45 || keyCode == 109) {
    handleEvent("-", false);
  } else if (keyCode == 88 || keyCode == 106) {
    handleEvent("x", false);
  } else if (keyCode == 47 || keyCode == 111) { // /
    handleEvent("÷", false);
  } else if (keyCode == 16) { //shift
    handleEvent("±", false);
  } else if (keyCode == 83) { //s
    handleEvent("A", false);
  } else if (keyCode == 82) { //r
    handleEvent("B", false);
  } else if (keyCode == 80) { //p
    handleEvent("R", false);
  } else if (keyCode == 70) { //f
    handleEvent("!", false);
  }
}


void handleEvent(String val, boolean num) {
  if (num && dVal.length() < 25) {
    if (dVal.equals("0.0")) {
      dVal = val;
    } else {
      dVal += val;
    }

    if (left) {
      l = float(dVal);
    } else {
      r = float(dVal);
    }
  } else if (val.equals("C")) {
    dVal = "0.0";
    left = true;
    l = 0.0;
    r = 0.0;
    result = 0.0;
    op = ' ';
    displayOp = " ";
  } else if (val.equals(".")) {
    if (!dVal.contains(".")) {
      dVal += ".";
    }
  } else if (val.equals("+")) {
    op = '+'; //sets op to val
    displayOp = "+";
    dVal = "0.0";
    left = false;
  } else if (val.equals("=")) {
    performCalculation();
  } else if (val.equals("-")) {
    op = '-';
    displayOp = "-";
    dVal = "0.0";
    left = false;
  } else if (val.equals("x")) {
    op = 'x';
    displayOp = "x";
    dVal = "0.0";
    left = false;
  } else if (val.equals("÷")) {
    op = '÷';
    displayOp = "÷";
    dVal = "0.0";
    left = false;
  } else if (val.equals("±")) {
    if (left) {
      l = l * -1;
      dVal = str(l);
    } else {
      r = r * -1;
      dVal = str(r);
    }
  } else if (val.equals("A")) {
    if (left) {
      l = sq(l);
      dVal = str(l);
    } else {
      r = sq(r);
      dVal = str(r);
    }
  } else if (val.equals("B")) {
    if (left) {
      l = sqrt(l);
      dVal = str(l);
    } else {
      r = sqrt(r);
      dVal = str(r);
    }
  } else if (val.equals("R")) {
    op = 'ʸ';
    displayOp = "xʸ";
    dVal = "0.0";
    left = false;
  } else if (val.equals("!")) {
    if (left) {
      l = factorial(int(l));
      dVal = str(l);
    } else {
      r = factorial(int(r));
      dVal = str(r);
    }
  }
}


void mouseReleased() { //listener that finds what button was clicked
  for (int i = 0; i < numButtons.length; i++) { //numbers
    if (numButtons[i].overButton && dVal.length() < 25) {
      handleEvent(str(numButtons[i].val), true);
    }
  }
  for (int i = 0; i < opButtons.length; i++) {
    if (opButtons[i].overButton) {
      if (opButtons[i].val == 'C') { //clear
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '+') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '-') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == 'x') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '÷') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '=') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '.') {
        handleEvent(".", false);
        //displayOp = str(opButtons[i].val);
      } else if (opButtons[i].val == '±') {
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == 'A') { //exponent auto-calculate
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == 'B') { //square root auto-calculate
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == 'R') { //to power
        handleEvent(str(opButtons[i].val), false);
      } else if (opButtons[i].val == '!') { //factorial auto-calculate
        handleEvent(str(opButtons[i].val), false);
      }
    }
  }
  println("l:" + l + " r:" + r + " op:" + op + " result:" + result + " left:" + left);
}

void updateDisplay() {
  if (dVal.length() < 18) { //adjusts text size based on number of characters
    textSize(35);
  } else if (dVal.length() < 20) {
    textSize(33);
  } else if (dVal.length() < 22) {
    textSize(31);
  } else if (dVal.length() < 24) {
    textSize(29);
  } else {
    textSize(27);
  }

  textAlign(RIGHT);
  text(dVal, width - 13, 47);
}

void performCalculation() {
  if (op == '+') {
    result = l + r;
  } else if (op == '-') {
    result = l - r;
  } else if (op == 'x') {
    result = l * r;
  } else if (op == '÷') {
    result = l / r;
  } else if (op == 'ʸ') {
    result = pow(l, r);
  }

  dVal = str(result);
  l = result;
  left = true;
}

int factorial (int x) { //x! value put into x (l or r) will be cast as int
  if (x == 1) {
    minusCount = 1;
  } else if (x <= 0) { //negatives return 0
    factFinish = true;
    return 0;
  } else {
    minusCount = x - 1;
  }
  while (factFinish == false) {
    x = x * minusCount;
    minusCount = minusCount - 1;
    if (minusCount <= 0) {
      factFinish = true;
    }
  }

  factFinish = false; //reset
  minusCount = 0; //reset

  return x;
}
