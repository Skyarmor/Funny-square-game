from cmu_graphics import *
import random

app.stepsPerSecond = 60
app.background = rgb(120, 120, 120)
enemyai = Label(0, 900, 900)
aftertutorial = Label(0, 900, 900)
antispam = []
wall1 = Rect(900, 100, 50, 50, fill='black')
wall2 = Rect(900, 100, 50, 50, fill='black')
wall3 = Rect(900, 100, 50, 50, fill='black')
wall4 = Rect(900, 100, 50, 50, fill='black')
wall5 = Rect(900, 100, 50, 50, fill='black')
wall6 = Rect(900, 100, 50, 50, fill='black')
wall7 = Rect(900, 100, 50, 50, fill='black')
wall8 = Rect(900, 100, 50, 50, fill='black')
wall9 = Rect(900, 100, 50, 50, fill='black')
wall10 = Rect(900, 100, 50, 50, fill='black')
wall11 = Rect(900, 100, 50, 50, fill='black')
fullwallbutton = Rect(900, 900, 50, 50, fill='red')
fullwallbuttonsign = Rect(900, 900, 40, 40, fill='darkred')
fullwall = Rect(900, 0, 50, 400, fill='black')
fullwallsign = Rect(900, 0, 10, 400, fill='purple')
fullwalldiag = Rect(900, 0, 50, 400, fill='black')
fullwallsigndiag = Rect(900, 0, 10, 400, fill='purple')
deathplate = Rect(900, 100, 50, 50, fill='red')
enemydiag = Rect(9999, 9999, 50, 50, fill='red')
enemydiag2 = Rect(9999, 9999, 50, 50, fill='red')
enemydiagsign1 = Line(950, 950, 900, 900)
enemydiagsign2 = Line(950, 950, 900, 900)
enemydiag2sign1 = Line(950, 950, 900, 900)
enemydiag2sign2 = Line(950, 950, 900, 900)
enemymimic = Rect(900, 200, 50, 50, fill='red')
enemymimicsign = Circle(225,
                        225,
                        15,
                        fill='red',
                        border='orange',
                        borderWidth=8)
enemymover = Rect(99999, 99999, 50, 50, fill='purple')
teleporter = Rect(250, 250, 50, 50, fill='white', opacity=80)
lockedteleporter = Rect(900, 900, 50, 50, fill='yellow', opacity=80)
lockedteleportermover = Rect(900, 900, 50, 50, fill='yellow', opacity=80)
tele1 = Circle(900, 900, 25, fill='blue')
tele2 = Circle(900, 900, 25, fill='orange')
tele3 = Circle(900, 900, 25, fill='purple')
tele4 = Circle(900, 900, 25, fill='yellow')
green = Label(100, 900, 900)
red = Label(0, 900, 900)
tutorialtext = Label('WASD to move. E to reset the level.', 200, 250, size=20)
player = Rect(0, 0, 50, 50, fill=rgb(red.value, green.value, 0))
gameover = Label('GAME OVER', 200, 200, size=45, fill='white', opacity=0)
level = Label(0, 390, 10)
death2 = Label(0, 900, 900)

movecountervertical = Label(5, 20, 375, font='monospace', size=25)
movecounterhorizontal = Label(5, 20, 345, font='monospace', size=25)


def death():
    if (green.value >= 0.5):
        green.value -= 0.5
    if (gameover.opacity <= 99.5):
        gameover.opacity += 0.5
    if (red.value <= 99.5):
        red.value += 0.5
    level.value == 0
    movecounterhorizontal.value = -1
    movecountervertical.value = -1


def enemytick():
    if (player.centerX > enemydiag.centerX
            and player.centerY > enemydiag.centerY):
        enemydiag.centerX += 50
        enemydiag.centerY += 50
    if (player.centerX < enemydiag.centerX
            and player.centerY < enemydiag.centerY):
        enemydiag.centerX -= 50
        enemydiag.centerY -= 50
    if (player.centerX > enemydiag.centerX
            and player.centerY < enemydiag.centerY):
        enemydiag.centerX += 50
        enemydiag.centerY -= 50
    if (player.centerX < enemydiag.centerX
            and player.centerY > enemydiag.centerY):
        enemydiag.centerX -= 50
        enemydiag.centerY += 50
    if (player.centerX > enemydiag2.centerX
            and player.centerY > enemydiag2.centerY):
        enemydiag2.centerX += 50
        enemydiag2.centerY += 50
    if (player.centerX < enemydiag2.centerX
            and player.centerY < enemydiag2.centerY):
        enemydiag2.centerX -= 50
        enemydiag2.centerY -= 50
    if (player.centerX > enemydiag2.centerX
            and player.centerY < enemydiag2.centerY):
        enemydiag2.centerX += 50
        enemydiag2.centerY -= 50
    if (player.centerX < enemydiag2.centerX
            and player.centerY > enemydiag2.centerY):
        enemydiag2.centerX -= 50
        enemydiag2.centerY += 50


def constantenemytick():
    if (player.centerX > enemymover.centerX):
        enemymover.centerX += 1
    if (player.centerX < enemymover.centerX):
        enemymover.centerX -= 1
    if (player.centerY < enemymover.centerY):
        enemymover.centerY -= 1
    if (player.centerY > enemymover.centerY):
        enemymover.centerY += 1


def onKeyPress(key):
    antispam.append(level.value)
    aftertutorial.value = random.randint(10, 18)
    if (aftertutorial.value in antispam):
        aftertutorial.value = random.randint(10, 18)
    aftertutorial.value += 0.5
    if (key == 'e' and level.value > 0):
        level.value -= 0.5
        green.value = 100
        red.value = 0
        gameover.opacity = 0
        death2.value = 0
        enemydiag.centerX = 9000
        enemymover.centerX = 9000
        enemydiag2.centerX = 9000

    if (key == 'e' and level.value == 0):
        green.value = 100
        red.value = 0
        gameover.opacity = 0
        death2.value = 0
    enemyai.value = random.randint(1, 2)
    if (movecounterhorizontal.value == 0 and movecountervertical.value == 0):
        movecounterhorizontal.value = -1
        movecountervertical.value = -1
##wasd movement
    if key == 'w' and player.centerY >= 75 and movecountervertical.value > 0:
        player.centerY -= 50
        movecountervertical.value -= 1
        enemymimic.centerY += 50
        enemytick()
    if key == 's' and player.centerY <= 325 and movecountervertical.value > 0:
        player.centerY += 50
        movecountervertical.value -= 1
        enemymimic.centerY -= 50
        enemytick()
    if key == 'a' and player.centerX >= 75 and movecounterhorizontal.value > 0:
        player.centerX -= 50
        movecounterhorizontal.value -= 1
        enemymimic.centerX += 50
        enemytick()
    if key == 'd' and player.centerX <= 325 and movecounterhorizontal.value > 0:
        player.centerX += 50
        movecounterhorizontal.value -= 1
        enemymimic.centerX -= 50
        enemytick()


##wall collisions
    if (key == 'w' and player.centerY == wall1.centerY
            and player.centerX == wall1.centerX
            or key == 'w' and player.centerY == wall2.centerY
            and player.centerX == wall2.centerX
            or key == 'w' and player.centerY == wall3.centerY
            and player.centerX == wall3.centerX
            or key == 'w' and player.centerY == wall4.centerY
            and player.centerX == wall4.centerX
            or key == 'w' and player.centerY == wall5.centerY
            and player.centerX == wall5.centerX
            or key == 'w' and player.centerY == wall6.centerY
            and player.centerX == wall6.centerX
            or key == 'w' and player.centerY == wall7.centerY
            and player.centerX == wall7.centerX
            or key == 'w' and player.centerY == wall8.centerY
            and player.centerX == wall8.centerX
            or key == 'w' and player.centerY == wall9.centerY
            and player.centerX == wall9.centerX
            or key == 'w' and player.centerY == wall10.centerY
            and player.centerX == wall10.centerX
            or key == 'w' and player.centerY == wall11.centerY
            and player.centerX == wall11.centerX):
        player.centerY += 50
        movecountervertical.value += 1
    if (key == 's' and player.centerY == wall1.centerY
            and player.centerX == wall1.centerX
            or key == 's' and player.centerY == wall2.centerY
            and player.centerX == wall2.centerX
            or key == 's' and player.centerY == wall3.centerY
            and player.centerX == wall3.centerX
            or key == 's' and player.centerY == wall4.centerY
            and player.centerX == wall4.centerX
            or key == 's' and player.centerY == wall5.centerY
            and player.centerX == wall5.centerX
            or key == 's' and player.centerY == wall6.centerY
            and player.centerX == wall6.centerX
            or key == 's' and player.centerY == wall7.centerY
            and player.centerX == wall7.centerX
            or key == 's' and player.centerY == wall8.centerY
            and player.centerX == wall8.centerX
            or key == 's' and player.centerY == wall9.centerY
            and player.centerX == wall9.centerX
            or key == 's' and player.centerY == wall10.centerY
            and player.centerX == wall10.centerX
            or key == 's' and player.centerY == wall11.centerY
            and player.centerX == wall11.centerX):
        player.centerY -= 50
        movecountervertical.value += 1
    if (key == 'a' and player.centerY == wall1.centerY
            and player.centerX == wall1.centerX
            or key == 'a' and player.centerY == wall2.centerY
            and player.centerX == wall2.centerX
            or key == 'a' and player.centerY == wall3.centerY
            and player.centerX == wall3.centerX
            or key == 'a' and player.centerY == wall4.centerY
            and player.centerX == wall4.centerX
            or key == 'a' and player.centerY == wall5.centerY
            and player.centerX == wall5.centerX
            or key == 'a' and player.centerY == wall6.centerY
            and player.centerX == wall6.centerX
            or key == 'a' and player.centerY == wall7.centerY
            and player.centerX == wall7.centerX
            or key == 'a' and player.centerY == wall8.centerY
            and player.centerX == wall8.centerX
            or key == 'a' and player.centerY == wall9.centerY
            and player.centerX == wall9.centerX
            or key == 'a' and player.centerY == wall10.centerY
            and player.centerX == wall10.centerX
            or key == 'a' and player.centerY == wall11.centerY
            and player.centerX == wall11.centerX
            or key == 'a' and player.centerX == fullwall.centerX
            or key == 'a' and player.centerX == fullwalldiag.centerX):
        player.centerX += 50
        movecounterhorizontal.value += 1
    if (key == 'd' and player.centerY == wall1.centerY
            and player.centerX == wall1.centerX
            or key == 'd' and player.centerY == wall2.centerY
            and player.centerX == wall2.centerX
            or key == 'd' and player.centerY == wall3.centerY
            and player.centerX == wall3.centerX
            or key == 'd' and player.centerY == wall4.centerY
            and player.centerX == wall4.centerX
            or key == 'd' and player.centerY == wall5.centerY
            and player.centerX == wall5.centerX
            or key == 'd' and player.centerY == wall6.centerY
            and player.centerX == wall6.centerX
            or key == 'd' and player.centerY == wall7.centerY
            and player.centerX == wall7.centerX
            or key == 'd' and player.centerY == wall8.centerY
            and player.centerX == wall8.centerX
            or key == 'd' and player.centerY == wall9.centerY
            and player.centerX == wall9.centerX
            or key == 'd' and player.centerY == wall10.centerY
            and player.centerX == wall10.centerX
            or key == 'd' and player.centerY == wall11.centerY
            and player.centerX == wall11.centerX
            or key == 'd' and player.centerX == fullwall.centerX
            or key == 'd' and player.centerX == fullwalldiag.centerX):
        player.centerX -= 50
        movecounterhorizontal.value += 1


def onKeyRelease(key):
    if (player.centerX == teleporter.centerX and player.centerY
            == teleporter.centerY and movecounterhorizontal.value != -1
            and movecountervertical.value != -1
            or player.centerX == lockedteleporter.centerX and player.centerY
            == lockedteleporter.centerY and enemymimic.centerX >= 500
            or player.centerX == lockedteleportermover.centerX
            and player.centerY == lockedteleportermover.centerY
            and enemymover.centerX >= 500 and level.value <= 9):
        level.value += 0.5
    elif (player.centerX == teleporter.centerX and player.centerY
          == teleporter.centerY and movecounterhorizontal.value != -1
          and movecountervertical.value != -1
          or player.centerX == lockedteleporter.centerX and player.centerY
          == lockedteleporter.centerY and enemymimic.centerX >= 500
          or player.centerX == lockedteleportermover.centerX
          and player.centerY == lockedteleportermover.centerY
          and enemymover.centerX >= 500 and level.value >= 10):
        level.value = aftertutorial.value


def onStep():
    if (enemydiag.centerX >= 500):
        fullwalldiag.centerX = 999
    if (enemymover.centerX >= 500):
        lockedteleportermover.fill = 'white'
    else:
        lockedteleportermover.fill = 'yellow'
    if (enemymimic.centerX >= 500):
        lockedteleporter.fill = 'white'
    else:
        lockedteleporter.fill = 'yellow'
    if (enemymover.centerX >= player.centerX - 50
            and enemymover.centerY >= player.centerY - 50
            and enemymover.centerX <= player.centerX + 50
            and enemymover.centerY <= player.centerY + 50):
        death()
    if (player.centerX == fullwallbutton.centerX
            and player.centerY == fullwallbutton.centerY):
        fullwall.centerX = 900
    constantenemytick()
    ##teleporters#
    if (player.centerX == tele1.centerX and player.centerY == tele1.centerY):
        player.centerX = tele2.centerX
        player.centerY = tele2.centerY
    if (enemymimic.centerX == tele1.centerX
            and enemymimic.centerY == tele1.centerY):
        enemymimic.centerX = tele2.centerX
        enemymimic.centerY = tele2.centerY
    if (enemymover.centerX >= tele1.centerX - 50
            and enemymover.centerY >= tele1.centerY - 50
            and enemymover.centerX <= tele1.centerX + 50
            and enemymover.centerY <= tele1.centerY + 50):
        enemymover.centerX = tele2.centerX
        enemymover.centerY = tele2.centerY
    if (enemydiag.centerX == tele1.centerX
            and enemydiag.centerY == tele1.centerY):
        enemydiag.centerX = tele2.centerX
        enemydiag.centerY = tele2.centerY
    if (player.centerX == tele3.centerX and player.centerY == tele3.centerY):
        player.centerX = tele4.centerX
        player.centerY = tele4.centerY
    if (enemymimic.centerX == tele3.centerX
            and enemymimic.centerY == tele3.centerY):
        enemymimic.centerX = tele4.centerX
        enemymimic.centerY = tele4.centerY
    if (enemymover.centerX >= tele3.centerX - 50
            and enemymover.centerY >= tele3.centerY - 50
            and enemymover.centerX <= tele3.centerX + 50
            and enemymover.centerY <= tele3.centerY + 50):
        enemymover.centerX = tele4.centerX
        enemymover.centerY = tele4.centerY
    if (enemydiag.centerX == tele3.centerX
            and enemydiag.centerY == tele3.centerY):
        enemydiag.centerX = tele4.centerX
        enemydiag.centerY = tele4.centerY
    if (fullwall.centerX >= 500):
        fullwallbuttonsign.fill = 'orange'
    else:
        fullwallbuttonsign.fill = 'darkred'

    enemydiagsign1.x1 = enemydiag.centerX - 25
    enemydiagsign1.y1 = enemydiag.centerY - 25
    enemydiagsign1.x2 = enemydiag.centerX + 25
    enemydiagsign1.y2 = enemydiag.centerY + 25
    enemydiagsign2.x1 = enemydiag.centerX + 25
    enemydiagsign2.y1 = enemydiag.centerY - 25
    enemydiagsign2.x2 = enemydiag.centerX - 25
    enemydiagsign2.y2 = enemydiag.centerY + 25
    enemydiag2sign1.x1 = enemydiag2.centerX - 25
    enemydiag2sign1.y1 = enemydiag2.centerY - 25
    enemydiag2sign1.x2 = enemydiag2.centerX + 25
    enemydiag2sign1.y2 = enemydiag2.centerY + 25
    enemydiag2sign2.x1 = enemydiag2.centerX + 25
    enemydiag2sign2.y1 = enemydiag2.centerY - 25
    enemydiag2sign2.x2 = enemydiag2.centerX - 25
    enemydiag2sign2.y2 = enemydiag2.centerY + 25
    enemymimicsign.centerX = enemymimic.centerX
    enemymimicsign.centerY = enemymimic.centerY
    fullwallsign.centerX = fullwall.centerX
    fullwallsign.centerY = fullwall.centerY
    fullwallbuttonsign.centerX = fullwallbutton.centerX
    fullwallbuttonsign.centerY = fullwallbutton.centerY
    fullwallsigndiag.centerX = fullwalldiag.centerX
    fullwallsigndiag.centerY = fullwalldiag.centerY

    if (movecounterhorizontal.value == -1 or movecountervertical.value == -1
            or player.centerX == enemydiag.centerX
            and player.centerY == enemydiag.centerY
            or player.centerX == enemymimic.centerX
            and player.centerY == enemymimic.centerY or death2.value == 1
            or player.centerX == deathplate.centerX
            and player.centerY == deathplate.centerY
            or enemydiag2.centerX == player.centerX
            and enemydiag2.centerY == player.centerY):
        death()
    if (enemymimic.centerX == deathplate.centerX
            and enemymimic.centerY == deathplate.centerY):
        enemymimic.centerX = 9999
    if (enemydiag.centerX == deathplate.centerX
            and enemydiag.centerY == deathplate.centerY):
        enemydiag.centerX = 9999
    if (enemymover.centerX >= deathplate.centerX - 50
            and enemymover.centerY >= deathplate.centerY - 50
            and enemymover.centerX <= deathplate.centerX + 50
            and enemymover.centerY <= deathplate.centerY + 50):
        enemymover.centerX = 9999
    player.fill = rgb(red.value, green.value, 0)
    ###teleporters/level changers###
    if (level.value == 0.5):
        tutorialtext.value = "However, you have a limited amount of moves"
        tutorialtext.size = 15
        teleporter.centerX = 25
        teleporter.centerY = 25
        wall1.centerX = 125
        wall1.centerY = 125
        wall2.centerX = 75
        wall2.centerY = 175
        wall3.centerY = 75
        wall3.centerX = 175
        movecounterhorizontal.value = 5
        movecountervertical.value = 5
        player.centerX = 275
        player.centerY = 275
        level.value = 1
        print('Object loading for level 1 complete!')
    if (level.value == 1.5):
        tutorialtext.value = "The black square are walls; you can't move through them."
        tutorialtext.size = 12.5
        tutorialtext.centerY += 10
        player.centerX = 25
        player.centerY = 25
        teleporter.centerX = 375
        teleporter.centerY = 375
        movecounterhorizontal.value = 7
        movecountervertical.value = 7
        wall1.centerX = 25
        wall1.centerY = 225
        wall2.centerX = 225
        wall2.centerY = 25
        wall3.centerY = 175
        wall3.centerX = 75
        wall4.centerX = 175
        wall4.centerY = 75
        level.value = 2
        print('Object loading for level 2 complete!')
    if (level.value == 2.5):
        tutorialtext.value = "Red is deadly not only to you.. Portals are a one way instant travel."
        tutorialtext.size = 10
        player.centerX = 375
        player.centerY = 375
        app.background = rgb(150, 120, 120)
        teleporter.centerX = 25
        teleporter.centerY = 175
        tele1.centerX = 375
        tele1.centerY = 75
        tele2.centerX = 125
        tele2.centerY = 25
        wall1.centerX = 25
        wall1.centerY = 225
        wall2.centerX = 225
        wall2.centerY = 25
        wall3.centerX = 75
        wall3.centerY = 175
        wall2.centerX = 125
        wall2.centerY = 125
        enemydiag.centerX = 25
        enemydiag.centerY = 375
        movecounterhorizontal.value = 4
        movecountervertical.value = 11
        level.value = 3
        print('Object loading for level 3 complete!')
    if (level.value == 3.5):
        tutorialtext.value = "You can move against black walls to trick entities."
        tutorialtext.fill = 'white'
        tutorialtext.size = 12.5
        app.background = rgb(150, 120, 120)
        player.centerX = 25
        player.centerY = 175
        wall1.centerX = 75
        wall1.centerY = 125
        wall2.centerY = 75
        wall2.centerX = 75
        wall3.centerX = 75
        wall3.centerY = 225
        wall4.centerX = 75
        wall4.centerY = 275
        wall5.centerX = 75
        wall5.centerY = 325
        wall6.centerX = 75
        wall6.centerY = 25
        wall7.centerX = 75
        wall7.centerY = 375
        tele1.centerX = 900
        tele2.centerX = 900
        teleporter.centerX = 900
        lockedteleporter.centerX = 375
        lockedteleporter.centerY = 125
        enemymimic.centerX = 325
        enemymimic.centerY = 175
        deathplate.centerX = 175
        deathplate.centerY = 175
        movecounterhorizontal.value = 8
        movecountervertical.value = 8
        enemydiag.centerX = 9999
        level.value = 4
        print('Object loading for level 4 complete!')
    if (level.value == 4.5):
        tutorialtext.centerX = 900
        app.background = rgb(160, 120, 120)
        player.centerX = 375
        player.centerY = 125
        lockedteleportermover.centerX = 25
        lockedteleportermover.centerY = 175
        movecountervertical.value = 30
        movecounterhorizontal.value = 30
        wall1.centerX = 75
        wall1.centerY = 125
        wall2.centerY = 75
        wall2.centerX = 75
        wall3.centerX = 75
        wall3.centerY = 225
        wall4.centerX = 75
        wall4.centerY = 275
        wall5.centerX = 75
        wall5.centerY = 325
        wall6.centerX = 75
        wall6.centerY = 25
        wall7.centerX = 75
        wall7.centerY = 175
        enemymover.centerX = 125
        enemymover.centerY = 375
        deathplate.centerX = 175
        deathplate.centerY = 175
        lockedteleporter.centerX = 900
        level.value = 5
        print('Object loading for level 5 complete!')
    if (level.value == 5.5):
        app.background = rgb(160, 120, 120)
        player.centerX = 25
        player.centerY = 175
        lockedteleportermover.centerX = 900
        level.value = 6
        deathplate.centerX = 900
        teleporter.centerX = 375
        teleporter.centerY = 25
        wall1.centerX = 75
        wall1.centerY = 125
        wall2.centerY = 75
        wall2.centerX = 75
        wall3.centerX = 75
        wall3.centerY = 225
        wall4.centerX = 75
        wall4.centerY = 275
        wall5.centerX = 75
        wall5.centerY = 325
        wall6.centerX = 75
        wall6.centerY = 25
        wall7.centerX = 75
        wall7.centerY = 175
        wall8.centerX = 75
        wall8.centerY = 375
        tele1.centerX = 25
        tele1.centerY = 25
        tele3.centerX = 25
        tele3.centerY = 375
        tele4.centerX = 325
        tele4.centerY = 25
        tele2.centerX = 375
        tele2.centerY = 75
        wall9.centerX = 325
        wall9.centerY = 75
        wall10.centerX = 275
        wall10.centerY = 25
        wall11.centerX = 375
        wall11.centerY = 125
        deathplate.centerX = 375
        deathplate.centerY = 75
        movecountervertical.value = 4
        movecounterhorizontal.value = 1
        print('object loading for level 6 complete')
    if (level.value == 6.5):
        app.background = rgb(160, 120, 120)
        player.centerX = 375
        player.centerY = 25
        teleporter.centerX = 900
        teleporter.centerY = 900
        wall1.centerX = 900
        wall1.centerY = 900
        wall2.centerY = 900
        wall2.centerX = 900
        wall3.centerX = 900
        wall3.centerY = 900
        wall4.centerX = 900
        wall4.centerY = 900
        wall5.centerX = 900
        wall5.centerY = 900
        wall6.centerX = 900
        wall6.centerY = 900
        wall7.centerX = 900
        wall7.centerY = 900
        wall8.centerX = 900
        wall8.centerY = 900
        tele1.centerX = 900
        tele1.centerY = 900
        tele3.centerX = 900
        tele3.centerY = 900
        tele4.centerX = 900
        tele4.centerY = 900
        tele2.centerX = 900
        tele2.centerY = 900
        wall9.centerX = 900
        wall9.centerY = 900
        wall10.centerX = 900
        wall10.centerY = 900
        wall11.centerX = 900
        wall11.centerY = 900
        deathplate.centerX = 900
        deathplate.centerY = 900
        enemydiag.centerX = 375
        enemydiag.centerY = 375
        tele1.centerX = 175
        tele1.centerY = 175
        tele2.centerX = 75
        tele2.centerY = 25
        teleporter.centerX = 25
        teleporter.centerY = 125
        movecounterhorizontal.value = 5
        movecountervertical.value = 5
        level.value = 7
        print('object loading for level 7 complete')
    if (level.value == 7.5):
        app.background = rgb(160, 120, 120)
        player.centerX = 25
        player.centerY = 125
        teleporter.centerX = 900
        enemydiag.centerX = 9999
        tele1.centerX = 900
        tele2.centerX = 900
        fullwall.centerX = 225
        movecounterhorizontal.value = 100
        movecountervertical.value = 100
        tele1.centerX = 75
        tele1.centerY = 325
        tele2.centerX = 275
        tele2.centerY = 325
        fullwallbutton.centerX = 375
        fullwallbutton.centerY = 125
        deathplate.centerX = 325
        deathplate.centerY = 75
        enemymover.centerX = 175
        enemymover.centerY = 25
        lockedteleportermover.centerX = 25
        lockedteleportermover.centerY = 25
        level.value = 8
        print('object loading for level 8 complete')
    if (level.value == 8.5):
        lockedteleportermover.centerX = 900
        player.centerX = 25
        player.centerY = 25
        fullwallbutton.centerX = 900
        tele1.centerX = 900
        tele2.centerX = 900
        deathplate.centerX = 900
        fullwalldiag.centerX = 75
        enemydiag.centerX = 425
        enemydiag.centerY = 175
        deathplate.centerX = 125
        deathplate.centerY = 175
        movecountervertical.value = 5
        movecounterhorizontal.value = 7
        teleporter.centerX = 375
        teleporter.centerY = 175
        wall1.centerX = 175
        wall1.centerY = 175
        wall2.centerX = 225
        wall2.centerY = 175
        wall3.centerX = 275
        wall3.centerY = 175
        level.value = 9
        print('Object loading for level 9 complete')
    if (level.value == 9.5):
        wall1.centerX = 900
        wall1.centerY = 900
        wall2.centerX = 900
        wall2.centerY = 900
        wall3.centerX = 900
        wall3.centerY = 900
        teleporter.centerX = 900
        deathplate.centerX = 900
        movecountervertical.value = 100
        movecounterhorizontal.value = 100
        player.centerX = 375
        player.centerY = 175
        wall1.centerX = 325
        wall1.centerY = 175
        enemydiag.centerX = 25
        enemydiag.centerY = 175
        teleporter.centerX = 25
        teleporter.centerY = 175
        tele2.centerX = 225
        tele2.centerY = 25
        tele1.centerX = 375
        tele1.centerY = 125
        level.value = 10
        print('Object loading for level 10 complete')
    if (level.value == 10.5):
        level.value = 11
        print('Object loading for level 11 complete')
        enemydiag.centerX = 900
        tele1.centerX = 900
        tele2.centerX = 900
        wall1.centerX = 900
        teleporter.centerX = 900
        player.centerX = 25
        player.centerY = 25
        teleporter.centerX = 375
        teleporter.centerY = 275
        movecounterhorizontal.value = 100
        movecountervertical.value = 100
        enemydiag.centerX = 375
        enemydiag.centerY = 25
        enemydiag2.centerX = 25
        enemydiag2.centerY = 375
        tele1.centerX = 325
        tele1.centerY = 25
        tele2.centerX = 125
        tele2.centerY = 125
        tele4.centerX = 125
        tele4.centerY = 125
        tele3.centerX = 25
        tele3.centerY = 325
        gameover.value = "THANKS FOR PLAYING!!"
        gameover.size = 20


cmu_graphics.run()
