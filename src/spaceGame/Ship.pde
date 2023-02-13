class Ship {
  int x, y, w, ammo, turretCount, health;
  PImage ship, ship1;
  boolean imageSwitch = true;
  boolean playImage = true; //true and false are two different ships
  int switchCount = 0;

  //contructor
  Ship() {
    x = 0;
    y = 0;
    w = 90;
    //ammo = 1000;
    turretCount = 1;
    health = 5;
    ship = loadImage("ship.png");
    ship1 = loadImage("ship1.png");
  }

  void display() {
    imageMode(CENTER);
    ship.resize(w, w);
    ship1.resize(w, w);

    if (imageSwitch == true && switchCount > 20) {
      imageSwitch = false;
      switchCount = 0;
      playImage = false;
    } else if (imageSwitch == false && switchCount > 20) {
      imageSwitch = true;
      switchCount = 0;
      playImage = true;
    } else {
      switchCount++;
    }

    if (playImage) {
      image(ship, x, y);
    } else if (!playImage) {
      image(ship1, x, y);
    }
  }

  void move (int tempx, int tempy) {
    x = tempx;
    y = tempy;
  }

  //boolean fire () {
  //  if (ammo > 0) {
  //    ammo--;
  //    return true;
  //  } else {
  //    return false;
  //  }
  //}

  boolean intersect(Rock rock) {
    float d = dist(x, y, rock.x, rock.y);
    if (d < rock.diameter / 2 + 10) {
      return true;
    } else {
      return false;
    }
  }
  
  boolean intersectP(PowerUp powerUp) {
    float d = dist(x, y, powerUp.x, powerUp.y);
    if (d < powerUp.diameter / 2) {
      return true;
    } else {
      return false;
    }
  }
}
