

int message = 0;

int r = 0 ;
void setup() {
  Serial.begin(9600);
  pinMode(6, OUTPUT);

}

void loop() {
  if (Serial.available()!=0)  
  {
    Serial.println("Lecture port serie");
    r=Serial.read();

    if( r == 48)
    {
      digitalWrite(6,HIGH);
    }
    else
    {
      digitalWrite(6,LOW);
    }
  }
}





