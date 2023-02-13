class Rock {
  //make movement frame by frame? use random to pick set speeds
  int x, y, diameter, speed;
  PImage rock;

  //constructor
  Rock() {
    x = int(random(width));
    y = -50;
    diameter = int(random(30, 100));
    speed = int(random(2, 7));
    rock = loadImage("rock.png");
  }

  void display() {
    rock.resize(diameter, diameter);
    imageMode(CENTER);
    image(rock, x, y);
  }

  void move() {
    y += speed;
  }

  boolean reachedBottom() {
    if(y > height + 100) {
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
