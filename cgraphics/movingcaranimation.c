#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
void main()
{
int gd = DETECT,gm;
int i;
initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
for(i=0; i<=220; i++)
{
 setcolor(GREEN);
 line(0+i, 300, 210+i, 300);
 line(50+i, 300, 75+i, 270);
 line(75+i, 270, 150+i, 270);
 line(150+i, 270, 165+i, 300) ;
 line(0+i, 300, 0+i, 330);
 line(210+i, 300, 210+i, 330);
 circle(65+i, 330, 15);
 circle(65+i, 330, 2);
 circle(145+i, 330, 15);
 circle(145+i, 330, 2);
 line(0+i, 330, 50+i, 330);
 line(80+i, 330, 130+i, 330);
 line(210+i, 330, 160+i, 330);
 delay(100);
 cleardevice();
}
}
