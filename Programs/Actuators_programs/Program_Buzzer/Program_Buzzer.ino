/*----------------------------------------*/
/*Programmer : Corentin Dupont            */
/*Management of door bell                 */
/*Last modification : april 22 2020       */
/*----------------------------------------*/

/*--------------Librairies----------------*/
#include "pitches.h"
/*----------------------------------------*/

/*--------------Variables-----------------*/
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

int a = 1 ; // To simulate the presence of an unknown person if a=1
/*----------------------------------------*/

/*--------------Loop setup----------------*/
void setup()
{
}
/*----------------------------------------*/

/*--------------Main loop----------------*/
void loop()
{
  while (a == 1) //Simulation of the presence of an unknown person
  {
    for (int thisNote = 0; thisNote < 8; thisNote++)
    {
      int noteDuration = 1000 / noteDurations[thisNote];
      tone(8, melody[thisNote], noteDuration);
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      noTone(8);
    }
  }

}
/*----------------------------------------*/
