#include <stdio.h>
#include <stdlib.h>
float kalman(float mpu_value,float bno_value,float mpu_accuracy,float bno_accuracy)
{
    float constant=mpu_accuracy/(mpu_accuracy+bno_accuracy);
    return bno_value+constant*(mpu_value-bno_value);
}
int main()
{
    float mpu6050[10] = {0.0, 11.68, 18.95, 23.56, 25.72, 25.38, 22.65, 18.01, 10.14, -0.26};
    float bno55[10] = {0.0,9.49, 16.36, 21.2, 23.16, 22.8, 19.5, 14.85, 6.79, -2.69};
    float result[10];
    printf("average results:\n");
    int i;
    for(i=0;i<10;i++)
        result[i]=kalman(mpu6050[i],bno55[i],0.78,0.92);
    for(i=0;i<10;i++)
        printf("%.1f ",result[i]);
    return 0;
    //i couldnt continue the task to the end because i had an exam today and i have exam tomorrow so i have to study
}
