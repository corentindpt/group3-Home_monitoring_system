/*----------------------------------------*/
/*Programmer : Corentin Dupont            */
/*Management of lighting                  */
/*Last modification : april 24 2020       */
/*----------------------------------------*/

/*--------------Variables-----------------*/
int ledPin = 2;                // choose the pin for the LED
int inputPin = 3;               // choose the input pin (for PIR sensor)
int pirState = LOW;             // we start, assuming no motion detected
int val = 0;                    // variable for reading the pin status

/*----------------------------------------*/

/*--------------Loop setup----------------*/
void setup()
{
  Serial.begin(9600);
  pinMode(inputPin, INPUT);
  pinMode(ledPin, OUTPUT);
}
/*----------------------------------------*/

/*--------------Main loop----------------*/
void loop()
{
  if (LdrRead() <= 400)
  {
    val = digitalRead(inputPin);  // read input value
    Serial.println(val);
    val = digitalRead(inputPin);  // read input value
    if (val == HIGH)
    {
      // check if the input is HIGH
      digitalWrite(ledPin, HIGH);  // turn LED ON
      delay(3000);
      digitalWrite(ledPin, LOW);  // turn LED ON
      if (pirState == LOW)
      {
        // we have just turned on
        Serial.println("Motion detected!");
        // We only want to print on the output change, not state
        pirState = HIGH;
      }
    }
    else
    {
      if (pirState == HIGH)
      {
        // we have just turned of
        Serial.println("Motion ended!");
        // We only want to print on the output change, not state
        pirState = LOW;
      }
    }
  }


}
/*----------------------------------------*/

int LdrRead()
{
  int valeur = analogRead(A0);
  Serial.println(valeur);
  delay(250);
  return valeur ;

}
