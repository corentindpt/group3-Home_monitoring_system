/*----------------------------------------*/
/*Programmer : Corentin Dupont            */
/*Management of servo motor               */
/*Last modification : april 21 2020       */
/*----------------------------------------*/

/*--------------Librairies----------------*/
#include <Servo.h> //Servomotor
/*----------------------------------------*/

/*---------------Objects------------------*/
Servo lock;
/*----------------------------------------*/


/*--------------Variables-----------------*/
int a = 1; // test variable for detection if = 1 there is someone known
/*----------------------------------------*/


/*--------------Loop setup----------------*/
void setup()
{
  Serial.begin(9600);
  lock.attach(9);   // Attach the servomotor to pin D9
  init_servo();
}
/*----------------------------------------*/


/*--------------Main loop----------------*/
void loop()
{
  management_door();
}
/*----------------------------------------*/

/*----servo motor initialization----*/
void init_servo(void)
{
  Serial.println("Initialisation");
  lock.write(0);
  delay(1500);
}
/*----------------------------------------*/

/*--------------management_door loop----------------*/
void management_door(void)
{
  if (a == 1)
  {
    Serial.println("Door open");
    lock.write(90);
  }
  else
  {
    Serial.println("Door close");
    lock.write(0);
  }
}
