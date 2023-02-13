class Laser {
  //make super laser?
  int x, y, w, h, speed;

  //constructor
  Laser(int x, int y) {
    this.x = x;
    this.y = y + 22;
    w = 4;
    h = 10;
    speed = 5;
  }

  void display() {
    rectMode(CENTER);
    noStroke();
    fill(18, 201, 91);
    rect(x, y, w, h);
  }

  void move() {
    y -= speed;
  }

  boolean reachedTop() {
    if (y < -5) {
      return true;
    } else {
      return false;
    }
  }

  boolean intersect(Rock rock) {
    float d = dist(x, y, rock.x, rock.y);
    if (d < rock.diameter / 2) {
      return true;
    } else {
      return false;
    }
  }
}
