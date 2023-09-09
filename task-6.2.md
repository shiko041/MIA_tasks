# Task 6.2

![Arduino Simulation for Wall-E rotary motor](Task%206%202%20204c07b4503148c3b2d589ba0a9d657b/Powerful_Borwo.png)

Arduino Simulation for Wall-E rotary motor

```arduino
//defining channel pins
#define Channel_A 2
#define Channel_B 3
long long counter=0;
void setup()
{
  Serial.begin(9600);
  //defining pins as iunput
  pinMode(Channel_A, INPUT_PULLUP);
  pinMode(Channel_B, INPUT_PULLUP);
  //calling intterupt to count
  attachInterrupt(digitalPinToInterrupt(Channel_A),ISR_ENCODER_Channel_A,CHANGE);
  attachInterrupt(digitalPinToInterrupt(Channel_B),ISR_ENCODER_Channel_B,CHANGE);
}

void loop()
{
  //Serial.println(counter);
}
//moving clock wise
void ISR_ENCODER_Channel_A(void)
{
  if(digitalRead(Channel_A)!=digitalRead(Channel_B))
    counter++;
  else 
    counter--;
  //Serial.println("moving clockwise");
}
//moving anti clock wise
void ISR_ENCODER_Channel_B(void)
{
  if(digitalRead(Channel_A)==digitalRead(Channel_B))
    counter++;
  else 
    counter--;
   //Serial.println("moving clockwise");
}
```

# Wall-E specs

1. 540 pulse per revolution
2. Diameter of wheel = 40 cm = 0.4 m
3. maximum speed = 0.5 m/s = 50 cm per second

## How to calculate Cuttoff Frequency?

It is well known that $Time=Distance/Speed$

- Distance moved in one revolution: $2*π*r=2*π*0.2=1.2567$m
- $Time=Distance/max speed =1.2567/0.5=2.51327 s$
- now the revolution takes $2.51327 s$ —> $0.3978 rev/sec$
- number of pulses per second: $**540 ∗ 0.3978 = 214.86$ pulse per sec**
- $fc= 214.86 pulse /sec$
- $540 = 2π$  —> $214.85= 0.4 π$
- $fc= 0.4π * 2π=2.5 rad/s$