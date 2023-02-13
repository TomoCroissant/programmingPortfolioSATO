class PowerUp {
  int x, y, diameter, speed;
  char val;
  PImage healthShip;

  //constructor
  PowerUp() {
    x = int(random(width));
    y = -50;
    diameter = 85;
    speed = int(random(2, 7));
    healthShip = loadImage("ship.png");
    if (int(random(2)) == 0) {
      val = 'h';
    } else {
      val = 'a';
    }
  }

  void display() {
    healthShip.resize(diameter, diameter);
    imageMode(CENTER);
    image(healthShip, x, y);
  }

  void move() {
    y += speed;
  }

  boolean reachedBottom() {
    if (y > height + 100) {
      return true;
    } else {
      return false;
    }
  }

  //boolean intersect(Laser laser) {
  //  float d = dist(x, y, laser.x, laser.y);
  //  if (d < 10) {
  //    return true;
  //  } else {
  //    return false;
  //  }
  //}
}
