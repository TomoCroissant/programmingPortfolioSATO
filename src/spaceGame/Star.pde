class Star {
  int x, y, diameter, speed;

  //constructor
  Star() {
    x = int(random(width));
    y = int(random(height));
    diameter = ceil(random(6));
    speed = 1;
  }

  void display() {
    noStroke();
    fill(245);
    circle(x, y, diameter);
  }

  void move() {
    if (y > height + 7) {
      y = -7;
    } else {
      y += speed;
    }
  }

  boolean reachedBottom() {
    return true;
  }
}
