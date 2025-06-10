#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<math.h>
int main()
{
int gd = DETECT, gm;
float x1=100, x2=300, y1=120, y2=250;
float dx, dy, xn, yn, steps;
int i;
initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
dx = x2-x1;
dy = y2-y1;
if(fabs(dx) >= fabs(dy))
	steps = fabs(dx);
else
	steps = fabs(dy);
xn = dx/steps;
yn = dy/steps;
for(i=1; i<=steps; i++)
{
	putpixel((int)(x1+0.5), (int)(y1+0.5), YELLOW);
	delay(10);
	x1 = x1+xn;
	y1 = y1+yn;
}
getch();
cleardevice();
return 0;
}
