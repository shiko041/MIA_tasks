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