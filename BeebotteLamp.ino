/**
 Beebotte-driven lamp
 
 python script on linux side gets lamp switch status from beebotte
 this sketch uses that to control pin 4

**/

const int relay = 4;

#include <Bridge.h>
#include <Process.h>


void setup() {
  pinMode(relay, OUTPUT);
  digitalWrite(relay, HIGH);

  Bridge.begin();

  Process p;
  p.runShellCommand("/root/read_lamp.py &");
}

void loop() {  
  
   char lamp[5];

  
   Bridge.get("lamp", lamp, 5);
   
   if(lamp[0] == 'o' && lamp[1] == 'n') {
       digitalWrite(relay, LOW);
   }
   else {
       digitalWrite(relay, HIGH);
   }
   delay(100);
  
}

