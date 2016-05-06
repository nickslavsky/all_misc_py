#include <stdio.h>
#include <math.h> 
#include <stdlib.h>
#include <time.h>
typedef int bool;
#define true 1
#define false 0

bool is_within_exclusion(double x, double y, int offsetX, int offsetY, int leftX, int leftY)
{
	if (x>leftX && x<leftX+offsetX && y>leftY && y<leftY+offsetY)
	{
		return true;
	}
	else
	{
		return false;
	}
}

double random(int ceiling)
{
	return ((double)rand()/(double)(RAND_MAX)) * (double)ceiling;
}

__declspec(dllexport) double averageDistanceLamina(long N, int side_length, int leftX, int leftY, int offsetX, int offsetY)
{
	long dist_count = 0;
	double dist_sum = 0.0;
	double prevX = 0.0;
	double prevY = 0.0;
	srand((unsigned int)time(NULL));
	while(prevX == 0.0)
	{
		double x1 = random(side_length);
		double y1 = random(side_length);
		if(!is_within_exclusion(x1, y1, offsetX, offsetY, leftX, leftY))
		{
			prevX=x1;
			prevY=y1;
		}
	}
	while(dist_count < N)
	{
		double x1 = random(side_length);
		double y1 = random(side_length);
		if(!is_within_exclusion(x1, y1, offsetX, offsetY, leftX, leftY))
		{
			dist_sum += sqrt( (x1-prevX)*(x1-prevX) + (y1-prevY)*(y1-prevY) );
			prevX=x1;
			prevY=y1;
			dist_count++;
		}		
	}
	return dist_sum / (dist_count-1);
}



      
  
