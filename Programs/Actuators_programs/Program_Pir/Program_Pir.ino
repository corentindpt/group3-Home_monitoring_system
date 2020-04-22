/*----------------------------------------*/
/*Programmer : Corentin Dupont            */
/*Management of lighting                  */
/*Last modification : april 21 2020       */
/*----------------------------------------*/

/*--------------Variables-----------------*/
const int piroutpin = 3;
const int ledPin = 2;
int buttonstate = 0;
/*----------------------------------------*/

/*--------------Loop setup----------------*/
void setup() {
  Serial.begin(9600);
  pinMode(piroutpin, INPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(piroutpin, LOW);
  digitalWrite(ledPin, LOW);
  delay(50);
}
/*----------------------------------------*/

/*--------------Main loop----------------*/
void loop()
{
  buttonstate = digitalRead(piroutpin);
  //Serial.println(buttonstate);
  if (buttonstate == HIGH)
  {
    digitalWrite(ledPin, HIGH);
    delay(10000);
  }
  else
  {
    Serial.println("led off");
    digitalWrite(ledPin, LOW);
  }
}
/*----------------------------------------*/
