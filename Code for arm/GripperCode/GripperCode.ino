int Motor1 = 5;
int Motor2 = 6;

void VaccumGrip(){
  digitalWrite(Motor1, HIGH);
  digitalWrite(Motor2, LOW); 
}

void StopVaccum(){
  digitalWrite(Motor1, LOW);
  digitalWrite(Motor2, LOW);
}



void setup() {
  // put your setup code here, to run once:
  digitalWrite(Motor1, OUTPUT);
  digitalWrite(Motor2, OUTPUT);
  Serial.begin(115200); 

}

void loop() {
  if (Serial.available() > 0){
    String msg = Serial.readStringUntil(';');

    if (msg == "GRAB"){
      VaccumGrip();
    }
    if (msg == "NOGRAB"){
      StopVaccum();
    }
  }

}
