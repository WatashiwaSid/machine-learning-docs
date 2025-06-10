#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<stdlib.h>
int main()
{
int gd = DETECT, gm, p=100, q=100, r=20;
double x,y,x2;
initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
x=0,y=r;
x2=r/sqrt(2);
while(x<=x2)
{
	y = sqrt(r*r - x*x);
	putpixel(x+p, y+q, RED);
	putpixel(-x+p, -y+q, RED);
	putpixel(x+p, -y+q, GREEN);
	putpixel(-x+p, y+q, GREEN);
	putpixel(y+p, x+q, YELLOW);
	putpixel(-y+p, -x+q, YELLOW);
	putpixel(y+p, -x+q, BLUE);
	putpixel(-y+p, x+q, BLUE);
	x++;
}
getch();
closegraph();
return 0;
}
