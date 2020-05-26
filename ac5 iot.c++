#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

int cont = 0;

void setup() {
 
  lcd.begin(16, 2);
  
}

void loop() {
lcd.setCursor(0, 0);
lcd.print("ESCOLHA A OPCAO:");
lcd.setCursor(1, 1);
lcd.print("FIX  PASS  TEX");
  
  if (digitalRead(6) == LOW){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("LUIZ A S ORTEGA");
      lcd.setCursor(1, 1);
      lcd.print("R.A: 1903543");
      delay(2000);
  
  }if (digitalRead(7) == LOW){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("LUIZ R.A: 1903543");
      delay(2000);
   
  }if (digitalRead(7) == LOW){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("LUIZ R.A: 1903543");
      delay(2000);
    
     }}