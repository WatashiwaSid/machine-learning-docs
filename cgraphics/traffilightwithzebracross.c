#include<stdio.h>
#include<conio.h>
#include<dos.h>
#include<graphics.h>
int main()
{
int gd = DETECT, gm;
initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
setfillstyle(1, DARKGRAY);
rectangle(150,150,270,390);
floodfill(151,151,WHITE);

// RED LIGHT
setfillstyle(1, RED);
circle(210, 190, 20);
floodfill(211,191, WHITE);

// YELLOW LIGHT
setfillstyle(1, YELLOW);
circle(210, 260, 20);
floodfill(211,261, 15);

//green light
setfillstyle(1, GREEN);
circle(210, 330, 20);
floodfill(211, 331, 15);

//ZEBRA
setfillstyle(1, 15);
rectangle(390,350,410,410);
floodfill(391,351, 15);

setfillstyle(1, BLACK);
rectangle(420, 350, 440, 410);
floodfill(421, 351, 15);

setfillstyle(1,15);
rectangle(450,350,470,410);
floodfill(451,351,15);

setfillstyle(1,BLACK);
rectangle(480,350,500,410);
floodfill(481,351,15);

getch();
closegraph();
return 0;
}
