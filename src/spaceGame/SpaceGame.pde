// Tomo Sato | 28 Nov 2022 | SpaceGame

import processing.sound.*;
SoundFile laserSound1, explosion, chargeLaserSound, hitRock, powerUp;

Ship s1;

Timer rockTimer, powerUpTimer;

ArrayList<Rock> rocks = new ArrayList<Rock>();
ArrayList<PowerUp> powerUps = new ArrayList<PowerUp>();
ArrayList<Laser> lasers = new ArrayList<Laser>();

Star [] stars = new Star [110];


int score, level, rockCount, laserCount, charge, anCounter;
boolean play, chargedSound, animationComplete;

PImage heart1, heart2, heart3, heart4, heart5, explosion1, explosion2, explosion3;


void setup () {
  size(900, 900);
  laserSound1 = new SoundFile(this, "laserSound1.wav");
  explosion = new SoundFile(this, "explosion.wav");
  chargeLaserSound = new SoundFile(this, "chargeLaserSound.wav");
  hitRock = new SoundFile(this, "hitRock.wav");
  powerUp = new SoundFile(this, "powerUp.wav");


  s1 = new Ship(); //ship

  rockTimer = new Timer(700); //rocks
  rockTimer.start();

  powerUpTimer = new Timer(15700);
  powerUpTimer.start();

  for (int i = 0; i < stars.length; i++) { //stars
    stars[i] = new Star();
  }



  score = 0;
  level = 1;
  rockCount = 0;
  laserCount = 0;
  charge = 390;
  play = false;
  chargedSound = false;
  animationComplete = false;
  anCounter = 0;

  heart1 = loadImage("ship.png");
  heart2 = loadImage("ship.png");
  heart3 = loadImage("ship.png");
  heart4 = loadImage("ship.png");
  heart5 = loadImage("ship.png");
  explosion1 = loadImage("explosion1.png");
  explosion2 = loadImage("explosion2.png");
  explosion3 = loadImage("explosion3.png");
}


void draw () {
  if (!play) {
    startScreen();
  } else {
    background(50);
    noCursor();


    for (int i = 0; i < stars.length; i++) { //stars
      stars[i].display();
      stars[i].move();
    }

    //HUD
    infoPanel();
    reloadBar();
    health(340, 23);


    //rendering lasers & detect rock collision
    for (int i = 0; i < lasers.size(); i++) {
      Laser l = lasers.get(i);
      for (int j = 0; j < rocks.size(); j++) {
        Rock r = rocks.get(j);
        if (l.intersect(r)) { //intersect
          hitRock.play();
          lasers.remove(l);
          hitAnimation(r.x, r.y, r.diameter);
          r.diameter -= 50;
          if (r.diameter<30) {
            hitAnimation(r.x, r.y, 25);
            rocks.remove(r);
          }

          score += r.diameter;
          rockCount += 1;
        }
        if (l.reachedTop()) { //removes laser when off screen
          lasers.remove(l);
          println("lasers: " + lasers.size());
        } else {
          l.display();
          l.move();
        }
      }
    }

    s1.display(); //player
    s1.move(mouseX, mouseY);

    if (rockTimer.isFinished()) { //rock timer
      rocks.add(new Rock());
      rockTimer.start();
    }

    //rendering rocks & detect ship collision
    for (int i = 0; i < rocks.size(); i++) {
      Rock r = rocks.get(i);
      if (s1.intersect(r)) { //ship intersect
        s1.health -= 1;
        score += 25;
        rockCount++;
        explosion.play();
        hitAnimation(mouseX, mouseY, 150);
        rocks.remove(r);
      }

      if (r.reachedBottom()) { //did rock reach bottom of screen
        rocks.remove(r);
        println("rocks: " + rocks.size());

        score -= r.diameter / 5;
      } else {
        r.display();
        r.move();
      }
    }

    if (powerUpTimer.isFinished()) { //power up timer
      powerUps.add(new PowerUp());
      powerUpTimer.start();
    }

    //rendering powerups & detect ship collision
    if (s1.health < 5) {
      for (int i = 0; i < powerUps.size(); i++) {
        PowerUp p = powerUps.get(i);
        if (s1.intersectP(p)) { //ship intersect
          s1.health += 1;
          charge = 360;
          chargedSound = true;
          powerUps.remove(p);
        }

        if (p.reachedBottom()) { //did powerUp reach bottom of screen
          powerUps.remove(p);
        } else {
          p.display();
          p.move();
        }
      }
    }
    charge++; //increases laser charge
    if (score < 0) { //disallowsw score from going below 0
      score = 0;
    }
    if (charge >= 360) { //shoots 3 when charge is full
      s1.turretCount = 3;
    } else {
      s1.turretCount = 1;
    }
    if (s1.health <= 0) {
      gameOver();
    }
  }
}


void infoPanel() {
  rectMode(CENTER);
  fill(128, 127);
  rect(width/2, 25, width, 50);
  fill(255);
  textSize(25);
  textAlign(LEFT);
  text("Score: " + score, 10, 35);
  text("Accuracy: " + rockCount + " / " + laserCount, 135, 35);
}

void reloadBar() { //the bar that tracks laser charge
  rectMode(CORNER);
  fill(255);
  if (charge < 361) { //moveing bar
    rect(530, 13, charge, 20);
  } else { //stops bar from moving when full
    charge = 360;
    rect(530, 13, charge, 20);
  }

  fill(0); //render unfilled charge bars
  rect(590, 12, 3, 22);
  rect(650, 12, 3, 22);
  rect(710, 12, 3, 22);
  rect(770, 12, 3, 22);
  rect(830, 12, 3, 22);
  rect(890, 12, 3, 22);

  fill(18, 201, 91);
  if (charge >= 60) { //renders lines on bars when reload amount is enough
    rect(590, 12, 3, 22);
  }
  if (charge >= 120) {
    rect(650, 12, 3, 22);
  }
  if (charge >= 180) {
    rect(710, 12, 3, 22);
  }
  if (charge >= 240) {
    rect(770, 12, 3, 22);
  }
  if (charge >= 300) {
    rect(830, 12, 3, 22);
  }
  if (charge >= 360) {
    fill(201, 36, 18); //outlines rectangle in red
    rect(890, 12, 3, 22); //r border
    rect(530, 12, 3, 22); //l border
    rect(530, 12, 360, 3);//t border
    rect(530, 32, 360, 3);//b border

    //charge meter lines
    rect(590, 12, 3, 22);
    rect(650, 12, 3, 22);
    rect(710, 12, 3, 22);
    rect(770, 12, 3, 22);
    rect(830, 12, 3, 22);
    rect(890, 12, 3, 22);

    if (chargedSound) {
      powerUp.play();
      chargedSound = false;
      println("chargedsound");
    }
  }
  if (charge == 359) {
    chargedSound = true;
  }

  rectMode(CENTER);
}

void health (int x, int y) { //health
  heart1.resize(50, 50);
  if (s1.health == 5) {
    image(heart1, x, y);
    image(heart1, x + 35, y);
    image(heart1, x + 70, y);
    image(heart1, x + 105, y);
    image(heart1, x + 140, y);
  } else if (s1.health == 4) {
    image(heart1, x, y);
    image(heart1, x + 35, y);
    image(heart1, x + 70, y);
    image(heart1, x + 105, y);
  } else if (s1.health == 3) {
    image(heart1, x, y);
    image(heart1, x + 35, y);
    image(heart1, x + 70, y);
  } else if (s1.health == 2) {
    image(heart1, x, y);
    image(heart1, x + 35, y);
  } else if (s1.health == 1) {
    image(heart1, x, y);
  } else if (s1.health <= 0) {
    //gameOver(); game over is at bottom of draw loop
  }
}

void startScreen() {
  background(0);
  fill(255);
  textAlign(CENTER);
  textSize(50);
  text("Click or Press any key to START", width/2, height/2);
  if (mousePressed || keyPressed) {
    play = true;
  }
}

void gameOver() {
  background(0);
  fill(255);
  textAlign(CENTER);
  textSize(50);
  text("GAME OVER", width/2, height/2 + 50);
  text("Score: " + score, 250, height / 4 + 30);
  text("Accuracy: " + rockCount + "/" + laserCount, 650, height / 4 + 30);
  play = false;
  noLoop();
}

void mousePressed () {
  handleEvent();
}

void keyPressed() {
  if (key == ' ') {
    handleEvent();
  }
}

void handleEvent() {
  laserSound1.stop();
  chargeLaserSound.stop();

  if (s1.turretCount == 1 && charge > 60) {
    laserSound1.play();
    lasers.add(new Laser(mouseX, mouseY));
    charge = charge - 60; //subtract laser charge
    laserCount++;
  } else if (s1.turretCount == 2 && charge > 120) {
    lasers.add(new Laser(mouseX - 15, mouseY));
    lasers.add(new Laser(mouseX + 15, mouseY));
    charge = charge - 120;
    laserCount++;
  } else if (s1.turretCount == 3 && charge > 180) {
    chargeLaserSound.play();
    lasers.add(new Laser(mouseX - 15, mouseY));
    lasers.add(new Laser(mouseX, mouseY));
    lasers.add(new Laser(mouseX + 15, mouseY));
    charge = charge - 160;
    laserCount++;
  }
}


void hitAnimation (int x, int y, int diameter) {
  explosion1.resize(diameter + 50, diameter + 50);
  explosion2.resize(diameter + 50, diameter + 50);
  explosion3.resize(diameter + 50, diameter + 50);
  while (!animationComplete) {
    if (anCounter < 2) {
      image(explosion1, x, y);
    } else if (anCounter <= 3) {
      image(explosion2, x, y);
    } else if (anCounter <= 5) {
      image(explosion3, x, y);
    } else {
      animationComplete = true;
      println("anTRUE");
    }
    anCounter++;
    println("anCount: " + anCounter);
  }
  animationComplete = false; //reset
  println("anFalse");
  anCounter = 0; //reset
}
