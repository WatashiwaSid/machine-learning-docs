#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<math.h>
int main()
{
int gd = DETECT, gm;
int x1=100, x2=300, y1=120, y2=250;
int x,y;
float m,c;
m = (float)(y2-y1)/(x2-x1);
c = y1 - m*x1;
initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
for(x=x1; x<=x2; x++)
{
	y = (int)(m * x + c +0.5);
	putpixel(x,y,YELLOW);
	delay(10);
}
getch();
cleardevice();
return 0;
}
