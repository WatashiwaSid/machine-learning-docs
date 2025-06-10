#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
int main()
{
int gd = DETECT, gm;
int i;
initgraph(&gd, &gm, "C:\\TURBOC3\BGI");
for(i=0; i<=220; i++)
{
	setcolor(YELLOW);
	circle(100+i, 300, 20);
	circle(200+i, 300, 20);
	circle(100+i, 300, 2);
	circle(200+i, 300, 2);
	line(100+i, 300, 150+i, 250);
	line(150+i, 250, 200+i, 300);
	line(100+i, 300, 200+i, 300);
	line(150+i, 250, 150+i, 230);
	line(140+i, 230, 160+i, 230);
	line(200+i, 300, 210+i, 270);
	line(210+i, 270, 190+i, 270);

	delay(100);
	cleardevice();
}
getch();
closegraph();
return 0;
}
